# Microbiome Conference Tracker

A filterable list of upcoming microbiome and microbiology meetings, with abstract deadlines, format, location, size and cost. Maintained by the Langille Lab at Dalhousie University.

## How it works

* `index.html` is the whole website. It loads `conferences.json` and does all filtering and sorting in the browser, so GitHub Pages serves it with no build step.
* `conferences.json` holds the data. Edit this file to add or correct a meeting.
* `validate.py` checks the data. Run `python3 validate.py` before committing.
* `UPDATE_INSTRUCTIONS.md` describes the automatic update, which runs on a schedule, checks every entry against its official page, adds new meetings and commits the result.

## Suggest a meeting or a correction

Use the [issue forms](https://github.com/LangilleLab/microbiome-conferences/issues/new/choose) to suggest a meeting, correct a detail, or request a removal. Each request is checked against the official meeting page during the next scheduled update, which replies on the issue and closes it. You can also edit `conferences.json` directly in a pull request; run `python3 validate.py` first.

## License

The website code (`index.html`, `validate.py`) is released under the MIT License (see `LICENSE`). The conference data (`conferences.json`) is released under CC BY 4.0 (see `LICENSE-DATA`); please credit the Langille Lab Microbiome Conference Tracker when you reuse it.
