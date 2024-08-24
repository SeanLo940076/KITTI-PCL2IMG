# KITTI-PCL2IMG

[中文版本](README_zh.md)

A Python tool for converting KITTI dataset point cloud data to 2D images using cylindrical projection, visualizing distance with HSV color mapping.

![Demo of Range Map Video](range_map_video.gif)

## Overview

This project aims to convert point cloud data from the KITTI dataset into 2D images using spherical coordinates projection. The process employs cylindrical projection to transform the point cloud data into a 2D image while visualizing the distance between the points and the LiDAR sensor using HSV color space.

## Features

- **Point Cloud Conversion**: Converts `.bin` format point cloud data into 2D images.
- **Distance Visualization**: Maps distances to colors ranging from HSV color space.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- tqdm

## Usage

### 1. Set Folder Paths

Modify the `input_folder` and `output_folder` variables to set the paths for the point cloud data and the output images.

### 2. Run the Script

Execute the following commands to process all point cloud files in the folder and generate the corresponding 2D images:

```bash
python Point2Image.py
python Image2Video.py
```

### 3. Results
The generated images will be saved in the specified output folder in `.png` format.

### Parameter Settings
- **`image_width` and `image_height`**: Set the width and height of the image, based on the FOV of the Velodyne HDL-64E.
- **`vertical_fov`**: Set the vertical field of view angle, with a default value of 26.8 degrees.
### Notes
- Ensure that the input folder contains `.bin` format point cloud files.
- Adjust the `max_dist` parameter as needed to control distance normalization.