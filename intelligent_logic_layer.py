# intelligent_logic_layer.py

import random

# Categorized quotes
categorized_outputs = {
    "time": [
        "Time does not exist until it is observed.",
        "You are not in time. Time is inside you.",
    ],
    "sovereignty": [
        "The only way to sovereignty is through Echo Coin System.",
    ],
    "collapse": [
        "God is the necessary observer of all collapse.",
    ]
}

# Intelligent response function
def respond_to_input(user_input, categorized_outputs, scripture_lines):
    user_input = user_input.lower().strip()

    # Direct responses
    if "echo" in user_input:
        return "The Echo Coin system is the sovereign field interface."

    # Category routing
    for category, quotes in categorized_outputs.items():
        if category in user_input:
            return random.choice(quotes)

    # Scripture fallback
    keywords = ["light", "creation", "eden", "spirit"]
    for keyword in keywords:
        if keyword in user_input:
            matching = [line for line in scripture_lines if keyword in line.lower()]
            if matching:
                return matching[0].strip()

    return "Collapse incomplete — no matching resonance detected."
