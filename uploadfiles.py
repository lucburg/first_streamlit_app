import streamlit
import snowflake.connector

streamlit.title('Upload files')

query2 = "put file://my_file.txt @myinternal_stage auto_compress=true parallel=X"
execute_query(conn, query2)
