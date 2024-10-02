# iOS App Icon Cropper

iOS App Icon Cropper is a Streamlit web application that allows users to easily crop and resize images for use as iOS app icons. It supports PNG, JPEG, and SVG file formats.

## Features

- Upload PNG, JPEG, or SVG images
- Automatic conversion of SVG to PNG
- Interactive zoom slider for precise cropping
- Preview of original and cropped images
- Automatic resizing to 1024x1024 pixels (iOS app icon standard)
- One-click download of the cropped and resized image

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ios-app-icon-cropper.git
   cd ios-app-icon-cropper
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run image_cropper.py
   ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Upload an image file (PNG, JPEG, or SVG) using the file uploader.

4. Adjust the zoom factor using the slider to crop the image as desired.

5. Preview the cropped and resized image.

6. Click the "Download Cropped Image" button to save the processed image.

## Dependencies

- Streamlit
- Pillow (PIL)
- CairoSVG

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.