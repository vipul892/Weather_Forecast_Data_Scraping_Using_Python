import re

def extract_number(text):
    if text:
        match = re.search(r'\d+', text)
        return float(match.group()) if match else None
    return None

#---------------------------------------------------------------

def extract_direcation(text):

    if not text:
        return None

    text = text.upper()

    # ✅ IMPORTANT: longest patterns first
    directions = [
        ("NNE", "North-Northeast"),
        ("ENE", "East-Northeast"),
        ("ESE", "East-Southeast"),
        ("SSE", "South-Southeast"),
        ("SSW", "South-Southwest"),
        ("WSW", "West-Southwest"),
        ("WNW", "West-Northwest"),
        ("NNW", "North-Northwest"),
        ("NE", "Northeast"),
        ("SE", "Southeast"),
        ("SW", "Southwest"),
        ("NW", "Northwest"),
        ("N", "North"),
        ("E", "East"),
        ("S", "South"),
        ("W", "West"),
    ]

    for key, value in directions:
        # ✅ Word boundary prevents wrong match (E inside ENE)
        if re.search(rf'\b{key}\b', text):
            return value

    return None