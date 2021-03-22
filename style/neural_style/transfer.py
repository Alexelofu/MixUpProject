import streamlit as st
from PIL import Image
import style


rad =st.sidebar.radio("Navigation",["Home","About Us", "Stylize"])

if rad == "Home":
    st.title('Home')
    st.write(" ")
    st.write("Ever wanted to paint like your favorite artist or simply have a beautiful art work of you without paying through you nose? Well this is possible by using Neural Style Transfer.")
    st.write("## Neural Style Transfer")
    st.write("Neural-Style, or Neural-Transfer, allows you to take an image and reproduce it with a new artistic style. The algorithm takes three images, an input image, a content-image, and a style-image, and changes the input to resemble the content of the content-image and the artistic style of the style-image.")
    imgs = Image.open("neural art.png")
    st.image(imgs, width=500)
    st.write("Style transfer is a fun and interesting technique that showcases the capabilities and internal representations of neural networks.")
    st.write("In summary, we’ll take the base input image, a content image that we want to match, and the style image that we want to match. We’ll transform the base input image by minimizing the content and style distances (losses) with backpropagation, creating an image that matches the content of the content image and the style of the style image.")

if rad == "About Us":
    st.title('About Us')
    st.write(" ")
    st.write(" My name is Ofuonyeadi Alexander, a graduate of Chemistry and a Data Science enthusiast. I like analysing data to find insighs to will aid with decision making. I also like building machine learning models especially for prediction in the financial sector.")
    st.write(" This project is my capstone project for my graduate accceleration programme at STUTERN limited. The projects explores Deep learning models for applying artistic style transfers from art to pictures, thus creating wonderful looking pictures. ")
    st.write('The project is also dear to me as I am avid art lover myself.')


if rad == "Stylize":
        st.title('Stylize')
        st.write('Content images and style images can be picked from the navigation bar. Content image is shown above and output or styled image will appear below after picking style and clicking the stylize button. Run time can differ depending on your systems processing speed.')
        img = st.sidebar.selectbox(
        'select image',
        ('amber.jpg', 'lion.jpg', 'portrait.jpg')
        )

       
        style_name = st.sidebar.selectbox(
            'select style',
            ('candy', 'mosaic', 'udnie', 'rain_princess')
        )


        model = "saved_models/" + style_name + ".pth"
        input_image = "images/content-images/" + img
        output_image = "images/output-images" + style_name + "-" + img


        st.write("### Content Image:")
        image = Image.open(input_image)
        st.image(image, width=200)

        clicked = st.button("Stylize")

        if clicked:
            model = style.load_model(model)
            style.stylize(model, input_image, output_image)

            st.write("### Output Image:")
            image = Image.open(output_image)
            st.image(image, width=200)
