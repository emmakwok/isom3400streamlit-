import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Retail Business Dashboard")
st.header("Manager Input Section")
st.write("Please enter the monthly sales target and select the region.")

option = st.selectbox("Enter Monthly Sales Target (in USD)",
                      ["Red", "Blue", "Green"])
st.write(f"You selected: {option}")

