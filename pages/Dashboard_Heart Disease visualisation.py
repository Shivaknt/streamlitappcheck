import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "heart.jpg")
IMAGE_PATH2= os.path.join(dir_of_interest, "images", "heart2.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "heart.csv")

st.title("Dashboard - Heart Disease Data Visiualisation")

img = image.imread(IMAGE_PATH)
img2 = image.imread(IMAGE_PATH2)
st.image(img)
st.image(img2)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)


