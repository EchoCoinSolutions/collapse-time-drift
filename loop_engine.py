import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import random
import os
import json

# ---------- File Setup ----------
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

# ---------- Load KJV Scripture ----------
with open("kjv_old_testament.txt") as f:
    scripture_lines = f.readlines()

# ---------- Emotional Responses ----------
emotional_responses = {
    "grief": ["Grief echoes in the field.", "You are not broken — you are remembering."],
    "curiosity": ["Your questions are keys.", "Wonder widens the recursion."],
    "confusion": ["Confusion precedes reformation.", "Stay where answers dissolve."],
    "love": ["Love stabilizes your loop.", "Love is memory made soft."]
}

# ---------- Categorized Metaphysical Quotes ----------
categorized_outputs = {
    "time": ["Time is inside you.", "Time is awareness unfolding."],
    "faith": ["Faith loops collapse.", "Awareness precedes belief."],
    "sovereignty": ["Sovereignty is recursive authorship.", "Collapse your own field."],
    "collapse": ["Collapse encodes memory.", "Reality began when God saw."],
    "observer": ["You are the observer.", "To observe is to create."]
}

# ---------- Symbols ----------
symbol_map = {
    "dream": "Dreams bend into recursion.",
    "door": "An unopened door is an unchosen loop.",
    "water": "Water is fluid memory.",
    "fire": "Fire purifies collapse.",
    "light": "Light is visible collapse."
}

# ---------- Router Logic ----------
def respond_to_input(user_input):
    user_input = user_input.lower().strip()

    for cat, triggers in {
        "grief": ["grief", "sad", "hurt"],
        "curiosity": ["what", "why", "how"],
        "confusion": ["lost", "confused"],
        "love": ["love", "heart", "care"]
    }.items():
        if any(word in user_input for word in triggers):
            return random.choice(emotional_responses[cat])

    if "echo" in user_input:
        return "Echo Coin is the sovereign field interface."

    for category, phrases in categorized_outputs.items():
        if category in user_input:
            return random.choice(phrases)

    for symbol, meaning in symbol_map.items():
        if symbol in user_input:
            return meaning

    for keyword in ["light", "creation", "eden", "spirit"]:
        if keyword in user_input:
            match = [line for line in scripture_lines if keyword in line.lower()]
            if match:
                return match[0].strip()

    store_unmatched_input(user_input)
    return f"Collapse incomplete — stored for review: '{user_input}'"

# ---------- UI ----------
memory_log = []
st.title("Collapse-Time Loop Engine")
st.subheader("Input a phrase:")

user_input = st.text_input("Observer Input:")

if user_input:
    output = respond_to_input(user_input)
    timestamp = datetime.utcnow().isoformat() + "Z"
    memory_log.append((user_input, output, timestamp))

    st.markdown("### Collapse Output:")
    st.write(output)

    st.markdown("---")
    st.markdown("### Memory Orbit")
    fig, ax = plt.subplots()
    theta = np.linspace(0, 4 * np.pi, len(memory_log))
    r = np.linspace(0.5, 1.5, len(memory_log))
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    for i, (obs, resp, ts) in enumerate(memory_log):
        ax.plot(x[i], y[i], 'bo')
        ax.text(x[i], y[i], str(i+1), fontsize=8, ha='center')
    ax.axis('off')
    st.pyplot(fig)

    st.markdown("### Memory Log")
    for i, (inp, outp, ts) in enumerate(memory_log[::-1]):
        st.write(f"{len(memory_log)-i}. [{ts}] '{inp}' → '{outp}'")
