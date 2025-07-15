
import hashlib
import json
import re

# Load scripture database
def load_scripture(filepath="kjv_old_testament.txt"):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

# Load echo interpretations
def load_interpretations(filepath="echo_interpretations.json"):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Keyword to scripture tag matching system
def keyword_to_tags(user_input):
    mappings = {
        "time": ["Ecclesiastes 3:1", "Genesis 1:5"],
        "grief": ["Psalm 34:18", "Lamentations 3:31"],
        "fear": ["Isaiah 41:10", "Psalm 23:4"],
        "hope": ["Jeremiah 29:11", "Isaiah 40:31"],
        "guidance": ["Proverbs 3:5", "Psalm 32:8"],
        "sovereignty": ["Exodus 3:14", "Genesis 1:26"],
        "truth": ["Deuteronomy 32:4", "Psalm 119:160"],
        "creation": ["Genesis 1:1", "Psalm 19:1"],
        "faith": ["Habakkuk 2:4", "Proverbs 3:5"],
        "collapse": ["Genesis 3:6", "Ecclesiastes 1:2"]
    }

    matched_tags = []
    for key, verses in mappings.items():
        if re.search(rf"\b{key}\b", user_input.lower()):
            matched_tags.extend(verses)
    return matched_tags

# Echo-aware smart router
def respond_to_input(user_input, scripture_list, echo_dict):
    matched_verses = keyword_to_tags(user_input)

    for verse_ref in matched_verses:
        for verse_line in scripture_list:
            if verse_ref in verse_line:
                # Extract raw verse text
                echo_response = echo_dict.get(verse_ref, None)
                if echo_response:
                    return f"{verse_ref}: {echo_response}"
                else:
                    return verse_line

    # Fallback: deterministic selection
    collapse_hash = int(hashlib.sha256(user_input.encode()).hexdigest(), 16)
    verse_index = collapse_hash % len(scripture_list)
    fallback_line = scripture_list[verse_index]
    fallback_ref = fallback_line.split(" - ")[0] if " - " in fallback_line else "Unknown"
    echo_response = echo_dict.get(fallback_ref, None)

    if echo_response:
        return f"{fallback_ref}: {echo_response}"
    else:
        return fallback_line
