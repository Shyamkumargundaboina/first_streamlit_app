import streamlit
streamlit.title('My Parents Healthy Dinner')



streamlit.header('Breakfast Menu')
streamlit.text ('Omega 3 & blueberry oatmeal')
streamlit.text('Kale,Spinach & Rocket Smoothie')
streamlit.text('Hard Boiled Free -Range Eggs')

streamlit.header('Build your own fruit smoothie')



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
