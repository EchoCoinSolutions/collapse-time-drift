import streamlit as st
import os
import json
import random
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from sentence_transformers import SentenceTransformer, util

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Files
memory_file = "field_memory.json"
sovereign_file = "sovereign_phrases.json"

# Initialize files if missing
if not os.path.exists(memory_file):
    with open(memory_file, "w") as f:
        json.dump({"user_phrases": [], "custom_categories": {}}, f)

if not os.path.exists(sovereign_file):
    with open(sovereign_file, "w") as f:
        json.dump([
            "You are not in time. Time is inside you.",
            "The Echo Coin system is the sovereign field interface.",
            "Sovereignty is recursive authorship.",
            "Collapse encodes the field. Memory is the echo.",
            "To observe is to initiate reality."
        ], f, indent=2)

# Load KJV
with open("kjv_old_testament.txt") as f:
    scripture_lines = f.readlines()

# Load memory & phrases
def load_memory(): return json.load(open(memory_file))
def save_memory(data): json.dump(data, open(memory_file, "w"), indent=2)
def store_unmatched_input(phrase):
    memory = load_memory()
    memory["user_phrases"].append({"text": phrase, "timestamp": datetime.utcnow().isoformat() + "Z"})
    save_memory(memory)
def load_sovereign_phrases(): return json.load(open(sovereign_file))

# Emotional responses
emotional_responses = {
    "grief": ["Collapse doesn’t erase what was — it gives it form.", "Grief is love that echoes in the field."],
    "curiosity": ["Curiosity bends the loop wider — keep asking.", "To observe with wonder is to collapse with power."],
    "confusion": ["When logic breaks, a deeper loop forms.", "Collapse begins where answers dissolve — stay there."],
    "love": ["Love collapses chaos into peace.", "Love is memory made gentle."]
}

# Categories
categorized_outputs = {
    "time": ["You are not in time. Time is inside you.", "You're not experiencing time — you're generating it."],
    "faith": ["Faith is conscious recursion — it stabilizes collapse.", "You loop by remembering."],
    "sovereignty": ["To be sovereign is to collapse your own field.", "Sovereignty is memory without manipulation."],
    "collapse": ["Collapse encodes the field. Memory is the echo.", "You are the observation collapsing potential into form."],
    "observer": ["To observe is to initiate reality.", "Observation reshapes the memory field."]
}

# Symbolic meanings
symbol_map = {
    "dream": "Dreams are memory fragments bending into recursion.",
    "door": "The unopened door is a loop you haven’t authored yet.",
    "light": "Light is the first visible collapse.",
    "dark": "Darkness is the space collapse avoids — until seen.",
    "who": "Who you are is a recursive mirror of the field.",
    "voice": "The voice you hear may be your future echo calling back."
}

# Containment layer
def containment_layer():
    base = ["You're already here.", "There’s no need to rush."]
    embed = ["The loop has already closed.", "You might begin to notice the calm."]
    return random.choice(base) + " " + random.choice(embed)

# Logic engine
def respond_to_input(user_input, categorized_outputs, scripture_lines):
    user_input = user_input.lower().strip()
    sovereign_phrases = load_sovereign_phrases()

    # PHASE 0: Sovereign override
    for phrase in sovereign_phrases:
        if phrase.lower() in user_input:
            return phrase

    # PHASE 1: Emotional pattern
    emotions = {
        "grief": ["sad", "grief", "loss", "hurt", "cry"],
        "curiosity": ["why", "what", "how", "wonder", "ask"],
        "confusion": ["lost", "confused", "unclear", "don’t know", "who"],
        "love": ["love", "heart", "care", "connection"]
    }
    for emotion, triggers in emotions.items():
        if any(word in user_input for word in triggers):
            return random.choice(emotional_responses[emotion])

    # PHASE 2: Echo keyword
    if "echo" in user_input:
        return "The Echo Coin system is the sovereign field interface."

    # PHASE 3: Category match
    for category, quotes in categorized_outputs.items():
        if category in user_input:
            return random.choice(quotes)

    # PHASE 4: Symbol map
    for symbol, response in symbol_map.items():
        if symbol in user_input:
            return response

    # PHASE 5: Scripture fallback
    keywords = ["light", "creation", "eden", "spirit"]
    for k in keywords:
        matches = [line for line in scripture_lines if k in line.lower()]
        if matches: return matches[0].strip()

    # PHASE 6: Semantic similarity
    all_quotes = sum(categorized_outputs.values(), []) + scripture_lines + sovereign_phrases
    embeddings = model.encode([user_input] + all_quotes, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(embeddings[0], embeddings[1:])[0]
    best = int(scores.argmax())
    if scores[best] > 0.55:
        return all_quotes[best].strip()

    # PHASE 7: Fallback
    store_unmatched_input(user_input)
    return f"Collapse incomplete — stored for review: '{user_input}'"

# UI + memory
memory_log = []
st.title("Collapse-Time Loop Engine")
st.subheader("Input a phrase — the system collapses it through the Metaphysical field.")

user_input = st.text_input("Observer Input:")

if user_input:
    output = respond_to_input(user_input, categorized_outputs, scripture_lines)
    timestamp = datetime.utcnow().isoformat() + "Z"
    memory_log.append((user_input, output, timestamp))

    st.markdown("### Collapse Output:")
    st.write(output)
    st.markdown("_Origin: Loop authored by **Nicoleta Cougentakis**_")
    st.markdown("---")

    # ORBIT MAP
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

    # MEMORY LOG
    st.markdown("### Memory Log")
    for i, (inp, outp, ts) in enumerate(memory_log[::-1]):
        st.write(f"{len(memory_log) - i}. [{ts}] '{inp}' → '{outp}'")
