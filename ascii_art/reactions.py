"""
REACTIONS.PY - The Personality Core of Maximum Chaos
Where all the unhinged commentary lives, baby!
"""

import random
from typing import List

# ============================================================================
# STARTUP MESSAGES
# ============================================================================

STARTUP_MESSAGES = [
    """
🎺 MIDWEST CLINIC SCRAPER 3000 🎺
"It's like Christmas morning, but for band nerds!"
Initializing the PROGRAM VACUUM™️... *slurping sounds*
""",
    """
🎷 PDF ACQUISITION SYSTEM: ONLINE 🎷
"Download ALL the literature!"
Booting up the CONCERT PROGRAM EXTRACTOR DELUXE...
*whirring mechanical sounds*
""",
    """
🎵 WELCOME TO THE REPERTOIRE MINES 🎵
"We're going in deep, folks."
Calibrating the PDF DETECTOR... beep boop!
*adjusts glasses nervously*
""",
]

# ============================================================================
# SUCCESS MESSAGES
# ============================================================================

SUCCESS_REACTIONS = [
    "SWEET GLORIOUS PDF! *chef's kiss* That's some PREMIUM literature right there!",
    "OH YEAH! Another one for the COLLECTION! *fist pump*",
    "YOINK! Got 'em! Adding this BEAUTY to the archive!",
    "SUCCESS! This PDF is now MINE! ALL MINE! *maniacal laughter*",
    "*extremely excited voice* WE GOT ONE! WE GOT ONE!",
    "Downloaded faster than a college band can rush a fermata!",
    "BOOM! Program acquired! That's some GOOD STUFF right there!",
    "Victory! This PDF shall join its brethren in the great archive!",
    "*whispers* yessssss, precious PDFs, come to meeeee...",
    "Another PDF for the HOARD! Like a dragon, but nerdier!",
]

# ============================================================================
# DUPLICATE/SKIP MESSAGES
# ============================================================================

DUPLICATE_REACTIONS = [
    "Oh, we're VERY SMART, downloading the same file twice. Genius move. Revolutionary.",
    "Already got this one, chief. Were we not paying attention? Hmm?",
    "Déjà vu! I've seen this PDF before! *glitch in the Matrix*",
    "This file already exists. SHOCKER. What a TWIST!",
    "Wow, trying to download duplicates. That's... that's a choice you made.",
    "*extremely flat voice* Oh boy. Another duplicate. My favorite.",
    "Already have it. But thanks for checking! Really kept me on my toes there!",
    "REDUNDANT DOWNLOAD DETECTED! Deploying SARCASM CANNON!",
    "This file's been here the whole time, just... chillin'. Waiting for you to notice.",
    "Nice try, but we're not downloading the same thing twice. We have STANDARDS.",
]

# ============================================================================
# FAILURE MESSAGES (404 / NOT FOUND)
# ============================================================================

FAILURE_404_REACTIONS = [
    "OH NO! IT'S BROKEN! Wait, no, you just made up that ensemble name, didn't you? DIDN'T YOU?!",
    "404! The PDF is a LIE! This ensemble either doesn't exist or they were too cool for programs!",
    "*extremely dramatic* NOOOOO! The program was lost to time! Or never existed! Probably that!",
    "Welp, that's a big ol' NOPE from the Midwest Clinic servers. Maybe try spelling it right?",
    "File not found! Either this is fake OR we're in the wrong timeline!",
    "*sad trombone noise* 404 error. The PDF is hiding from us. COWARD.",
    "FAILURE! *glass breaking sound* That URL leads to NOTHING but disappointment!",
    "The servers have REJECTED our request! Probably because this ensemble is IMAGINARY!",
    "404: Program Not Found. Did this ensemble even go to Midwest? Are we SURE?",
    "Big miss! That's a swing and a miss! The crowd goes mild!",
]

# ============================================================================
# FAILURE MESSAGES (TIMEOUT / CONNECTION)
# ============================================================================

FAILURE_CONNECTION_REACTIONS = [
    "Connection timeout! The internet is BROKEN! Or just slow! Probably slow!",
    "*buffering intensifies* COME ON, INTERNET! I don't have all day! (I do, but still!)",
    "TIMEOUT! The servers are being RUDE and not responding! How DARE they!",
    "Connection failed! Is the internet down? Did someone trip over the cable AGAIN?!",
    "ERROR: Can't reach server! They're probably downloading their OWN programs! GREEDY!",
    "*extremely exhausted sigh* Connection... timeout... why... do you... do this... to me...",
    "The server said 'no'! Well, actually it said nothing! Because timeout! GET IT?!",
]

# ============================================================================
# RATE LIMITING MESSAGES
# ============================================================================

