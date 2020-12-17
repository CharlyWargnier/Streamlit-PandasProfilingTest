import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import io


import requests
import base64
import time
import os

def _max_width_():
    max_width_str = f"max-width: 1600px;"
    #max_width_str = f"max-width: 1550px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

_max_width_()

c30, c31, c32 = st.beta_columns(3)

with c30:
    #st.image('logo.jpg', width = 275)
    st.header('')

with c32:
  st.header('')
  st.header('')
  st.markdown('###### Original script by ___ - Ported to [![this is an image link](https://i.imgur.com/iIOA6kU.png)](https://www.streamlit.io/)&nbsp, with :heart: by [@DataChaz](https://twitter.com/DataChaz) &nbsp [![this is an image link](https://i.imgur.com/thJhzOO.png)](https://www.buymeacoffee.com/cwar05)')


with st.beta_expander("ℹ️ - About this app ", expanded=True):

  st.write("""  
    
-   This data app uses _________________ to ___________________________.
-   Remove spinners - cache function i.e. Running recurse_entities
-   This app is free. If it's useful to you, you can [buy me a coffee](https://www.buymeacoffee.com/cwar05) to support my work! 🙏

	    """)

with st.beta_expander("ℹ️ - To-do's ", expanded=True):

  st.write("""  

-   Add IndexError: list index out of range
-   Add advanced parameter - explorative=True"
-   Add encoding parameter? try with tommyh files to check read/import issue"

	    """)


with st.beta_expander("ℹ️ - Fixed ", expanded=True):

  st.write("""  
-   ___________________ 
	    """)

#df = pd.DataFrame(
#    np.random.rand(100, 5),
#    columns=['a', 'b', 'c', 'd', 'e']
#)
#

st.title("Pandas Profiling in Streamlit")
#st.write(df)

#st.write("Multi-file uploader from ashikMultifile.py")

c1, c2, c3 = st.beta_columns([10,0.2,10])

with c1:
    multiple_files = st.file_uploader(
        "Multiple File Uploader",
        accept_multiple_files=True
    )


with c3:
    st.text('')
    for file in multiple_files:
        file_container = st.beta_expander(
            f"File name: {file.name} ({file.size})"
        )
        data = io.BytesIO(file.getbuffer())
        file_container.write(pd.read_csv(data))
        #file_container.write(pd.read_csv(data, error_bad_lines=False))
        file.seek(0)

dfs = [pd.read_csv(file) for file in multiple_files]
#dfs = [pd.read_csv(data, header=None, delim_whitespace=True) for file in multiple_files]
dfs
list1 = type(dfs)
list1

firstinList = dfs[0]
#secondinList = dfs[1]

firstinList2 = type(firstinList)
firstinList2

option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

options = {
    "1st table": "1st table",
    "id2": "2nd table",
    "id3": "3rd table",
}

option = st.selectbox("selectbox 2", list(options.items()), 0 , format_func=lambda o: o[1])

option[0]

#st.stop()

#pr = ProfileReport(secondinList, explorative=True)
pr = ProfileReport(dfs[0])
pr = ProfileReport(dfs[0], explorative=True)
st_profile_report(pr)

#pr = ProfileReport(firstinList, explorative=True)
#st_profile_report(pr)
