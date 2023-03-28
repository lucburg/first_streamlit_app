import streamlit
import snowflake.connector
from urllib.error import URLError

streamlit.title('Upload files')
try:
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_cur = my_cnx.cursor()
  my_cur.execute("put file://my_file.txt @my_internal_named_stage auto_compress=true parallel=X")
  my_cnx.close()
except URLError as e:
  streamlit.error()

