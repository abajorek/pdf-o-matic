#!/usr/bin/env python3
"""
MIDWEST CLINIC SCRAPER 3000
The most ENTHUSIASTIC web scraper you've ever seen!

This scraper downloads concert program PDFs from midwestclinic.org
with MAXIMUM PERSONALITY and MINIMUM CHILL.

Usage:
    python scraper.py --year 2009 --ensemble Buchholz
    python scraper.py --years 2015-2023 --ensemble USAF
    python scraper.py --list ensemble_lists/known_ensembles.txt --years 2010-2023
    python scraper.py --year 2019 --ensemble NorthTexas --boring  # (why tho?)
    python scraper.py --year 2019 --ensemble USAF --chaos  # LET'S GOOOO!!!
"""

import argparse
import os
import sys
import time
import requests
from pathlib import Path
from typing import List, Tuple, Optional
from urllib.parse import quote
import random

# Import our BEAUTIFUL reaction system
sys.path.insert(0, str(Path(__file__).parent))
from ascii_art import reactions

# ============================================================================
# CONFIGURATION
# ============================================================================

BASE_URL = "https://www.midwestclinic.org/user_files_1/pdfs/concerts/{year}/{year}_{ensemble}_Concert.pdf"
RATE_LIMIT_DELAY = 1.0  # seconds - we're CIVILIZED
TIMEOUT = 30  # seconds
OUTPUT_DIR = "programs"

# Colors for terminal (with fallback for boring mode)
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'

# ============================================================================
# STATISTICS TRACKER
# ============================================================================

class Stats:
    def __init__(self):
        self.success = 0
        self.skipped = 0
        self.failed = 0
        self.total = 0

    def add_success(self):
        self.success += 1

    def add_skip(self):
        self.skipped += 1

    def add_failure(self):
        self.failed += 1

# ============================================================================
# THE UNHINGED UI ENGINE
# ============================================================================

