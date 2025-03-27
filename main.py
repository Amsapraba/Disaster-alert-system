import streamlit as st

# Configure Page
st.set_page_config(
    page_title="🌊 Tsunami Alert System",
    page_icon="🌊",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("🌊 Tsunami Alert System")
st.sidebar.markdown("---")

# Navigation Options
page = st.sidebar.radio(
    "🔗 Navigate to",
    ["🏖️ Before Tsunami", "🌊 During Tsunami", "📝 After Tsunami", "🚁 Rescue Operations"]
)

# Before Tsunami Section
if page == "🏖️ Before Tsunami":
    st.title("🏖️ Before Tsunami: Early Warning System")
    st.write("""
    - Monitor earthquake activity to predict tsunami occurrence.
    - Detect ocean anomalies and wave height changes.
    - Predict potential tsunami zones and alert coastal regions.
    - Implement AI to detect early warning signs.
    """)

    st.info("✅ Stay Prepared: Evacuation plans should be ready for vulnerable zones.")
    
# During Tsunami Section
elif page == "🌊 During Tsunami":
    st.title("🌊 During Tsunami: Live Tracking System")
    st.write("""
    - Track real-time tsunami propagation and arrival time.
    - Monitor wave heights and changes using satellite data.
    - Alert emergency services and evacuation teams.
    """)

    st.warning("⚠️ Ongoing Tsunami Detected: Follow evacuation protocols immediately!")
    
# After Tsunami Section
elif page == "📝 After Tsunami":
    st.title("📝 After Tsunami: Impact & Damage Analysis")
    st.write("""
    - Assess the damage in affected regions.
    - Document infrastructure loss and casualties.
    - Analyze tsunami aftermath using satellite imagery.
    """)

    st.success("📝 Impact Analysis Ongoing: Submitting reports to disaster authorities.")
    
# Rescue Operations Section
elif page == "🚁 Rescue Operations":
    st.title("🚁 Rescue & Relief Operations")
    st.write("""
    - Dispatch rescue teams to affected areas.
    - Provide medical aid and essentials.
    - Coordinate relief supplies and shelter arrangements.
    """)

    st.info("🆘 Request Rescue Assistance if needed!")
