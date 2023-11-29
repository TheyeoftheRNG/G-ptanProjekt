from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import joblib
import streamlit as st


st.title("DnD Race Predicter")

model_KNeighborsClassifier = joblib.load("model_KNeighborsClassifier.joblib")

height = st.slider("height", 1, 100)

weight = st.slider("weight", 1, 350)

speed = st.slider("speed", 20,50, step=5)

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


height = height **4
weight = weight **4
speed = speed **4
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
     st.write("dragonborn")
elif number == 1:
    st.write("dwarf")
elif number == 2:
    st.write("elf")
elif number == 3:
    st.write("gnome")
elif number == 4:
    st.write("half.elf")
elif number == 5:
    st.write("half.orc")
elif number == 6:
     st.write("halfling")
elif number == 7:
     st.write("human")
elif number == 8:
    st.write("tiefling")