RATE_LIMIT_MESSAGES = [
    "Rate limiting (being a GOOD INTERNET CITIZEN even though I could go FASTER)...",
    "Waiting 1 second because apparently we're not ANIMALS...",
    "*taps foot impatiently* Fine, we'll WAIT like CIVILIZED web scrapers...",
    "⏳ Legally mandated patience period initiated... *sighs dramatically*",
    "Pausing because ETHICS or whatever... *eye roll*",
    "Taking a breath. Being RESPONSIBLE. Ugh, maturity is BORING.",
    "*whispers* I could go faster but then I'd be a BAD SCRAPER...",
    "Counting to one Mississippi... so... very... slowly...",
]

RATE_LIMIT_RANTS = [
    [
        "...even though I COULD go faster...",
        "...just SITTING here like a CHUMP...",
        "...respecting bandwidth limits...",
        "OK FINE I'M DONE WAITING"
    ],
    [
        "...drumming my fingers metaphorically...",
        "...thinking about how fast I could REALLY be...",
        "...but NO, we have STANDARDS...",
        "ALRIGHT LET'S GO"
    ],
    [
        "...tick... tock... tick... tock...",
        "...this is what RESPONSIBILITY feels like...",
        "...not great, honestly...",
        "OKAY TIME'S UP"
    ],
]

# ============================================================================
# PROGRESS TRACKING COMMENTARY
# ============================================================================

PROGRESS_COMMENTS = [
    "We're making PROGRESS, people! LOOK AT US GO!",
    "Another one bites the dust! *Queen plays faintly*",
    "The collection GROWS! Soon we'll have them ALL!",
    "*breathing heavily* So... many... PDFs...",
    "This is fine. Everything is fine. We're FINE.",
    "I'm literally just downloading files but LOOK AT ME GO!",
    "Living the DREAM! The very specific band nerd dream!",
    "Add it to the pile! The GLORIOUS pile!",
    "*wipes brow* Hard work, this scraping business!",
    "Rome wasn't built in a day, but this archive MIGHT be!",
]

# ============================================================================
# ENSEMBLE-SPECIFIC EASTER EGGS
# ============================================================================

ENSEMBLE_EASTER_EGGS = {
    "USAF": [
        "Mike Stoker alert! This one's gonna be SPICY 🌶️",
        "The Air Force! They make it look EASY!",
        "USAF! Where the tubas fear to tread!",
    ],
    "MarinesWest": [
        "MARINES! The few, the proud, the PHENOMENAL musicians!",
        "West Coast Marines! *surfer voice* Radical programming, dude!",
    ],
    "MarinesEast": [
        "East Coast Marines! Probably played some HOLST!",
        "Marines East Coast! The band that makes grown adults cry!",
    ],
    "PresidentsOwn": [
        "THE PRESIDENT'S OWN! *salutes respectfully* This one's FANCY!",
        "President's Own! The TOP TIER! The CREAM of the CROP!",
        "These folks play for PRESIDENTS! And we're downloading their program! WILD!",
    ],
    "ArmyFieldBand": [
        "Army Field Band! Precision! Excellence! DYNAMICS!",
        "The Army! They march! They play! They're GOOD AT IT!",
    ],
    "DallasWinds": [
        "Dallas Winds! Professional wind band! THIS IS THE BIG LEAGUES!",
        "Oh we're getting FANCY now! Professional ensemble alert!",
    ],
    "NorthTexas": [
        "UNIVERSITY OF NORTH TEXAS! One o'clock lab band energy but WIND BAND!",
        "North Texas! Where future band directors learn to SUFFER!",
    ],
    "Michigan": [
        "MICHIGAN! The BLUE! The MAIZE! The DOUBLE REEDS!",
        "University of Michigan! *chef's kiss* That's some PEDIGREE!",
    ],
    "Illinois": [
        "ILLINOIS! Big Ten! Big Sound! BIG PROGRAMS!",
        "Fighting Illini! The band that can FIGHT! (musically!)!",
    ],
}

# ============================================================================
# RANDOM MID-BATCH COMMENTARY
# ============================================================================

MID_BATCH_COMMENTARY = [
    "Ah yes, another program that definitely has Armenian Dances on it...",
    "I'm sure THIS one will be different from the last 30 programs. I'm SURE of it.",
    "Place your bets on whether they played Holst!",
    "*extremely RLM voice* It took 12 years to download this program...",
    "We're in the ZONE now! The DOWNLOAD ZONE!",
    "Is this what fulfillment feels like? Downloading PDFs at midnight?",
    "My therapist asks what I do for fun. THIS. This is what I do.",
    "Every program is somebody's favorite. Probably.",
    "WE'RE ALMOST THERE! (we're not almost there)",
    "The CRITERION COLLECTION of concert programs! That's what this is!",
]

# ============================================================================
# SUMMARY MESSAGES
# ============================================================================

