import streamlit as st
import pandas as pd
import plotly.express as px
from utils.api_handler import get_earthquake_data, get_tsunami_alerts

# Configure Streamlit UI
st.set_page_config(page_title="AI Disaster Alert System", layout="wide")

# Sidebar for page selection
page = st.sidebar.selectbox(
    "Navigate",
    ["🏠 Home", "🌍 Map View", "📊 Impact Analysis", "📸 Crowdsourcing"]
)

# Load Data
earthquake_data = get_earthquake_data()
tsunami_alerts = get_tsunami_alerts()

# -------------------- 🏠 HOME PAGE --------------------
if page == "🏠 Home":
    st.title("🌊 AI-Powered Disaster Alert System")
    st.markdown("### Real-Time Disaster Alerts with AI Predictions")

    # Earthquake Info
    st.subheader("📡 Recent Earthquake Data")
    st.write(earthquake_data)

    # Tsunami Alerts
    st.subheader("⚠️ Active Tsunami Alerts")
    if not tsunami_alerts.empty:
        st.write(tsunami_alerts)
    else:
        st.success("✅ No active tsunami alerts at the moment.")

# -------------------- 🌍 MAP PAGE --------------------
elif page == "🌍 Map View":
    st.title("🌍 Real-Time Disaster Zone Map")
    fig = px.scatter_mapbox(
        earthquake_data,
        lat="latitude",
        lon="longitude",
        color="magnitude",
        size="magnitude",
        hover_data=["location", "time", "tsunami_alert"],
        zoom=2,
        title="Earthquake Hotspots",
    )
    fig.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig)

# -------------------- 📊 IMPACT ANALYSIS PAGE --------------------
elif page == "📊 Impact Analysis":
    st.title("📊 Predicted Impact Analysis")
    
    # Impact Prediction Based on Magnitude
    def predict_impact(mag):
        if mag >= 8.0:
            return "Severe Impact on Life, Property, and Ecosystem"
        elif mag >= 6.0:
            return "Moderate Impact on Coastal Regions"
        else:
            return "Low Impact Expected"
    
    earthquake_data['predicted_impact'] = earthquake_data['magnitude'].apply(predict_impact)
    st.write(earthquake_data[["location", "magnitude", "predicted_impact"]])
    
    # Severity Pie Chart
    impact_count = earthquake_data['predicted_impact'].value_counts()
    fig = px.pie(
        values=impact_count.values,
        names=impact_count.index,
        title="Predicted Impact Distribution"
    )
    st.plotly_chart(fig)

# -------------------- 📸 CROWDSOURCING PAGE --------------------
elif page == "📸 Crowdsourcing":
    st.title("📸 Crowdsourced Impact Reports")
    st.markdown("### Submit Impact Reports from Affected Zones")

    # Form for Crowdsourcing
    with st.form(key="report_form"):
        name = st.text_input("Your Name")
        location = st.text_input("Location of Impact")
        description = st.text_area("Describe the Impact")
        photo = st.file_uploader("Upload Photo (Optional)", type=["jpg", "png", "jpeg"])
        submit_button = st.form_submit_button("Submit Report")

        if submit_button:
            st.success(f"✅ Report Submitted by {name} from {location}!")
