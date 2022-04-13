import os

def who(unknown_image="/home/pi/third-eye/temp/image.jpg", knwons_dir="/home/pi/third-eye/data/known"):
    name = os.popen(f"face_recognition {knwons_dir} {unknown_image} | cut -d ',' -f2").read()
    return name
