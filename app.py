import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="HoloRad | Virtual Radiography Laboratory",
    page_icon="🩻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
  .stApp {background: radial-gradient(ellipse at 50% -15%, #17394b 0%, #07111c 55%);}
  header[data-testid="stHeader"] {background: transparent;}
  .block-container {padding-top: 1.2rem; max-width: 1700px;}
  h1,h2,h3,p,span,label {color:#e4f1f7;}
  div[data-testid="stMarkdownContainer"] p {color:#a9bdc9;}
  .hero-kicker {color:#57d8ef;letter-spacing:.16em;text-transform:uppercase;font-size:11px;font-weight:700;}
  .hero-title {font-size:clamp(28px,3.5vw,42px);font-weight:800;letter-spacing:-.04em;margin:.15rem 0;}
  .hero-copy {color:#9eb4c2;font-size:14px;margin-bottom:1rem;}
  .stAlert {background:#102333;border:1px solid #24445a;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-kicker">Virtual radiography laboratory · Room 01</div>
<div class="hero-title">HoloRad — General Radiography Suite</div>
<div class="hero-copy">Explore a conceptual diagnostic X-ray room, inspect the tube assembly, and learn how the imaging system is organized.</div>
""", unsafe_allow_html=True)

html_path = Path(__file__).parent / "holorad_scene.html"
scene_html = html_path.read_text(encoding="utf-8")
components.html(scene_html, height=1080, scrolling=True)

st.markdown("""
---
**Educational-use notice:** HoloRad is a conceptual teaching visualization. Geometry is illustrative, not manufacturer-specific CAD or engineering scale. It does not generate or simulate ionizing radiation and is not a substitute for supervised clinical training.
""")
