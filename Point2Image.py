import numpy as np
import cv2
import os
from tqdm import tqdm  # progress bar

def world2image(x, y, z, image_width, image_height, vertical_fov):
    """
    Convert world coordinates to image coordinates using cylindrical projection.
    """
    theta = np.arctan2(y, x) / np.pi * 180.0 + 180.0
    phi = (np.arctan2(z, np.sqrt(x**2 + y**2)) * 180.0 / np.pi) + (vertical_fov / 2)

    u = int(image_width - (theta / 360.0) * image_width)
    v = int((1 - (phi / vertical_fov)) * image_height)
    
    return u, v

def process_point_cloud_file(file_path, output_folder, image_width, image_height, vertical_fov, max_dist=35.0):
    # Load point cloud from bin file
    point_cloud = np.fromfile(file_path, dtype=np.float32).reshape(-1, 4)

    # Create an empty image
    img = np.zeros((image_height, image_width, 3), dtype=np.uint8)

    # Add tqdm to display the progress bar
    for point in tqdm(point_cloud, desc=f'Processing {os.path.basename(file_path)}', unit='points'):
        x, y, z, _ = point
        u, v = world2image(x, y, z, image_width, image_height, vertical_fov)
        
        # Calculate the distance in x, y and z
        d = np.sqrt(x**2 + y**2 + z**2)
        
        # Normalize the distance
        normalized_dist = d / max_dist
        
        # Map distance to HSV color
        hue = int(120 * (1 - normalized_dist))  # Hue from green (0) to red (120)
        hue = np.clip(hue, 0, 120)  # Ensure hue is within the valid range
        color = cv2.cvtColor(np.uint8([[[hue, 255, 255]]]), cv2.COLOR_HSV2BGR)[0][0]
        
        # Check bounds and assign color
        if 0 <= u < image_width and 0 <= v < image_height:
            img[v, u] = color

    # Convert RGB image to BGR (for OpenCV)
    img_cv2 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Save the image
    base_name = os.path.basename(file_path).replace('.bin', '.png')
    output_path = os.path.join(output_folder, base_name)
    cv2.imwrite(output_path, img_cv2)

def process_point_cloud_folder(input_folder, output_folder):
    # Constants for the image based on Velodyne HDL-64E FOV
    horizontal_fov = 360.0
    vertical_fov = 26.8

    # Determine the image size
    image_width = 2084  # Based on the desired horizontal resolution
    image_height = int(image_width * (vertical_fov / horizontal_fov))  # Maintain aspect ratio based on FOV

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_list = [f for f in os.listdir(input_folder) if f.endswith('.bin')]
    
    for file_name in tqdm(file_list, desc='Processing files', unit='file'):
        file_path = os.path.join(input_folder, file_name)
        process_point_cloud_file(file_path, output_folder, image_width, image_height, vertical_fov)

# Example usage
path = '/home/sean/Documents/GitHub/KITTI-PCL2IMG'
input_folder = path + '/data'
output_folder = path + '/range_image'

process_point_cloud_folder(input_folder, output_folder)
