
import os
file_path=os.path.join('data','s1','bbaf2n.mpg')
# print(file_path)
print(file_path)
import subprocess
# C:\DATA\lipapp\data\s1
# os.system('C:/ffmpeg/ffmpeg -i {file_path} -vcodec libx264 test_video.mp4 -y')
command = f'C:/ffmpeg/ffmpeg -i "{file_path}" -vcodec libx264 test_video.mp4 -y'
print(command)




try:
    subprocess.run(command,check=True)
    print("conversion Successfull")

except subprocess.CalledProcessError as e:
    print(e, "error ffmpeg")