# Computer Vision Basics with OpenCV and Python

![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)
![OpenCV Version](https://img.shields.io/badge/OpenCV-4.10.0.84-brightgreen)
![PyCharm](https://img.shields.io/badge/PyCharm-Community%20Edition-purple)

Created for educational purposes, this repository contains a basic Computer Vision project developed in Python using the OpenCV library. The goal of this project is to introduce fundamental Computer Vision concepts, such as morphology, adding shapes and text to images or videos, using the smartphone camera, opening images, videos, and the webcam. Development was carried out using PyCharm Community Edition and the `opencv-python` package version `4.10.0.84`.

// ## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Using the Smartphone Camera](#using-the-smartphone-camera)
- [Usage](#usage)
- [Contributing](#contributing)

## Overview

This project covers basic Computer Vision concepts using Python and OpenCV. The main functionalities addressed include:

- **Morphology**: Application of morphological operations such as dilation, erosion, and opening on images.
- **Adding Shapes and Text**: How to draw geometric shapes and add text to images and videos.
- **Using the Smartphone Camera**: How to open and manipulate the smartphone camera settings with OpenCV.
- **Opening Images and Videos**: How to open and manipulate image and video files.
- **Using the Webcam**: How to open and manipulate webcam settings.

## Installation

### Prerequisites

- **Python 3.11+**
- **pip**
- **PyCharm Community Edition**
- **opencv-python version 4.10.0.84**

### Installation Steps

1. **Install PyCharm Community Edition** <br/>
   I used this IDE for its convenience in installing packages and using the language.

   - Download and install PyCharm Community Edition from the [official website](https://www.jetbrains.com/pycharm/download/).

2. **Clone this repository**
   - Open PyCharm
   - Follow these steps: <br/>
   File > Project from Version Control... > Repository URL <br/>
   **URL:** https://github.com/amandabarboza/computer-vision-python.git

3. **Install OpenCV Package** <br/>
   File > Settings > Project: computer-v... > Python Interpreter <br/>
    '+' (button) > write opencv-python > install package > close
## Using the Smartphone Camera

To use your smartphone camera with this project, you'll need to download and install the IP Webcam app. Follow the steps below to install and set up the app:

### Steps to Install IP Webcam

1. **Download and Install IP Webcam on Your Smartphone**

   - Go to the [Google Play Store](https://play.google.com/store/apps/details?id=com.pas.webcam) on your Android smartphone.
   - Search for "IP Webcam".
   - Tap "Install" and wait for the installation to complete.

2. **Configure IP Webcam**

   - Open the IP Webcam app on your smartphone.
   - Go to "Settings" to adjust options as needed (resolution, video quality, etc.).
   - Tap "Start server" to begin streaming from your camera.

3. **Connect to the Smartphone Camera**

   - After starting the server in IP Webcam, you'll see a URL displayed on your smartphone.
   - On your computer, use this URL to access the camera stream.

### Running the Mobile Camera Script

To capture video from your smartphone camera using the IP Webcam app, follow these steps:

1. **Replace `{your-ip}` in the `openingCellphoneCamera.py` script with the URL displayed by the IP Webcam app.**

2. **Run the `openingCellphoneCamera.py`**



## Usage

Choose the file you want to run and click on "Run 'file'".

## Contributing

Contributions are welcome! If you wish to contribute to the project, please follow these steps:

1. Fork this repository
2. Clone your Fork
3. Create a Branch for your Feature
4. Commit your changes
5. Push the changes to your Fork
6. Open a Pull Request

<br/>

Developed by
Amanda Barboza - amandabarboza.dev@gmail.com
<!-- [LinkedIn](https://www.linkedin.com/in/amanda-barboza-dev/) -->
