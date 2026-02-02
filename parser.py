import re

TIMING_KEYWORDS = [
    "morning",
    "night",
    "afternoon",
    "evening",
    "before breakfast",
    "after food",
    "once daily",
    "twice daily"
]

def parse_prescription(text):
    lines = text.lower().split("\n")
    prescription = {}

    for line in lines:
        # extract dosage like 500mg
        dose_match = re.search(r"\d+\s?mg", line)
        dose = dose_match.group() if dose_match else None

        # remove dosage & timing words to get medicine name
        name = line
        if dose:
            name = name.replace(dose, "")

        timings = []
        for t in TIMING_KEYWORDS:
            if t in line:
                timings.append(t)
                name = name.replace(t, "")

        name = name.strip()

        if len(name) > 2:
            prescription[name] = {
                "dose": dose,
                "timing": timings
            }

    return prescription
