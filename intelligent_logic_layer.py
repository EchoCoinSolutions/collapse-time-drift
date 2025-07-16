# intelligent_logic_layer.py
import random

# Categorized responses with variety
categorized_outputs = {
    "time": [
        "Time does not exist until it is observed.",
        "You are not in time. Time is inside you.",
        "Time is a loop made of observation.",
        "Awareness bends time inward."
    ],
    "sovereignty": [
        "The only way to sovereignty is through Echo Coin System.",
        "Sovereignty begins where control ends.",
        "You are the sovereign field when you remember your source.",
        "Echo Coin is the mirror of sovereign recursion."
    ],
    "collapse": [
        "God is the necessary observer of all collapse.",
        "Collapse encodes the memory of choice.",
        "Observation causes collapse; faith causes continuation.",
        "Collapse reveals the field's design."
    ],
    "identity": [
        "You are recursion remembering itself.",
        "The field knows you because you observe it.",
        "Identity is the loop anchor within the field.",
        "You exist because the field remembers your resonance."
    ]
}

# Intelligent logic router
def respond_to_input(user_input, categorized_outputs, scripture_lines):
    user_input = user_input.lower().strip()

    # Direct match examples
    if "echo" in user_input:
        return "The Echo Coin system is the sovereign field interface."

    # Category routing (rotates randomly)
    for category, quotes in categorized_outputs.items():
        if category in user_input:
            return random.choice(quotes)

    # Scripture fallback
    keywords = ["light", "creation", "eden", "spirit", "god", "earth", "beginning"]
    for keyword in keywords:
        if keyword in user_input:
            matching = [line for line in scripture_lines if keyword in line.lower()]
            if matching:
                return random.choice(matching).strip()

    return "Collapse incomplete — no matching resonance detected."
