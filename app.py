import streamlit as st 
import pandas as pd
import numpy as np
""" # My first app Here's our first attempt at using
data to create a table: 
"""
"""
df = pd.DataFrame({ 'first column': [1, 2, 3, 4],
'second column': [10, 20, 30, 40] })
df
"""
"""
st.write("Here's our first attempt at usingdata to create a table:")
st.write(pd.DataFrame({ 'first column': [1, 2,
3, 4], 'second column': [10, 20, 30, 40] }))
"""
"""
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)
"""
'''
dataframe = pd.DataFrame( np.random.randn(10, 20),
columns=('col %d' % i for i in range(20)))
st.dataframe(dataframe.style.highlight_max(axis=0))
'''
'''
map_data = pd.DataFrame( np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon']) 
st.map(map_data)
'''
add_slider = st.sidebar.slider( 'Select a range of values', 0.0,100.0, (25.0, 75.0) )
add_selectbox = st.sidebar.selectbox( 'How would you like to becontacted?', ('Email', 'Home phone', 'Mobile phone') )


