import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Upload files')
try:
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_cur = my_cnx.cursor()
  my_cur.execute("put file://C:\\Users\\burguela\\my_file.txt @demo_db.public.my_internal_named_stage")
  my_cnx.close()
except URLError as e:
  streamlit.error()