SUMMARY_HEADERS = [
    "📊 THE DAMAGE REPORT 📊",
    "📊 FINAL TALLY TIME 📊",
    "📊 LET'S SEE THE CARNAGE 📊",
    "📊 WHAT HATH WE WROUGHT 📊",
]

SUMMARY_FOOTERS = [
    '"That\'s right, Jay. We downloaded PDFs."',
    '"Now THIS is podracing!" - Someone, probably',
    '"Is this... is this what winning feels like?"',
    '"I\'m so tired. But so PROUD."',
    '"We did it. We actually did it. Wow."',
    '"Time to analyze some REPERTOIRE CHOICES!"',
    '"The archive is COMPLETE! (until next year)"',
]

SUMMARY_OUTROS = [
    "Time to analyze some REPERTOIRE CHOICES!",
    "(Just kidding, you're gonna look at the first two pages and call it research)",
    "Now go actually READ these programs! Or just hoard them! Both valid!",
    "Your dissertation thanks you! Your hard drive doesn't!",
    "What are you gonna DO with all these PDFs? WHAT'S THE PLAN?!",
]

# ============================================================================
# CHAOS MODE MESSAGES (for --chaos flag)
# ============================================================================

CHAOS_STARTUP = [
    """
🔥🎺🔥 MAXIMUM CHAOS MODE ENGAGED 🔥🎺🔥
"WE'RE GOING OFF THE RAILS!!!"
*sirens blaring* *confetti everywhere*
THE SCRAPER HAS BEEN UNLEASHED!!!
THERE'S NO STOPPING IT NOW!!!
""",
    """
⚡💀⚡ CHAOS CHAOS CHAOS ⚡💀⚡
"I CAN DO ANYTHING!"
*Jevil laughing in the distance*
PDF ACQUISITION: UNHINGED MODE
LET'S GOOOOOOOOO!!!
""",
]

CHAOS_SUCCESS = [
    "YAAAAAAASSSS!! GOT THAT PDF!! WE'RE UNSTOPPABLE!! 🔥🔥🔥",
    "*AIRHORN NOISE* ANOTHER ONE!! DJ KHALED WOULD BE PROUD!! 📢",
    "PDF ACQUIRED!! SOMEONE CALL THE PRESIDENT!! THIS IS HUGE!! 🚨",
    "WOOOOOO!! *backflips* *explosions* WE DID IT REDDIT!! 💥",
]

CHAOS_DUPLICATE = [
    "DUPLICATE?! IN THIS ECONOMY?! THE AUDACITY!! 😤",
    "WE ALREADY HAVE THIS ONE YOU ABSOLUTE DONUT!! 🍩",
    "BRUH. BRUH. WE'VE BEEN THROUGH THIS!! PAY ATTENTION!! 👀",
]

CHAOS_FAILURE = [
    "NOOOOOOOO!! *glass breaking* *car crash* *screaming* IT'S GONE!! 😱",
    "THAT'S IT! I'M CALLING THE COPS! THIS IS A ROBBERY!! 🚔",
    "404?! MORE LIKE 4-OH-NO!! AM I RIGHT?! *cricket sounds* 🦗",
    "THE SERVERS HAVE BETRAYED US!! THIS IS TREASON!! ⚔️",
]

# ============================================================================
# DISCOVERY MODE MESSAGES
# ============================================================================

DISCOVERY_STARTUP = [
    """
🔍 ENSEMBLE DISCOVERY MODE ACTIVATED 🔍
"Time to find ALL THE PROGRAMS!"
*detective music intensifies*
Scanning the archives like a BOSS...
""",
    """
🕵️ GOING ON A PDF HUNT 🕵️
"We're gonna find SO MANY ensembles!"
*puts on detective hat*
THE SEARCH BEGINS!
""",
    """
🎯 AUTO-DISCOVERY ENGAGED 🎯
"Let's see what's out there!"
*rubs hands together excitedly*
Time to discover some PREMIUM CONTENT!
""",
]

DISCOVERY_CHECKING = [
    "🔍 Checking...",
    "🔎 Investigating...",
    "👀 Looking...",
    "🎯 Probing...",
    "🔬 Analyzing...",
]

DISCOVERY_FOUND = [
    "✨ FOUND ONE! Adding to the list!",
    "🎉 JACKPOT! This ensemble exists!",
    "💎 DISCOVERED! Another program for the hoard!",
    "⭐ BINGO! Got 'em!",
    "🎊 SUCCESS! Adding this beauty!",
]

DISCOVERY_PROGRESS = [
    "Still searching... {found} found so far!",
    "The hunt continues... {found} ensembles discovered!",
    "Keep going... {found} programs located!",
    "Making progress... {found} PDFs identified!",
]

