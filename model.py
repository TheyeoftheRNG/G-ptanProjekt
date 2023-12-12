from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import joblib
import streamlit as st


st.title("DnD Race Predicter")

model_KNeighborsClassifier = joblib.load("model_KNeighborsClassifier.joblib")

height = st.slider("Height in cm", 70, 210)

weight = st.slider("Weight in kg", 15, 200)

speed = st.slider("speed in feet", 25,30, step=5)

strength = st.slider("strength", 1, 20)

dexterity = st.slider("dexterity", 1, 20)

constitution = st.slider("constitution", 1, 20)

intelligence = st.slider("intelligence", 1, 20)

wisdom = st.slider("wisdom", 1, 20)

charisma = st.slider("charisma", 1, 20)


strength_modifier = strength-10//2

dexterity_modifier = dexterity-10//2

constitution_modifier = constitution-10//2

intelligence_modifier = intelligence-10//2

wisdom_modifier = wisdom-10//2

charisma_modifier = charisma-10//2


height = height * 0.393700787
weight = weight * 2.20462262


height = height **11
weight = weight **4
speed=speed-27.5
speed = speed **2
strength = strength **4
dexterity = dexterity **4
constitution = constitution **4
intelligence = intelligence **4
wisdom = wisdom **4
charisma = charisma **4
strength_modifier = strength_modifier **7
dexterity_modifier = dexterity_modifier **7
constitution_modifier = constitution_modifier **7
intelligence_modifier = intelligence_modifier **7
wisdom_modifier = wisdom_modifier **7
charisma_modifier = charisma_modifier **7

data = [{'height': height, 'weight': weight, 'speed': speed, 'strength': strength,
       'dexterity': dexterity, 'constitution': constitution, 'intelligence': intelligence,
       'wisdom': wisdom, 'charisma': charisma, 'strength_modifier': strength_modifier, 'dexterity_modifier': dexterity_modifier,
       'constitution_modifier': constitution_modifier, 'intelligence_modifier': intelligence_modifier, 'wisdom_modifier': wisdom_modifier,
       'charisma_modifier': charisma_modifier}]


dff = pd.DataFrame(data)


number = model_KNeighborsClassifier.predict(dff)





if number == 0:
     st.markdown("<h3 style='text-align: center; height:0px; font-size: 20px;font-weight: normal; '>dragonborn</h3>", unsafe_allow_html=True)
elif number == 1:
    st.markdown("<h3 style='text-align: center; height:0px; font-size: 20px;font-weight: normal; '>dwarf</h3>", unsafe_allow_html=True)
elif number == 2:
    st.markdown("<h3 style='text-align: center; height:0px; font-size: 20px;font-weight: normal; '>elf</h3>", unsafe_allow_html=True)
elif number == 3:
    st.markdown("<h3 style='text-align: center; height:0px; font-size: 20px;font-weight: normal; '>gnome</h3>", unsafe_allow_html=True)
elif number == 4:
    st.markdown("<h3 style='text-align: center; height:0px; font-size: 20px;font-weight: normal; '>half elf</h3>", unsafe_allow_html=True)
elif number == 5:
    st.markdown("<h3 style='text-align: center; height:0px; font-size: 20px;font-weight: normal; '>half orc</h3>", unsafe_allow_html=True)
elif number == 6:
     st.markdown("<h3 style='text-align: center; height:0px; font-size: 20px;font-weight: normal; '>halfling</h3>", unsafe_allow_html=True)
elif number == 7:
     st.markdown("<h3 style='text-align: center; height:0px; font-size: 20px;font-weight: normal; '>human</h3>", unsafe_allow_html=True)
elif number == 8:
    st.markdown("<h3 style='text-align: center; height:0px; font-size: 20px;font-weight: normal; '>tiefling</h3>", unsafe_allow_html=True)
