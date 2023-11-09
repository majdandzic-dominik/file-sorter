import os
import shutil

# (name of folder, associated extensions)
sorted_dirs_info = (("image", (".ai", ".gif", ".jpg", ".jpeg", ".bmp", ".svg", ".ico", ".png", ".svg", "webp")),
                    ("audio", (".mp3", ".flac", ".m4a", ".wav")),
                    ("video", (".mp4", ".avi", ".m4v", ".mkv", ".mov", ".h264")),
                    ("text", (".txt", ".doc", ".docx", ".pdf")))

src_dir = ""
dst_dir = ""

while not os.path.exists(src_dir):
    src_dir = input("Enter source directory: ")

while not os.path.exists(dst_dir):
    dst_dir = input("Enter destination directory: ")


if not os.path.exists(dst_dir):
    os.mkdir(dst_dir)

for dir_name in sorted_dirs_info:
    path = dst_dir + "\\" + dir_name[0]
    if not os.path.exists(path):
        os.mkdir(path)


# function for moving files
def move_files(src, dst, extensions):
    for file in os.listdir(src):
        src_path = src + "\\" + file
        dst_path = dst + "\\" + file
        if file.endswith(extensions):
            shutil.move(src_path, dst_path)


try:
    for dir_info in sorted_dirs_info:
        move_files(src_dir, dst_dir + "\\" + dir_info[0], dir_info[1])
except Exception:
    print("Unable to move files")
else:
    print("Files move successfully")