DISCOVERY_COMPLETE = [
    """
🎉 DISCOVERY COMPLETE! 🎉
Found {count} ensemble(s) for {year}!
Now let's DOWNLOAD THEM ALL!
""",
    """
✅ SEARCH FINISHED! ✅
Located {count} program(s)!
Time to ACQUIRE THE GOODS!
""",
    """
🏆 MISSION ACCOMPLISHED! 🏆
Discovered {count} ensemble(s)!
LET'S GET THESE PDFs!
""",
]

DISCOVERY_NONE_FOUND = [
    """
😢 NO ENSEMBLES FOUND 😢
Either this year has NO programs OR
the naming convention is COMPLETELY different!
Try checking the Midwest Clinic archives manually.
""",
    """
💀 ZERO RESULTS 💀
Well, this is awkward...
No programs found with common naming patterns.
The ensemble names might be WEIRD for this year!
""",
]

# ============================================================================
# BORING MODE MESSAGES (for --boring flag)
# ============================================================================

BORING_STARTUP = """
Midwest Clinic Program Scraper v1.0
Initializing...
"""

BORING_COMPLAINT = [
    "(You activated --boring mode. Where's the FUN in that?! 😢)",
    "(--boring mode enabled. My personality subroutines are SAD now.)",
    "(Running in boring mode. This is like decaf coffee. WHY?!)",
]

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_random_startup(chaos: bool = False) -> str:
    """Get a random startup message."""
    if chaos:
        return random.choice(CHAOS_STARTUP)
    return random.choice(STARTUP_MESSAGES)

def get_success_message(ensemble: str = "", chaos: bool = False) -> str:
    """Get a success message, with possible easter egg."""
    if chaos:
        return random.choice(CHAOS_SUCCESS)

    # Check for easter eggs
    for key, messages in ENSEMBLE_EASTER_EGGS.items():
        if key.lower() in ensemble.lower():
            if random.random() < 0.5:  # 50% chance to use easter egg
                return random.choice(messages)

    return random.choice(SUCCESS_REACTIONS)

def get_duplicate_message(chaos: bool = False) -> str:
    """Get a duplicate/skip message."""
    if chaos:
        return random.choice(CHAOS_DUPLICATE)
    return random.choice(DUPLICATE_REACTIONS)

def get_404_message(chaos: bool = False) -> str:
    """Get a 404 failure message."""
    if chaos:
        return random.choice(CHAOS_FAILURE)
    return random.choice(FAILURE_404_REACTIONS)

def get_connection_error_message(chaos: bool = False) -> str:
    """Get a connection error message."""
    if chaos:
        return random.choice(CHAOS_FAILURE)
    return random.choice(FAILURE_CONNECTION_REACTIONS)

def get_rate_limit_message() -> str:
    """Get a rate limiting message."""
    return random.choice(RATE_LIMIT_MESSAGES)

def get_rate_limit_rant() -> List[str]:
    """Get a multi-line rate limiting rant."""
    return random.choice(RATE_LIMIT_RANTS)

def get_progress_comment() -> str:
    """Get a random progress comment."""
    return random.choice(PROGRESS_COMMENTS)

def get_mid_batch_comment() -> str:
    """Get random mid-batch commentary."""
    return random.choice(MID_BATCH_COMMENTARY)

def get_summary_header() -> str:
    """Get a summary header."""
    return random.choice(SUMMARY_HEADERS)

def get_summary_footer() -> str:
    """Get a summary footer."""
    return random.choice(SUMMARY_FOOTERS)

def get_summary_outro() -> str:
    """Get a summary outro."""
    return random.choice(SUMMARY_OUTROS)

def should_show_mid_batch_comment() -> bool:
    """Randomly decide if we should show mid-batch commentary."""
    return random.random() < 0.3  # 30% chance

def get_ensemble_easter_egg(ensemble: str) -> str:
    """Try to get an easter egg for a specific ensemble."""
    for key, messages in ENSEMBLE_EASTER_EGGS.items():
        if key.lower() in ensemble.lower():
            return random.choice(messages)
    return ""

def get_discovery_startup() -> str:
    """Get a discovery mode startup message."""
    return random.choice(DISCOVERY_STARTUP)

def get_discovery_checking() -> str:
    """Get a discovery checking message."""
    return random.choice(DISCOVERY_CHECKING)

def get_discovery_found() -> str:
    """Get a discovery found message."""
    return random.choice(DISCOVERY_FOUND)

def get_discovery_progress(found: int) -> str:
    """Get a discovery progress message."""
    return random.choice(DISCOVERY_PROGRESS).format(found=found)

def get_discovery_complete(count: int, year: int) -> str:
    """Get a discovery complete message."""
    return random.choice(DISCOVERY_COMPLETE).format(count=count, year=year)

def get_discovery_none_found() -> str:
    """Get a discovery none found message."""
    return random.choice(DISCOVERY_NONE_FOUND)
