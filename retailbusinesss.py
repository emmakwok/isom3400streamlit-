import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Retail Business Dashboard")
st.header("Manager Input Section")
st.write("Please enter the monthly sales target and select the region.")

age = st.number_input("Enter Monthly Sales Target (in USD):",
                      min_value=0,
                      max_value=10000000,
                      value=25)
st.write(f"Your age is {age}")

option = st.selectbox("Select Region:",
                      ["North", "East", "South", "West"])
st.write(f"You selected: {option}")

