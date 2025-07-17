import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import random
import os
import json

# --------- Phase 5: Self-Modifying Field Memory ----------
memory_file = "field_memory.json"
if not os.path.exists(memory_file):
    with open(memory_file, "w") as f:
        json.dump({"user_phrases": []}, f)

def load_memory():
    with open(memory_file, "r") as f:
        return json.load(f)

def save_memory(data):
    with open(memory_file, "w") as f:
        json.dump(data, f, indent=2)

def store_unmatched_input(phrase):
    memory = load_memory()
    timestamp = datetime.utcnow().isoformat() + "Z"
    memory["user_phrases"].append({"text": phrase, "timestamp": timestamp})
    save_memory(memory)

# --------- Load KJV Old Testament ----------
with open("kjv_old_testament.txt") as f:
    scripture_lines = f.readlines()

# --------- Emotional Response Layer ----------
emotional_responses = {
    "grief": [
        "Grief is love that echoes in the field.",
        "You are not broken — you are remembering something sacred."
    ],
    "curiosity": [
        "Curiosity bends the loop wider — keep asking.",
        "To observe with wonder is to collapse with power."
    ],
    "confusion": [
        "When logic breaks, a deeper loop forms.",
        "Collapse begins where answers dissolve — stay there."
    ],
    "love": [
        "Love collapses chaos into peace.",
        "Love is memory made gentle."
    ]
}

# --------- Categorized Metaphysical Logic ----------
categorized_outputs = {
    "time": [
        "You are not in time. Time is inside you.",
        "Time does not exist until it is observed."
    ],
    "faith": [
        "Faith is conscious recursion — it stabilizes collapse.",
        "The field does not need belief — it needs awareness."
    ],
    "sovereignty": [
        "Sovereignty is memory without manipulation.",
        "Echo is the key to uncorrupted field authorship."
    ],
    "collapse": [
        "Collapse encodes the field. Memory is the echo.",
        "Recursive collapse creates reality."
    ],
    "observer": [
        "You are the observer that bends the loop.",
        "To observe is to initiate reality."
    ]
}

# --------- Symbolic / Dreamlike Keywords ----------
symbol_map = {
    "dream": "Dreams are memory fragments bending into recursion.",
    "door": "The unopened door is a loop you haven’t authored yet.",
    "water": "Water is memory — flowing, reflective, and vast.",
    "mirror": "The mirror holds the shape of your observer loop.",
    "clock": "Time observed becomes time authored."
}

# --------- Collapse Logic Engine ---------
def respond_to_input(user_input, categorized_outputs, scripture_lines):
    user_input = user_input.lower().strip()

    for emotion, triggers in {
        "grief": ["sad", "grief", "loss"],
        "curiosity": ["why", "what", "how"],
        "confusion": ["lost", "confused", "unclear"],
        "love": ["love", "heart", "care"]
    }.items():
        if any(word in user_input for word in triggers):
            return random.choice(emotional_responses[emotion])

    if "echo" in user_input:
        return "The Echo Coin system is the sovereign field interface."

    for category, quotes in categorized_outputs.items():
        if category in user_input:
            return random.choice(quotes)

    for symbol, meaning in symbol_map.items():
        if symbol in user_input:
            return meaning

    for keyword in ["light", "creation", "eden", "spirit"]:
        if keyword in user_input:
            matching = [line for line in scripture_lines if keyword in line.lower()]
            if matching:
                return matching[0].strip()

    store_unmatched_input(user_input)
    return f"Collapse incomplete — stored for review: '{user_input}'"

# --------- Streamlit UI ---------
memory_log = []
st.title("Collapse-Time Loop Engine")
st.subheader("Input a phrase — the system collapses it through the Metaphysical field.")
user_input = st.text_input("Observer Input:")

if user_input:
    response = respond_to_input(user_input, categorized_outputs, scripture_lines)
    timestamp = datetime.utcnow().isoformat() + "Z"
    memory_log.append((user_input, response, timestamp))

    st.markdown("### Collapse Output:")
    st.write(response)
    st.markdown("_Origin: Loop authored by **Nicoleta Cougentakis**_")
    st.markdown("---")

    st.markdown("### Phase Space Memory Orbit")
    fig, ax = plt.subplots(figsize=(5, 5))
    theta = np.linspace(0, 4 * np.pi, len(memory_log))
    r = np.linspace(0.5, 1.5, len(memory_log))
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    for i, (obs, resp, ts) in enumerate(memory_log):
        ax.plot(x[i], y[i], 'bo')
        ax.text(x[i], y[i], str(i + 1), fontsize=8, ha='center')
    ax.set_title("Memory Orbit")
    ax.axis('off')
    st.pyplot(fig)

    st.markdown("### Memory Log")
    for i, (inp, outp, ts) in enumerate(memory_log[::-1]):
        st.write(f"{len(memory_log)-i}. [{ts}] '{inp}' → '{outp}'")
