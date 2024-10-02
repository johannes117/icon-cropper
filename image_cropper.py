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

        # Add output size selection
        output_size = st.number_input("Output image size (width and height in pixels)", min_value=16, max_value=4096, value=1024, step=1)

        # Resize to the selected output size
        resized_image = cropped_image.resize((output_size, output_size), Image.LANCZOS)

        st.write(f"Cropped and Resized Image Preview ({output_size}x{output_size}):")
        st.image(resized_image, caption=f"Cropped and Resized Image ({output_size}x{output_size})", use_column_width=True)

        buf = io.BytesIO()
        resized_image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Cropped Image",
            data=byte_im,
            file_name=f"cropped_icon_{output_size}x{output_size}.png",
            mime="image/png"
        )
    else:
        st.info("Please upload a PNG or JPEG image to get started.")

if __name__ == "__main__":
    main()