import cv2
import os
from tqdm import tqdm

# Define the base path (modify this to your own path)
path = '/home/sean/Documents/GitHub/KITTI-PCL2IMG'

# Read any saved image (make sure the path is correct)
img = cv2.imread(path + '/range_map_/0000000000.png')
fps = 10  # Set the FPS for the video
size = (img.shape[1], img.shape[0])  # Get the image size information
print(size)
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # Video encoding format

# Create a VideoWriter object based on the image size (file name, encoder format, frame rate, image size)
videoWrite = cv2.VideoWriter(path + '/range_map_video.avi', fourcc, fps, size)

# Get the list of image files
files = os.listdir(path + '/range_map_')
out_num = len(files)

for i in tqdm(range(out_num)):
    # Use the path variable to construct the file name
    fileName = f'{path}/range_map_/{i:010d}.png'  # Loop through all images, named numerically
    img = cv2.imread(fileName)
    if img is None:
        continue
    videoWrite.write(img)  # Write the image into the video frame

videoWrite.release()  # Release the video writer; this is crucial when writing multiple videos sequentially
