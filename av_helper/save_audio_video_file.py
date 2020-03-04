import os
import time
from moviepy.editor import VideoFileClip


def save_audio_video_file(video_clip: VideoFileClip, output_dir='final_output', filename=None):
    """
    Utility Function to Save an Audio-Video File
    :param video_clip: File-Name of Video Clip
    :param output_dir: Output directory in which Audio File to Add
    :param filename: Complete Path of File-Name to write to
    :return: Complete Path of File-Name written to
    """
    if not filename:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        time_string = time.strftime("%Y%m%d_%H%M%S") + '.mp4'
        write_file_path = os.path.join(output_dir, time_string)
    else:
        write_file_path = filename
    video_clip.write_videofile(write_file_path)
    return write_file_path
