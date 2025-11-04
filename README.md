# Midwest Clinic Concert Program Scraper

A Python-based web scraper for downloading concert program PDFs from the Midwest Clinic archives. Features include batch downloading, year range support, and... let's just say *enhanced* user feedback.

## Features

- **Single or Batch Downloads**: Download one program or hundreds
- **Year Range Support**: Specify ranges like `2015-2023`
- **Ensemble List Files**: Process multiple ensembles from a text file
- **Smart Duplicate Detection**: Won't re-download existing files
- **Respectful Rate Limiting**: 1-second delays between requests
- **Detailed Statistics**: Track successes, failures, and skips
- **Personality**: This scraper has *opinions* about your download choices

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/midwest-clinic-scraper.git
cd midwest-clinic-scraper

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Basic Examples

Download a single program:
```bash
python scraper.py --year 2009 --ensemble Buchholz
```

Download across multiple years:
```bash
python scraper.py --years 2015-2023 --ensemble USAF
```

Batch download from a file:
```bash
python scraper.py --list ensemble_lists/known_ensembles.txt --years 2010-2023
```

### Command-Line Options

| Option | Description |
|--------|-------------|
| `--year YEAR` | Single year to download (e.g., `--year 2019`) |
| `--years RANGE` | Year range (e.g., `--years 2015-2023`) |
| `--ensemble NAME` | Single ensemble name (e.g., `--ensemble USAF`) |
| `--list FILE` | File containing ensemble names (one per line) |
| `--boring` | Disables personality features for professional environments |
| `--chaos` | Enables maximum personality mode (use at your own risk) |

### Ensemble List Format

Create a text file with one ensemble name per line:

```text
# ensemble_lists/military_bands.txt
USAF
MarinesWest
MarinesEast
PresidentsOwn
ArmyFieldBand
```

Lines starting with `#` are treated as comments.

## Output Structure

Downloaded PDFs are organized by year:

```
programs/
├── 2015/
│   ├── 2015_USAF_Concert.pdf
│   └── 2015_NorthTexas_Concert.pdf
├── 2016/
│   ├── 2016_USAF_Concert.pdf
│   └── 2016_NorthTexas_Concert.pdf
└── ...
```

## URL Pattern

The scraper uses this URL structure:
```
https://www.midwestclinic.org/user_files_1/pdfs/concerts/{YEAR}/{YEAR}_{ENSEMBLE}_Concert.pdf
```

## Tips for Finding Ensemble Names

1. Visit the Midwest Clinic website archives
2. Check program booklets for exact ensemble name formatting
3. Common formats: `SchoolName`, `UniversityName`, `USAF`, `MarinesWest`, etc.
4. Names are case-sensitive and must match the URL format exactly

## Common Ensembles

Some known ensemble names that have performed at Midwest:

**Military Bands:**
- `USAF` - United States Air Force Band
- `MarinesWest` - Marine Band West Coast
- `MarinesEast` - Marine Band East Coast
- `PresidentsOwn` - The President's Own Marine Band
- `ArmyFieldBand` - US Army Field Band

**University Bands:**
- `NorthTexas` - University of North Texas
- `Michigan` - University of Michigan
- `Illinois` - University of Illinois
- `Northwestern` - Northwestern University

**High School Bands:**
- Various high schools (check archives for specific formatting)

**Professional Ensembles:**
- `DallasWinds` - Dallas Winds

## Responsible Usage

This scraper includes:
- 1-second rate limiting between requests
- Respectful error handling
- User-Agent headers identifying the scraper
- Duplicate detection to minimize server load

Please use responsibly and in accordance with Midwest Clinic's terms of service.

## Requirements

- Python 3.7+
- `requests` library

## Troubleshooting

**404 Errors**: The ensemble name might be misspelled or the program might not exist for that year. Check the Midwest Clinic archives for the correct format.

**Connection Timeouts**: The server might be experiencing high traffic. Try again later or increase the rate limiting delay.

**Permission Errors**: Ensure you have write permissions in the directory where you're running the scraper.

## The Personality

Yes, this scraper has *personality*. It provides colorful commentary during downloads because:

1. Scraping is boring and we need entertainment
2. Progress feedback is more engaging with humor
3. You're downloading PDFs of concert programs at midnight and we both know it

Use `--boring` mode if you're:
- Running in a professional environment
- Recording terminal output for documentation
- Allergic to fun (no judgment)

Use `--chaos` mode if you:
- Want maximum entertainment value
- Need motivation during large batch downloads
- Appreciate enthusiastic web scrapers

## License

MIT License - Do whatever you want with this, just don't blame me if it judges your ensemble choices.

## Contributing

Found a bug? Want to add more personality? PRs welcome!

## Disclaimer

This tool is for educational and research purposes. Respect Midwest Clinic's terms of service and bandwidth. The author is not responsible for any inappropriate use or for the scraper's opinions about your taste in wind band literature.

---

*"That's right. We built a web scraper with personality. What are YOU doing with your life?"*
