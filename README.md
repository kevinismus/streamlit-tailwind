# streamlit-tailwind

A streamlit component that allows the addition of custom HTML with Tailwind classes

## Installation instructions 

```sh
pip install streamlit-tailwind
```

## Usage instructions

```python
import streamlit as st

from streamlit_tailwind import st_tw

value = st_tw(
        text="""
            <div class="bg-white p-4 h-48 rounded-lg"></div>
        """,
        height=192 # 4 x specified height in tailwind
    )

    st.write(value)

st.write(value)
