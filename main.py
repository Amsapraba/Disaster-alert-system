import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import random

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

# ---------- BEFORE TSUNAMI SECTION ----------
if page == "🏖️ Before Tsunami":
    st.title("🏖️ Before Tsunami: AI-Powered Early Warning System")
    st.write("""
    - Monitor earthquake activity to predict tsunami occurrence.
    - Detect ocean anomalies and wave height changes.
    - Predict potential tsunami zones and alert coastal regions.
    - Implement AI to detect early warning signs.
    """)
    
    st.markdown("---")

    # 🌊 1. Monitor Earthquake Activity
    st.subheader("🌏 Earthquake Monitoring")
    depth = st.slider("📏 Earthquake Depth (km)", 1, 700, 10)
    magnitude = st.slider("💥 Earthquake Magnitude", 4.0, 10.0, 6.5)
    distance_to_shore = st.number_input("🌊 Distance to Shore (km)", 1, 1000, 50)

    st.markdown("---")

    # 🌊 2. Detect Ocean Anomalies
    st.subheader("🌊 Ocean Anomaly Detection")
    wave_height = st.slider("🌊 Ocean Wave Height (m)", 0.1, 10.0, 1.5)
    pressure_change = st.slider("🔎 Seafloor Pressure Change (%)", 0, 100, 20)

    st.markdown("---")

    # 🌊 3. AI-Powered Tsunami Prediction
    st.subheader("🤖 AI Prediction: Tsunami Risk Assessment")

    # Advanced AI Prediction Formula
    risk_score = (magnitude ** 2 * wave_height * pressure_change) / (depth + distance_to_shore)

    def tsunami_alert(risk_score):
        """Classify Tsunami Risk Level Based on AI Score"""
        if risk_score > 150:
            return "⚠️ HIGH RISK - Immediate Action Required!", "danger"
        elif risk_score > 75:
            return "🟠 MODERATE RISK - Stay Alert!", "warning"
        else:
            return "✅ LOW RISK - No Immediate Danger", "success"

    alert_message, alert_status = tsunami_alert(risk_score)

    # Display Prediction Results
    if st.button("🔎 Predict Tsunami Risk"):
        if alert_status == "danger":
            st.error(f"{alert_message} | Risk Score: **{risk_score:.2f}**")
        elif alert_status == "warning":
            st.warning(f"{alert_message} | Risk Score: **{risk_score:.2f}**")
        else:
            st.success(f"{alert_message} | Risk Score: **{risk_score:.2f}**")

    st.markdown("---")

    # 🌊 4. Predict Potential Tsunami Zones & Impact
    st.subheader("🌍 Potential Tsunami Impact Zones")

    # Simulated Zone Risk Data
    zone_data = pd.DataFrame({
        "Region": ["Indian Ocean", "Bay of Bengal", "Pacific Ocean", "Arabian Sea", "Andaman Sea"],
        "Risk Level": [
            risk_score * 1.5 + random.uniform(0, 20),
            risk_score * 1.2 + random.uniform(0, 15),
            risk_score * 0.9 + random.uniform(0, 10),
            risk_score * 0.7 + random.uniform(0, 5),
            risk_score * 1.1 + random.uniform(0, 12)
        ]
    })

    # Plotly Bar Chart for Zone Risk
    fig = px.bar(zone_data, x="Region", y="Risk Level", color="Risk Level",
                 title="🌊 Predicted Tsunami Risk in Key Zones",
                 labels={"Risk Level": "Tsunami Risk Score"},
                 height=400)

    st.plotly_chart(fig)

    st.info("✅ High-risk zones should prepare for evacuation and safety protocols.")

    st.markdown("---")

    # 🌊 5. Visualizing Tsunami Wave Propagation (Simulated)
    st.subheader("🌊 Simulated Tsunami Wave Propagation")

    # Generate random wave heights for visualization
    time_steps = np.arange(0, 60, 5)
    wave_heights = [wave_height + np.random.uniform(-0.5, 0.5) for _ in range(len(time_steps))]

    wave_data = pd.DataFrame({"Time (mins)": time_steps, "Wave Height (m)": wave_heights})

    fig_wave = px.line(wave_data, x="Time (mins)", y="Wave Height (m)",
                       title="🌊 Simulated Tsunami Wave Progression",
                       labels={"Wave Height (m)": "Wave Height Over Time"},
                       height=400)

    st.plotly_chart(fig_wave)

    st.success("✅ Simulation complete! Tsunami progression tracked successfully.")

# ---------- DURING TSUNAMI SECTION ----------
elif page == "🌊 During Tsunami":
    st.title("🌊 During Tsunami: Live Tracking System")
    st.write("""
    - Track real-time tsunami propagation and arrival time.
    - Monitor wave heights and changes using satellite data.
    - Alert emergency services and evacuation teams.
    """)

    st.warning("⚠️ Ongoing Tsunami Detected: Follow evacuation protocols immediately!")
    
# ---------- AFTER TSUNAMI SECTION ----------
elif page == "📝 After Tsunami":
    st.title("📝 After Tsunami: Impact & Damage Analysis")
    st.write("""
    - Assess the damage in affected regions.
    - Document infrastructure loss and casualties.
    - Analyze tsunami aftermath using satellite imagery.
    """)

    st.success("📝 Impact Analysis Ongoing: Submitting reports to disaster authorities.")
    
# ---------- RESCUE OPERATIONS SECTION ----------
elif page == "🚁 Rescue Operations":
    st.title("🚁 Rescue & Relief Operations")
    st.write("""
    - Dispatch rescue teams to affected areas.
    - Provide medical aid and essentials.
    - Coordinate relief supplies and shelter arrangements.
    """)

    st.info("🆘 Request Rescue Assistance if needed!")
