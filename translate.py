import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy import *
from googletrans import Translator

def translate_video(video_path, lang_from, lang_to):
    translator = Translator()
    clip = VideoFileClip(video_path)
    translated_texts = []

    for txt in clip.iter_frames():
        result = translator.translate(txt, src=lang_from, dest=lang_to)
        translated_texts.append(result.text)

    translated_path = video_path.replace(".mp4", f"_{lang_to}.mp4")
    clip.write_videofile(translated_path)
    messagebox.showinfo("Success", f"Translated video saved as {translated_path}")

def browse_file():
    filename = filedialog.askopenfilename(title="Select a Video File", filetypes=[("Video files", "*.mp4")])
    video_path.set(filename)

app = tk.Tk()
app.title("Video Translator")

video_path = tk.StringVar()

tk.Label(app, text="Select a video file:").pack()
tk.Entry(app, textvariable=video_path).pack()
tk.Button(app, text="Browse", command=browse_file).pack()
tk.Button(app, text="Translate", command=lambda: translate_video(video_path.get(), 'en', 'es')).pack()

app.mainloop()
