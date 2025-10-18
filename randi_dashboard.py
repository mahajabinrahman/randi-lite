#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 23:31:00 2025

@author: mahajabin
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

# Load data
df = pd.read_csv('toy_models.csv')

# Calculate ethics score (arbitrary weights for now)

df['ethics_score'] = 1 - (0.5*df.bias_score + 0.5*df.energy_kwh/df.energy_kwh.max())

# Streamlit user interface
st.title('RANDI-lite: What does cleverness cost?')
st.write("A prototype tool for auditing AI models by planetary and ethical costs")

model = st.selectbox('Choose a model', df.model_name)
row = df[df.model_name == model].iloc[0]

st.subheader('Model Metrics')
st.write(f"Bias score: {row.bias_score}")
st.write(f"Energy cost (kWh): {row.energy_kwh:.2f}")
st.write(f"Ethics score: {row.ethics_score: .2f}")

# make plot
fig, ax = plt.subplots()
ax.bar(df.model_name, df.ethics_score, color = 'coral')
ax.set_ylabel("Ethics Score")
ax.set_xlabel("Model")
ax.set_ylim(0,1)
st.pyplot(fig)