class ScraperUI:
    """Handles all the PERSONALITY"""

    def __init__(self, boring: bool = False, chaos: bool = False):
        self.boring = boring
        self.chaos = chaos
        self.colors_enabled = not boring

    def _colorize(self, text: str, color: str) -> str:
        """Add color if not in boring mode."""
        if self.boring:
            return text
        return f"{color}{text}{Colors.RESET}"

    def print_startup(self):
        """Show the startup banner."""
        if self.boring:
            print(reactions.BORING_STARTUP)
            print(self._colorize(random.choice(reactions.BORING_COMPLAINT), Colors.YELLOW))
        else:
            startup = reactions.get_random_startup(chaos=self.chaos)
            print(self._colorize(startup, Colors.CYAN + Colors.BOLD))

    def print_success(self, filename: str, ensemble: str = ""):
        """Show success message."""
        if self.boring:
            print(f"✓ Downloaded: {filename}")
        else:
            message = reactions.get_success_message(ensemble, chaos=self.chaos)
            print(f"{self._colorize('✓', Colors.GREEN)} {self._colorize(filename, Colors.BOLD)}")
            print(f"   └─ {self._colorize(message, Colors.GREEN)}")

    def print_duplicate(self, filename: str):
        """Show duplicate/skip message."""
        if self.boring:
            print(f"⊘ Already exists: {filename}")
        else:
            message = reactions.get_duplicate_message(chaos=self.chaos)
            print(f"{self._colorize('⊘', Colors.YELLOW)} {self._colorize(filename, Colors.BOLD)}")
            print(f"   └─ {self._colorize(message, Colors.YELLOW)}")

    def print_failure(self, filename: str, error_type: str = "404", status_code: Optional[int] = None):
        """Show failure message."""
        if self.boring:
            status_msg = f"({status_code})" if status_code else f"({error_type})"
            print(f"✗ Failed {status_msg}: {filename}")
        else:
            if error_type == "404" or (status_code and status_code == 404):
                message = reactions.get_404_message(chaos=self.chaos)
            else:
                message = reactions.get_connection_error_message(chaos=self.chaos)

            status_msg = f"{status_code}" if status_code else error_type
            print(f"{self._colorize('✗', Colors.RED)} {self._colorize(f'Failed ({status_msg})', Colors.RED)}: {filename}")
            print(f"   └─ {self._colorize(message, Colors.RED)}")

    def print_rate_limit(self):
        """Show rate limiting message with optional rant."""
        if self.boring:
            print("⏳ Rate limiting...")
            return

        message = reactions.get_rate_limit_message()
        print(f"{self._colorize('⏳', Colors.CYAN)} {message}")

        # Sometimes add a rant (50% chance)
        if random.random() < 0.5 and not self.chaos:
            rant = reactions.get_rate_limit_rant()
            for line in rant:
                time.sleep(0.25)  # Dramatic pausing
                print(f"   {self._colorize(line, Colors.CYAN)}")

    def print_progress(self, current: int, total: int, year: str, ensemble: str):
        """Show progress with occasional commentary."""
        progress_text = f"[{current}/{total}] Processing {year} - {ensemble}"

        if self.boring:
            print(f"\n{progress_text}")
            return

        print(f"\n{self._colorize(progress_text, Colors.BLUE + Colors.BOLD)}")

        # Check for ensemble easter eggs
        easter_egg = reactions.get_ensemble_easter_egg(ensemble)
        if easter_egg:
            print(f"├─ {self._colorize(easter_egg, Colors.MAGENTA)}")

        # Random mid-batch commentary
        if reactions.should_show_mid_batch_comment():
            comment = reactions.get_mid_batch_comment()
            print(f"└─ {self._colorize(comment, Colors.CYAN)}")

    def print_summary(self, stats: Stats):
        """Show the final summary with ASCII art glory."""
        if self.boring:
            print("\n" + "="*50)
            print("SUMMARY")
            print("="*50)
            print(f"Successfully Downloaded: {stats.success}")
            print(f"Already Existed: {stats.skipped}")
            print(f"Failed: {stats.failed}")
            print(f"Output Directory: /{OUTPUT_DIR}/")
            print("="*50)
            return

        # THE GLORIOUS SUMMARY
        header = reactions.get_summary_header()
        footer = reactions.get_summary_footer()
        outro = reactions.get_summary_outro()

        print("\n")
        print(self._colorize("╔═════════════════════════════════════════════════╗", Colors.BOLD))
        print(self._colorize(f"║   {header:^44} ║", Colors.BOLD))
        print(self._colorize("╠═════════════════════════════════════════════════╣", Colors.BOLD))
        print(f"║  {self._colorize('✓', Colors.GREEN)} {self._colorize(f'Successfully Yoinked: {stats.success}', Colors.GREEN):54} ║")
        print(f"║  {self._colorize('⊘', Colors.YELLOW)} {self._colorize(f'Already Had (boring): {stats.skipped}', Colors.YELLOW):54} ║")
        print(f"║  {self._colorize('✗', Colors.RED)} {self._colorize(f'Failures (welp): {stats.failed}', Colors.RED):54} ║")
        print("║                                                 ║")
        print(f"║  🎷 {self._colorize(f'YOUR HOARD: /{OUTPUT_DIR}/', Colors.CYAN):46} ║")
        print("║                                                 ║")
        print(f"║  {self._colorize(footer, Colors.MAGENTA):50} ║")
        print(self._colorize("╚═════════════════════════════════════════════════╝", Colors.BOLD))
        print(f"\n{self._colorize(outro, Colors.CYAN)}")

        # Chaos mode gets EXTRA celebration
        if self.chaos and stats.success > 0:
            print(self._colorize("\n🎉🎊🎉 CHAOS REIGNS SUPREME!!! 🎉🎊🎉", Colors.MAGENTA + Colors.BOLD))
            print(self._colorize("WE'RE UNSTOPPABLE!!! NOTHING CAN STOP THE PDF HOARD!!!", Colors.MAGENTA))

# ============================================================================
# CORE SCRAPER FUNCTIONS
# ============================================================================

