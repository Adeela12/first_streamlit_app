import streamlit
streamlit.title("My parents New Healty Diner")
streamlit.header("Breakfast Menu")
streamlit.text("🥣 Omega3 and blueberry oatmeal")
streamlit.text("🥗 Kale, spinach and Rocket smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
