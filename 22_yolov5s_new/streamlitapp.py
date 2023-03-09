import streamlit as st
from utils import getprojdir
import pandas as pd
import numpy as np
import os, urllib, cv2

readme = os.path.normpath(getprojdir() + '/readme.md')

# Streamlit encourages well-structured code, like starting execution in a main() function.
def main():
    with open(readme, "r") as file:
        rmcontent = file.read()
    # Render the readme as markdown using st.markdown.
    readme_text = st.markdown(rmcontent)


if __name__ == "__main__":
    main()