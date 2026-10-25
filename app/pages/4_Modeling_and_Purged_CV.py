import sys
from pathlib import Path

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

st.set_page_config(page_title="Modeling & Purged CV", page_icon="🌲", layout="wide")
st.title("🌲 Modeling & Purged CV")
st.caption("AFML Chapters 4, 6-9 · code: `afml_fx.cv.purged_kfold`")

st.info("🚧 Under construction - see the roadmap in README.md.")

# Suggested layout once implemented:
#   1. Concept: one paragraph + key formula (st.latex)
#   2. Interactive controls: pair, date range, parameters (st.sidebar)
#   3. Result chart(s) comparing the AFML method with the naive baseline
#   4. "Why it matters on an FX desk" takeaway
