# moviepy Library - pip install moviepy
import moviepy.editor

cvt_video = moviepy.editor.VideoFileClip("D:\Django_project\PYTHON_P\ExtractAu.toVi\Aao Raja _ Yo Yo Honey Singh _ Chitrangada Singh _ Neha Kakkar _ Gabbar is Back(1080P_HD).mp4")

ext_audio = cvt_video.audio

ext_audio.write_audiofile("audio_Extracted.mp3")
