# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('Downloads/House_price.sav', 'rb'))

st.title("Boston Housing Price Predictor (1970s data ⚠️)")

col1, col2 = st.columns(2)

with col1:
    crim    = st.number_input("CRIM - Crime rate per capita", 0.0, 100.0, 3.6)
    zn      = st.number_input("ZN - % residential land >25k sq.ft lots", 0.0, 100.0, 11.0)
    indus   = st.number_input("INDUS - % non-retail business acres", 0.0, 30.0, 11.0)
    chas    = st.selectbox("CHAS - Bounds Charles River?", [0, 1])
    nox     = st.number_input("NOX - Nitric oxide conc. (ppm/10)", 0.3, 1.0, 0.55)
    rm      = st.number_input("RM - Avg rooms per house", 3.0, 9.0, 6.5)

with col2:
    age     = st.number_input("AGE - % houses built before 1940", 0.0, 100.0, 68.0)
    dis     = st.number_input("DIS - Dist. to employment centers", 0.0, 13.0, 3.8)
    rad     = st.number_input("RAD - Highway access index", 1, 24, 5)
    tax     = st.number_input("TAX - Property tax per $10k", 180, 720, 400)
    ptratio = st.number_input("PTRATIO - Pupil-teacher ratio", 12.0, 23.0, 18.5)
    b       = st.number_input("B - Racial composition index", 0.0, 400.0, 350.0)
    lstat   = st.number_input("LSTAT - % lower status population", 0.0, 40.0, 12.0)

if st.button("Predict House Price"):
    features = np.array([[crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]])
    
    pred = model.predict(features)[0]
    
    st.success(f"Estimated median house value: **${pred*1000:,.0f}** (in ~1970 dollars)")
    st.info("Note: This is historical Boston data — not current prices!")