def download_program(year: int, ensemble: str, ui: ScraperUI, stats: Stats) -> bool:
    """
    Download a single concert program PDF.

    Args:
        year: The year (e.g., 2009)
        ensemble: The ensemble name (e.g., "Buchholz" or "USAF")
        ui: The UI handler
        stats: Statistics tracker

    Returns:
        True if successful, False otherwise
    """
    # Create output directory
    year_dir = Path(OUTPUT_DIR) / str(year)
    year_dir.mkdir(parents=True, exist_ok=True)

    # Build filename and URL
    filename = f"{year}_{ensemble}_Concert.pdf"
    filepath = year_dir / filename
    url = BASE_URL.format(year=year, ensemble=quote(ensemble))

    # Check if already downloaded
    if filepath.exists():
        ui.print_duplicate(filename)
        stats.add_skip()
        return False

    # Download the PDF
    try:
        response = requests.get(url, timeout=TIMEOUT)

        if response.status_code == 200:
            # Success! Save the file
            with open(filepath, 'wb') as f:
                f.write(response.content)
            ui.print_success(filename, ensemble)
            stats.add_success()
            return True
        elif response.status_code == 404:
            # File not found
            ui.print_failure(filename, error_type="404", status_code=404)
            stats.add_failure()
            return False
        else:
            # Other HTTP error
            ui.print_failure(filename, error_type=f"HTTP {response.status_code}", status_code=response.status_code)
            stats.add_failure()
            return False

    except requests.exceptions.Timeout:
        ui.print_failure(filename, error_type="TIMEOUT")
        stats.add_failure()
        return False
    except requests.exceptions.ConnectionError:
        ui.print_failure(filename, error_type="CONNECTION ERROR")
        stats.add_failure()
        return False
    except Exception as e:
        ui.print_failure(filename, error_type=f"ERROR: {str(e)}")
        stats.add_failure()
        return False

def load_ensemble_list(filepath: str) -> List[str]:
    """Load ensemble names from a file (one per line)."""
    ensembles = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):  # Skip empty lines and comments
                ensembles.append(line)
    return ensembles

def parse_year_range(year_range: str) -> List[int]:
    """Parse a year range like '2015-2023' into a list of years."""
    if '-' in year_range:
        start, end = year_range.split('-')
        return list(range(int(start), int(end) + 1))
    else:
        return [int(year_range)]

# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Midwest Clinic Concert Program Scraper with MAXIMUM PERSONALITY',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --year 2009 --ensemble Buchholz
  %(prog)s --years 2015-2023 --ensemble USAF
  %(prog)s --list ensemble_lists/known_ensembles.txt --years 2010-2023
  %(prog)s --year 2019 --ensemble NorthTexas --boring
  %(prog)s --year 2019 --ensemble USAF --chaos
        """
    )

    parser.add_argument('--year', type=int, help='Single year to download')
    parser.add_argument('--years', type=str, help='Year range (e.g., 2015-2023)')
    parser.add_argument('--ensemble', type=str, help='Single ensemble name')
    parser.add_argument('--list', type=str, dest='ensemble_list', help='File with ensemble names (one per line)')
    parser.add_argument('--boring', action='store_true', help='Disable all the fun (WHY?!)')
    parser.add_argument('--chaos', action='store_true', help='Turn EVERYTHING up to 11')

    args = parser.parse_args()

    # Validate arguments
    if not (args.year or args.years):
        parser.error("Must specify --year or --years")

    if not (args.ensemble or args.ensemble_list):
        parser.error("Must specify --ensemble or --list")

    # Parse years
    if args.years:
        years = parse_year_range(args.years)
    else:
        years = [args.year]

    # Parse ensembles
    if args.ensemble_list:
        try:
            ensembles = load_ensemble_list(args.ensemble_list)
        except FileNotFoundError:
            print(f"Error: File not found: {args.ensemble_list}")
            sys.exit(1)
    else:
        ensembles = [args.ensemble]

    # Initialize UI and stats
    ui = ScraperUI(boring=args.boring, chaos=args.chaos)
    stats = Stats()

    # Show startup banner
    ui.print_startup()

    # Calculate total jobs
    total_jobs = len(years) * len(ensembles)
    stats.total = total_jobs
    current_job = 0

    print(f"\n{ui._colorize(f'📋 Jobs queued: {total_jobs}', Colors.BOLD)}")
    print(f"{ui._colorize(f'📅 Years: {len(years)}', Colors.BOLD)}")
    print(f"{ui._colorize(f'🎺 Ensembles: {len(ensembles)}', Colors.BOLD)}\n")

    # Main download loop
    for year in years:
        for ensemble in ensembles:
            current_job += 1

            # Show progress
            ui.print_progress(current_job, total_jobs, str(year), ensemble)

            # Download the program
            download_program(year, ensemble, ui, stats)

            # Rate limiting (be a good citizen)
            if current_job < total_jobs:  # Don't wait after the last one
                ui.print_rate_limit()
                time.sleep(RATE_LIMIT_DELAY)

    # Show final summary
    ui.print_summary(stats)

if __name__ == '__main__':
    main()
