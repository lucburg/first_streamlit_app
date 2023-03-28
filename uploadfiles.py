import streamlit
import snowflake.connector

streamlit.title('Upload files')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("put file://my_file.txt @myinternal_stage auto_compress=true parallel=X")
my_cnx.close()

