# ai-face-detector

This project demonstrates the use of OpenCV (Open Source Computer Vision Library) to detect and draw rectangles around faces and eyes in an image. The project uses pre-trained classifiers for face and eye detection.

## Prerequisites
- Python
- OpenCV library (install with `pip install opencv-python`)

## Usage
1. Make sure you have the necessary classifiers. Download the following XML files and save them in the same directory as your script:
   - [haarcascade_eye.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml)
   - [haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)

2. Replace `'SET_IMAGE'` in the code with the path to the image you want to process.

3. Run the script.