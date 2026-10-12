# Microbiome Conference Tracker

A filterable list of upcoming microbiome and microbiology meetings, with abstract deadlines, format, location, size and cost. Maintained by the Langille Lab at Dalhousie University.

## How it works

* `index.html` is the whole website. It loads `conferences.json` and does all filtering and sorting in the browser, so GitHub Pages serves it with no build step.
* `conferences.json` holds the data. Edit this file to add or correct a meeting.
* `validate.py` checks the data. Run `python3 validate.py` before committing.
* `UPDATE_INSTRUCTIONS.md` describes the automatic update, which runs on a schedule, checks every entry against its official page, adds new meetings and commits the result.

## Suggest a meeting or a correction

Open an issue with the meeting name, its official link, and what should change.

## License

The website code (`index.html`, `validate.py`) is released under the MIT License (see `LICENSE`). The conference data (`conferences.json`) is released under CC BY 4.0 (see `LICENSE-DATA`); please credit the Langille Lab Microbiome Conference Tracker when you reuse it.
