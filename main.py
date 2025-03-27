import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

# ---- Sidebar Dashboard ----
st.sidebar.title("🌊 Tsunami Alert System")
menu = st.sidebar.radio(
    "Navigate",
    ["Before Tsunami", "During Tsunami", "After Tsunami", "Rescue Operations"],
)

# ---- Dummy Sensor Data for Simulation ----
def simulate_earthquake_activity(steps=30):
    np.random.seed(42)
    seismic_activity = np.abs(np.sin(np.linspace(0, 3 * np.pi, steps)) * 5 + np.random.randn(steps))
    return seismic_activity

def detect_anomalies(seismic_activity):
    anomalies = []
    for activity in seismic_activity:
        if activity > 6:
            anomalies.append("⚠️ High Anomaly - Possible Tsunami!")
        elif activity > 3:
            anomalies.append("🟠 Moderate Anomaly - Monitor Closely")
        else:
            anomalies.append("✅ Normal - No Immediate Threat")
    return anomalies

# ---- DURING TSUNAMI: Real-Time Wave Propagation ----
def simulate_wave_data(steps=30):
    np.random.seed(42)
    wave_heights = np.abs(np.sin(np.linspace(0, 3 * np.pi, steps)) * 3 + np.random.randn(steps))
    return wave_heights

def predict_wave_propagation(wave_heights):
    risk_level = []
    for height in wave_heights:
        if height > 6:
            risk_level.append("⚠️ High Risk - Immediate Evacuation!")
        elif height > 3:
            risk_level.append("🟠 Moderate Risk - Stay Alert")
        else:
            risk_level.append("✅ Low Risk - No Immediate Danger")
    return risk_level

# ---- BEFORE TSUNAMI: AI Monitoring & Prediction ----
if menu == "Before Tsunami":
    st.title("🌊 AI-Powered Tsunami Prediction")
    st.write("Monitor earthquake activity, detect anomalies, and predict tsunami zones.")

    st.write("📡 **Simulating Seismic Activity Data...**")
    seismic_data = simulate_earthquake_activity(steps=30)
    anomaly_status = detect_anomalies(seismic_data)

    # Display Seismic Activity Graph
    st.write("🔍 **Tracking Seismic Activity and Anomalies...**")
    seismic_chart = st.line_chart([])

    for i, activity in enumerate(seismic_data):
        seismic_chart.line_chart(seismic_data[: i + 1])
        st.write(
            f"🌍 Seismic Activity: **{activity:.2f} units** | Status: {anomaly_status[i]}"
        )
        if anomaly_status[i] == "⚠️ High Anomaly - Possible Tsunami!":
            st.error("🚨 **ALERT: High Anomaly Detected! Possible Tsunami Risk!**")
        elif anomaly_status[i] == "🟠 Moderate Anomaly - Monitor Closely":
            st.warning("⚠️ **Caution: Moderate Anomaly. Monitor Closely!**")
        else:
            st.success("✅ **Normal Seismic Activity. No Immediate Threat.**")

        time.sleep(0.5)

    st.success("📡 **Monitoring Completed. Data Recorded.**")

# ---- DURING TSUNAMI: Real-Time Tracking ----
if menu == "During Tsunami":
    st.title("🌊 Real-Time Tsunami Monitoring")
    st.write("AI-powered real-time wave propagation tracking to minimize response time and ensure timely evacuation.")

    st.write("📡 **Simulating Real-Time Wave Data...**")
    wave_data = simulate_wave_data(steps=30)
    risk_status = predict_wave_propagation(wave_data)

    wave_chart = st.line_chart([])

    st.write("🔍 **Tracking Wave Heights & Risk Levels...**")
    for i, height in enumerate(wave_data):
        wave_chart.line_chart(wave_data[: i + 1])
        st.write(
            f"🌊 Wave Height: **{height:.2f} meters** | Risk Level: {risk_status[i]}"
        )
        if risk_status[i] == "⚠️ High Risk - Immediate Evacuation!":
            st.error("🚨 **ALERT: High Risk!**
