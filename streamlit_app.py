import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title("My parents New Healty Diner")
streamlit.header("Breakfast Menu")
streamlit.text("🥣 Omega3 and blueberry oatmeal")
streamlit.text("🥗 Kale, spinach and Rocket smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:" ,list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input(' What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    
except URLError as e:
  streamlit.error()

streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
  with my_cur as my_cnx:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
if streamlit.button('Get fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

streamlit.stop()


#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
  with my_cur as my_cnx:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
if streamlit.button('Get fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
def insert_row_snowflake():
  with my_cur as my_cnx:
    my_cur.execute("insert into fruit_load_list values('from streamlit')")
    return "Thanks for adding ", new_fruit
  
add_my_fruit = streamlit.text_input(' What fruit would you like information about?' , 'jackfruit')
if streamlit.button('Add a fruit to the list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)
