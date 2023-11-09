import os
import shutil
from tkinter import *

# (name of folder, associated extensions)
sorted_dirs_info = (("image", (".ai", ".gif", ".jpg", ".jpeg", ".bmp", ".svg", ".ico", ".png", ".svg", "webp")),
                    ("audio", (".mp3", ".flac", ".m4a", ".wav")),
                    ("video", (".mp4", ".avi", ".m4v", ".mkv", ".mov", ".h264")),
                    ("text", (".txt", ".doc", ".docx", ".pdf")))


# function for moving files
def move_files(src, dst, extensions):
    for file in os.listdir(src):
        src_path = src + "\\" + file
        dst_path = dst + "\\" + file
        if file.endswith(extensions):
            shutil.move(src_path, dst_path)


def sort_files():
    src_dir = input_src.get(1.0, "end-1c")
    dst_dir = input_dst.get(1.0, "end-1c")
    label_err.config(text="")
    label_success.config(text="")

    if not os.path.exists(src_dir):
        label_err.config(text="Source directory does not exist")
    elif not os.path.exists(dst_dir):
        label_err.config(text="Destination directory does not exist")
    else:
        # create separate directories for different file types inside destination directory
        for dir_info in sorted_dirs_info:
            path = dst_dir + "\\" + dir_info[0]
            if not os.path.exists(path):
                os.mkdir(path)
        try:
            for dir_info in sorted_dirs_info:
                move_files(src_dir, dst_dir + "\\" + dir_info[0], dir_info[1])
        except Exception:
            label_err.config(text="Unable to move files")
        else:
            label_success.config(text="Moved files successfully")


# UI -------------------------------------------
window = Tk()

window.title("File Sorter")
window.geometry("400x200")
font_style = ("Arial", 12)

label_src = Label(window, text="Source directory:",
                  font=font_style)
label_src.pack()
input_src = Text(window, height=1, font=font_style)
input_src.pack()

label_dst = Label(window, text="Destination directory:",
                  font=font_style)
label_dst.pack()
input_dst = Text(window, height=1, font=font_style)
input_dst.pack()

label_err = Label(window, text="",
                  font=font_style, fg="#ff0000")
label_err.pack()

btn_move = Button(window, text="Move files", font=font_style, command=sort_files)
btn_move.pack()

label_success = Label(window, text="", font=font_style)
label_success.pack()

window.mainloop()
