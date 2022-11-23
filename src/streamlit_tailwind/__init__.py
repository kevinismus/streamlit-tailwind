from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called streamlit_tailwind,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
	"st_tw", path=str(frontend_dir)
)

# Create the python function that will be called
def st_tw(
    text: str,
    height: Optional[int] = 100,
    key: Optional[str] = None,
):
    """
    Add a descriptive docstring
    """
    component_value = _component_func(
        text=text,
        height=height,
        key=key,
    )

    return component_value


def main():
    st.write("## Example")
    value = st_tw(
        text="""
            <div class="bg-white p-4 h-48 rounded-lg"></div>
        """,
        height=190 # 4 x specified height in tailwind
    )

    st.write(value)


if __name__ == "__main__":
    main()
