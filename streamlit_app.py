# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Customize your Smoothie :cup_with_straw:")
st.write("Choose the fruits you want in your Custom smoothie")

name_on_order = st.text_input('Name on smoothie :')
st.write("The name on your Smoothie wille be :", name_on_order)

cnx=st.connection("snowflakeconn",type="snowflake")
