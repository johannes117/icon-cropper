import streamlit as st
from PIL import Image
import io

def main():
    st.title("iOS App Icon Cropper")

    uploaded_file = st.file_uploader("Upload your image (PNG or JPEG)", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        
        original_width, original_height = image.size

        st.write("Original Image:")
        st.image(image, caption="Original Image", use_column_width=True)

        zoom_factor = st.slider("Zoom", min_value=1.0, max_value=2.0, value=1.0, step=0.01)

        # Calculate the size of the square crop
        crop_size = int(min(original_width, original_height) / zoom_factor)
        left = (original_width - crop_size) // 2
        top = (original_height - crop_size) // 2
        right = left + crop_size
        bottom = top + crop_size

        cropped_image = image.crop((left, top, right, bottom))

        # Always resize to 1024x1024
        resized_image = cropped_image.resize((1024, 1024), Image.LANCZOS)

        st.write("Cropped and Resized Image Preview:")
        st.image(resized_image, caption="Cropped and Resized Image (1024x1024)", use_column_width=True)

        if st.button("Download Cropped Image"):
            buf = io.BytesIO()
            resized_image.save(buf, format="PNG")
            byte_im = buf.getvalue()
            st.download_button(
                label="Download Cropped Image",
                data=byte_im,
                file_name="cropped_icon_1024x1024.png",
                mime="image/png"
            )
    else:
        st.info("Please upload a PNG or JPEG image to get started.")

if __name__ == "__main__":
    main()