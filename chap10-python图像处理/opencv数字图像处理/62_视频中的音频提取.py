"""
应用：
    1 opencv处理视频帧后写入视频文件(此视频文件不含音频，即无声视频)
    2 提取原视频文件中的音频文件
    3 将无声视频文件与音频文件合成新的视频文件(处理后的有声文件)

"""

# 1 无声视频提取见 61

from moviepy.editor import *


def extract_audio(videos_file_path):
    my_clip = VideoFileClip(videos_file_path)
    my_clip.audio.write_audiofile(f'{videos_file_path}.mp3')


def synthesis_video():

    # 音频和无声视频文件
    ad = AudioFileClip(f'video/test.mp4.mp3')
    vd = VideoFileClip(f'video/re.mp4')

    vd2 = vd.set_audio(ad)  # 将提取到的音频和视频文件进行合成
    vd2.write_videofile(f'video/xxx.mp4')  # 输出新的视频文件


if __name__ == '__main__':
    extract_audio(r'video/test.mp4')
    synthesis_video()