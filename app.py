import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import folium_static
import datetime

st.set_page_config(page_title="Infinity Engine", layout="wide")

# Sidebar with branding and license (reuse from radar)
with st.sidebar:
    st.markdown("## 🚀 Infinity Engine")
    st.markdown("Geological research platform for real-time natural resource mapping and development reporting.")
    st.markdown("---")
    st.markdown("### 📜 License")
    st.markdown("""
    **Proprietary Commercial Software**  
    Copyright © 2025 Gesner Deslandes. All rights reserved.

    This software is **licensed**, not sold.  
    Unauthorized copying, distribution, or resale is prohibited.
    """)
    st.markdown("📞 **Prisme Transfer** (Digicel Moncash): `(509) 4738-5663`")
    st.markdown("📧 **Email**: `deslandes78@gmail.com`")
    st.caption("© 2025 GlobalInternet.py")

st.title("🚀 Infinity Engine")
st.markdown("Real‑time natural resource mapping and development reporting")

# Placeholder for map – you can replace with actual geological data
st.subheader("🗺️ Resource Map (Placeholder)")

# Example: create a simple map using folium (you can also use plotly)
m = folium.Map(location=[18.5, -72.3], zoom_start=7, tiles="OpenStreetMap")
# Add a marker for a sample resource location
folium.Marker(
    [18.5, -72.3],
    popup="Sample Resource Site",
    tooltip="Click for info",
    icon=folium.Icon(color="green", icon="info-sign")
).add_to(m)
folium_static(m)

st.subheader("📊 Development Reporting")

# Dummy data – replace with your own data source
data = pd.DataFrame({
    "Site": ["Site A", "Site B", "Site C"],
    "Resource Type": ["Gold", "Copper", "Lithium"],
    "Estimated Value (USD)": [5e6, 3.2e6, 8.7e6],
    "Last Update": [datetime.date(2025, 3, 1), datetime.date(2025, 3, 15), datetime.date(2025, 3, 20)]
})
st.dataframe(data, use_container_width=True)

# Simple chart
fig = px.bar(data, x="Site", y="Estimated Value (USD)", color="Resource Type", title="Resource Estimates")
st.plotly_chart(fig, use_container_width=True)

st.info("This is a demonstration. Replace with your own geological data and mapping logic.")
