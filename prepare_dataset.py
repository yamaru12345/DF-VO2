import os
import shutil

shutil.copy('./dataset/sequences/10/calib.txt', './dataset/odom_data/10/')
for i in range(30):
    shutil.move(f'./dataset/odom_data/10/frames/frame_{i:06d}.png', f'./dataset/odom_data/10/{i:06d}.png')