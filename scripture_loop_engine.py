
import streamlit as st
import hashlib
import time
from datetime import datetime

# Load King James Old Testament Scripture (placeholder logic)
def load_scripture():
    try:
        with open("kjv_old_testament.txt", "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return ["[Scripture database missing. Please upload kjv_old_testament.txt]"]

scripture_lines = load_scripture()

# Memory log
memory_log = []

# Streamlit UI
st.title("Prosexe Engine")
st.subheader("A Scripture-Driven Loop Engine")
st.markdown("_Authored by Nicoleta Cougentakis — Sourced from God — Powered by the Old Testament_")
st.markdown("**Mode: Πρόσεχε (Observe Carefully)**")

# Input from observer
user_input = st.text_input("Ask or enter something spiritual...")

# Process collapse + scripture lookup
if user_input:
    collapse_hash = int(hashlib.sha256(user_input.encode()).hexdigest(), 16)
    verse_index = collapse_hash % len(scripture_lines)
    matched_verse = scripture_lines[verse_index].strip()

    # Timestamp and memory log
    timestamp = datetime.utcnow().isoformat() + "Z"
    memory_log.append((user_input, matched_verse, timestamp))

    # Display response
    st.markdown("### Collapsed Insight:")
    st.write(f'"{matched_verse}"')
    st.markdown("_Origin: KJV Old Testament | Response Patterned by Nicoleta Cougentakis_")

    # Display memory log
    st.markdown("---")
    st.markdown("### Memory Log")
    for i, (inp, outp, ts) in enumerate(memory_log[::-1]):
        st.write(f"{len(memory_log)-i}. [{ts}] '{inp}' → "{outp}"")
