import streamlit as st
import os
from PIL import Image
from yolov5_tflite_image_inference import detect_image
from utils import getprojdir


filenames = [os.path.normpath(getprojdir() + '/readme.md'), os.path.normpath(getprojdir() + '/README.md')]
for filename in filenames:
    if os.path.exists(filename):
        readme = filename

weights = os.path.normpath(getprojdir() + '/tests/yolov5s-fp16.tflite')
tempimg = os.path.normpath(getprojdir() + '/temp/temp.jpg')
detectedimg = os.path.normpath(getprojdir() + '/temp/tempyolov5_output.jpg')


def detect_userimage(usrimage):
    detect_image(
        weights,
        usrimage,
        416,
        0.25,
        0.45)

# streamlit encourages well-structured code, like starting execution in a main() function.


def main():
    # get readme file content
    with open(readme, "r") as file:
        rmcontent = file.read()

    st.set_page_config(layout="wide")

    # create two columns with a 1:1 ratio
    left_column, right_column = st.columns((1, 1))

    with left_column:
        # render the readme as markdown using st.markdown.
        readme_text = st.markdown(rmcontent)

    with right_column:
        st.title("Load your .jpg image for processing:")

        uploaded_file = st.file_uploader("Choose an image...", type="jpg")

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            image.save(tempimg)
            st.image(image, caption="Uploaded Image")

        if st.button("Image inference"):
            # Call the method when the button is clicked
            detect_userimage(tempimg)
            imagedet = Image.open(detectedimg)
            st.image(imagedet, caption="Yolov5 result")


if __name__ == "__main__":
    main()
