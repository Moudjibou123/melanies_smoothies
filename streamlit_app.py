# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
import requests

# Write directly to the app
st.title("Customize your Smoothie :cup_with_straw:")
st.write("Choose the fruits you want in your Custom smoothie")

name_on_order = st.text_input('Name on smoothie :')
st.write("The name on your Smoothie wille be :", name_on_order)

cnx=st.connection("snowflake")
session =cnx.session()

#session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'),col('SEARCH_ON'))
#st.dataframe(data=my_dataframe, use_container_width=True)
#ingredients_list = st.multiselect ('Choose up to 5 ingredients : ', my_dataframe,max_selections=5)
pd_df=my_dataframe.to_pandas()
st.dataframe(pd_df)  
st.stop()


if ingredients_list :
    #st.write (ingredients_list)
    #st.text(ingredients_list)

    ingredients_string =''

    for fruit_chosen in ingredients_list:
        ingredients_string +=fruit_chosen
        st.subheader(fruit_chosen + ' Nutrition Information')
        st.write ("https://fruityvice.com/api/fruit/"+fruit_chosen)
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_chosen)
        fv_df = st.dataframe(data=fruityvice_response.json(), use_container_width=True)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','""" + name_on_order + """')"""

    #st.write(my_insert_stmt)

    time_to_order= st.button('Submit your Order')
    #if ingredients_string:
    if time_to_order:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")

