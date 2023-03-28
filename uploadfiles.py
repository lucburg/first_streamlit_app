import streamlit
import snowflake.connector

streamlit.title('Upload files')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
query2 = "put file://my_file.txt @myinternal_stage auto_compress=true parallel=X"
execute_query(my_conn, query2)
