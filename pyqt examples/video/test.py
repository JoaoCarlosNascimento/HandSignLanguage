from moviepy.editor import VideoFileClip

videoClip = VideoFileClip("a.mp4")

videoClip.write_gif("a.gif", fps=15)
