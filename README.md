# HoloRad Python Web Application

A Streamlit-hosted Python web application with an embedded interactive Three.js radiography-room visualization.

## Run locally
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
Open the local URL shown by Streamlit (usually http://localhost:8501).

## Deploy publicly with Streamlit Community Cloud
1. Create a GitHub repository and upload `app.py`, `holorad_scene.html`, and `requirements.txt`.
2. Go to https://share.streamlit.io/ and sign in with GitHub.
3. Select **Create app**, choose the repository, branch, and `app.py`.
4. Deploy. Streamlit will provide a public URL.

## Architecture
- Python + Streamlit: application shell, page configuration and hosting.
- Three.js: interactive browser-side 3D visualization, loaded from jsDelivr CDN.
- The app does not require PyVista/VTK for this initial browser-based interactive scene.

## Notes
- The 3D library is loaded from a public CDN; users need an internet connection.
- This is an educational conceptual model, not manufacturer CAD or engineering-validated geometry.
- It does not generate or simulate ionizing radiation.
