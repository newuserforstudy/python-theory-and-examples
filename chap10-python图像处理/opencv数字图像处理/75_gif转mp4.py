import moviepy.editor as mp
clip = mp.VideoFileClip("your_file.gif")
clip.write_videofile("your_file.mp4")
