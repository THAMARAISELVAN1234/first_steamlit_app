import streamlit
streamlit.title('Hello Everyone')
streamlit.header('My profile')
streamlit.text('Myself Thamaraiselvan')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
