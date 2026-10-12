#!/usr/bin/env python3
"""Check conferences.json before it is committed. Exits with an error if anything is malformed."""
import json, re, sys
from datetime import date

ALLOWED = {
    "type": {"Conference", "Course/Workshop"},
    "format": {"In person", "Hybrid", "Virtual"},
    "orgType": {"Society", "Nonprofit", "Academic", "Commercial"},
    "size": {"Under 100", "100 to 500", "500 to 2000", "Over 2000"},
    "price": {"Free", "Under $500", "$500 to $1000", "Over $1000", "Not yet checked"},
    "src": {"pub", "est", ""},
}
TOPICS = {
    "Human gut", "Women's health", "Immunology", "Host microbe interactions",
    "Clinical and translational", "Ecology and evolution", "Methods and bioinformatics",
    "Probiotics and diet", "Therapeutics and regulation", "General microbiology",
    "Animal and One Health", "Oral microbiome", "Environmental microbiology", "Plant microbiome",
}
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

def is_date(s):
    if not isinstance(s, str) or not DATE.match(s):
        return False
    try:
        date.fromisoformat(s)
        return True
    except ValueError:
        return False

def main(path="conferences.json"):
    errors = []
    with open(path) as f:
        data = json.load(f)
    if not is_date(data.get("last_verified")):
        errors.append("last_verified must be YYYY-MM-DD")
    confs = data.get("conferences")
    if not isinstance(confs, list) or not confs:
        sys.exit("conferences must be a non empty list")
    names = set()
    for i, c in enumerate(confs):
        tag = f"[{i}] {c.get('name', '?')}"
        for key in ("name", "org", "orgType", "format", "deadlines", "topics", "size", "price", "url", "src"):
            if key not in c:
                errors.append(f"{tag}: missing {key}")
        if c.get("name") in names:
            errors.append(f"{tag}: duplicate name")
        names.add(c.get("name"))
        if c.get("type", "Conference") not in ALLOWED["type"]:
            errors.append(f"{tag}: bad type {c.get('type')}")
        for key in ("format", "orgType", "size", "price"):
            if key in c and c[key] not in ALLOWED[key]:
                errors.append(f"{tag}: bad {key} {c[key]!r}")
        for key in ("sizeSrc", "priceSrc"):
            if c.get(key, "") not in ALLOWED["src"]:
                errors.append(f"{tag}: bad {key}")
        for t in c.get("topics", []):
            if t not in TOPICS:
                errors.append(f"{tag}: topic {t!r} is not in the allowed list (add it to validate.py if intended)")
        if c.get("start"):
            if not (is_date(c["start"]) and is_date(c.get("end"))):
                errors.append(f"{tag}: start and end must both be YYYY-MM-DD")
            elif c["end"] < c["start"]:
                errors.append(f"{tag}: end is before start")
        elif not c.get("expect"):
            errors.append(f"{tag}: needs either start/end dates or an expect note")
        if c.get("approx") and not is_date(c["approx"]):
            errors.append(f"{tag}: approx must be YYYY-MM-DD")
        for d in c.get("deadlines", []):
            if d.get("d") is None:
                if not d.get("tba"):
                    errors.append(f"{tag}: deadline {d.get('k')} needs a date or tba text")
            elif not is_date(d["d"]):
                errors.append(f"{tag}: deadline {d.get('k')} has bad date {d['d']!r}")
        for key in ("url", "src"):
            if not str(c.get(key, "")).startswith("https://"):
                errors.append(f"{tag}: {key} must start with https://")
        if c.get("verified") and not is_date(c["verified"]):
            errors.append(f"{tag}: verified must be YYYY-MM-DD")
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print(f"OK: {len(confs)} entries")

if __name__ == "__main__":
    main(*sys.argv[1:])
