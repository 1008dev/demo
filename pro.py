import streamlit as st
import numpy as np
from PIL import Image

x=np.arange(-10,10)
st.title("graph of the equation")
s=st.slider(label="eq",min_value=1,max_value=10)
p=st.slider(label="pw",min_value=1,max_value=10)
inp=st.number_input("enter the equation")
if(st.button("plot")):
    st.text(s*x**p)
    st.line_chart(s*x**p)
    