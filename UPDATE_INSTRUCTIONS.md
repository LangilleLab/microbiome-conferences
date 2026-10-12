# Instructions for the scheduled update

These are the steps Claude follows on every scheduled run. Edit this file to change how updates work; the scheduled task itself only says "follow UPDATE_INSTRUCTIONS.md".

## Scope

List academic, society and nonprofit meetings focused on the microbiome, plus major general microbiology meetings (ASM Microbe, FEMS, CSM, Microbiology Society, ISME, Lake Arrowhead Microbial Genomes and similar). Include courses and workshops with `type: "Course/Workshop"`. Commercial meetings may be listed with `orgType: "Commercial"`. Do not list webinars, single talks, or meetings run by known predatory conference organizers.

## Every run

1. Read `conferences.json`.
2. For each entry whose meeting has not ended, open its `url` (or `src` if the url fails) and check dates, location, format, every deadline, price and size. Update anything that changed. When nothing changed, still set that entry's `verified` to today.
3. Fill gaps when the official page now has them: a deadline that was `tba`, a price band that was "Not yet checked", dates for an `expect` entry. When an expected meeting gets real dates, add `start` and `end`, remove `expect` and `approx`.
4. Remove entries whose `end` date is more than 30 days in the past. For a recurring series, add the next edition as an `expect` entry if it is not already listed.
5. Look for new meetings in the next 24 months. Check the Keystone, GRC, EMBO and EMBL, Cell Symposia, CSHL, Wellcome Connecting Science, FEMS, ISME, ASM and CSM event listings, plus a few web searches such as "microbiome conference 2027" and "microbiome symposium abstract deadline". Add any that fit the scope.
6. Set `last_verified` at the top of the file to today.
7. Run `python3 validate.py`. If it fails, fix the data and run it again. Never commit a file that fails validation.
8. Commit directly to `main` with a message that lists what changed, for example "Update: added X; FEMS abstract deadline now Dec 15; removed CSHL 2026". If nothing changed except verified dates, the message is "Routine check, no changes". Push.

## Rules for the data

* Only record what an official or reputable source states. Never guess a deadline or a date.
* Mark figures that are not published with `"sizeSrc": "est"` or `"priceSrc": "est"`.
* `price` is the standard (non student) delegate rate in US dollars, as a band: "Free", "Under $500", "$500 to $1000", "Over $1000", or "Not yet checked".
* `size` bands: "Under 100", "100 to 500", "500 to 2000", "Over 2000".
* Topics must come from the list in `validate.py`. Add a new topic there only when no existing topic fits.
* Dates are `YYYY-MM-DD`. A deadline without a date uses `"d": null` and a short `tba` note, such as "Not announced (Nov 15 last year)".
* Write plain prose in notes. Do not use hyphens or dashes.
* `src` links to the page the information came from; `url` links to the official meeting page.
