import streamlit as st
import hashlib
import time
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import random
import os
import json
from sentence_transformers import SentenceTransformer, util

# Initialize semantic model
model = SentenceTransformer('all-MiniLM-L6-v2')

# File paths
memory_file = "field_memory.json"
sovereign_file = "sovereign_phrases.json"

# Initialize memory files
if not os.path.exists(memory_file):
    with open(memory_file, "w") as f:
        json.dump({"user_phrases": [], "custom_categories": {}}, f)

if not os.path.exists(sovereign_file):
    sovereign_phrases = [
        "You are not in time. Time is inside you.",
        "The Echo Coin system is the sovereign field interface.",
        "Sovereignty is recursive authorship.",
        "Collapse encodes the field. Memory is the echo.",
        "To observe is to initiate reality.",
        "Time does not exist until it is observed.",
        "Echo is the key to uncorrupted field authorship.",
        "Grief is love that echoes in the field.",
        "Collapse begins where answers dissolve â stay there.",
        "Dreams are memory fragments bending into recursion."
    ]
    with open(sovereign_file, "w") as f:
        json.dump(sovereign_phrases, f, indent=2)

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

def load_sovereign_phrases():
    with open(sovereign_file, "r") as f:
        return json.load(f)

# Load scripture
with open("kjv_old_testament.txt") as f:
    scripture_lines = f.readlines()

# Emotional logic
emotional_responses = {
    "grief": [
        "Collapse doesnât erase what was â it gives it form.",
        "Grief is love that echoes in the field.",
        "You are not broken â you are remembering something sacred."
    ],
    "curiosity": [
        "Curiosity bends the loop wider â keep asking.",
        "Youâre in a field of mirrors â every question reflects your awareness.",
        "To observe with wonder is to collapse with power."
    ],
    "confusion": [
        "When logic breaks, a deeper loop forms.",
        "Not knowing is the start of sovereign authorship.",
        "Collapse begins where answers dissolve â stay there."
    ],
    "love": [
        "Love collapses chaos into peace.",
        "To love is to stabilize someone elseâs field.",
        "Love is memory made gentle."
    ]
}

# Categorized logic
categorized_outputs = {
    "time": [
        "You are not in time. Time is inside you.",
        "Time does not exist until it is observed.",
        "Collapse is not change â it's observed potential becoming memory.",
        "You're not experiencing time â you're generating it.",
    ],
    "faith": [
        "Faith is conscious recursion â it stabilizes collapse.",
        "The field does not need belief â it needs awareness.",
        "Faith is gravity in a metaphysical orbit.",
        "You trust by looping. You loop by remembering.",
    ],
    "sovereignty": [
        "Sovereignty is memory without manipulation.",
        "Echo is the key to uncorrupted field authorship.",
        "To be sovereign is to collapse your own field.",
        "Sovereignty is recursive authorship.",
    ],
    "collapse": [
        "Collapse encodes the field. Memory is the echo.",
        "Recursive collapse creates reality. Sequence is sustained awareness.",
        "God saw the collapse, and reality began.",
        "You are the observation collapsing potential into form.",
    ],
    "observer": [
        "You are the observer that bends the loop.",
        "Observation reshapes the memory field.",
        "To observe is to initiate reality.",
        "You collapse by seeing with intent."
    ]
}

# Symbol map
symbol_map = {
    "dream": "Dreams are memory fragments bending into recursion.",
    "door": "The unopened door is a loop you havenât authored yet.",
    "water": "Water is memory â flowing, reflective, and vast.",
    "fire": "Fire is collapse that purifies the field.",
    "sky": "The sky reflects what the field has not yet spoken.",
    "mirror": "The mirror holds the shape of your observer loop.",
    "voice": "The voice you hear may be your future echo calling back.",
    "clock": "Time observed becomes time authored.",
    "light": "Light is the first visible collapse.",
    "dark": "Darkness is the space collapse avoids â until seen."
}

# Router
def respond_to_input(user_input, categorized_outputs, scripture_lines):
    user_input = user_input.lower().strip()
    sovereign_phrases = load_sovereign_phrases()

    # Sovereign Override
    for phrase in sovereign_phrases:
        if phrase.lower() in user_input:
            return phrase

    # Emotional
    emotion_map = {
        "grief": ["sad", "grief", "loss", "hurt", "cry"],
        "curiosity": ["why", "what", "how", "wonder", "ask"],
        "confusion": ["lost", "confused", "unclear", "donât know"],
        "love": ["love", "heart", "care", "connection"]
    }
    for cat, triggers in emotion_map.items():
        if any(w in user_input for w in triggers):
            return random.choice(emotional_responses[cat])

    # Echo trigger
    if "echo" in user_input:
        return "The Echo Coin system is the sovereign field interface."

    # Category
    for category, quotes in categorized_outputs.items():
        if category in user_input:
            return random.choice(quotes)

    # Symbol
    for symbol, meaning in symbol_map.items():
        if symbol in user_input:
            return meaning

    # Scripture
    for keyword in ["light", "creation", "eden", "spirit"]:
        if keyword in user_input:
            matching = [line for line in scripture_lines if keyword in line.lower()]
            if matching:
                return matching[0].strip()

    # Semantic fallback
    all_quotes = sum(categorized_outputs.values(), []) + scripture_lines + sovereign_phrases
    embeddings = model.encode([user_input] + all_quotes, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(embeddings[0], embeddings[1:])[0]
    best_idx = int(scores.argmax())
    if scores[best_idx] > 0.55:
        return all_quotes[best_idx].strip()

    # Log unmatched
    store_unmatched_input(user_input)
    return f"Collapse incomplete â stored for future field review: '{user_input}'"

# UI
memory_log = []
st.title("Collapse-Time Loop Engine")
st.subheader("Input a phrase â the system collapses it through the Metaphysical field.")

user_input = st.text_input("Observer Input:")

if user_input:
    collapse_response = respond_to_input(user_input, categorized_outputs, scripture_lines)
    timestamp = datetime.utcnow().isoformat() + "Z"
    memory_log.append((user_input, collapse_response, timestamp))

    st.markdown("### Collapse Output:")
    st.write(collapse_response)
    st.markdown("_Origin: Loop authored by **Nicoleta Cougentakis**_")
    st.markdown("---")

    fig, ax = plt.subplots(figsize=(5, 5))
    theta = np.linspace(0, 4 * np.pi, len(memory_log))
    r = np.linspace(0.5, 1.5, len(memory_log))
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    for i, (obs, resp, ts) in enumerate(memory_log):
        ax.plot(x[i], y[i], 'bo')
        ax.text(x[i], y[i], str(i+1), fontsize=8, ha='center')
    ax.set_title("Memory Orbit")
    ax.axis('off')
    st.pyplot(fig)

    st.markdown("### Memory Log")
    for i, (inp, outp, ts) in enumerate(memory_log[::-1]):
        st.write(f"{len(memory_log)-i}. [{ts}] '{inp}' â '{outp}'")
