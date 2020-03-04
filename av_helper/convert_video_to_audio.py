import os
from moviepy.editor import VideoFileClip


def convert_video_to_audio(video_file: str, start_time: int = 0, video_duration=None):
    """
    Convert A Video File to mp3 format
    :param video_file: File Name of Video
    :param start_time: Starting Time (in s) at which clipping has to do
    :param video_duration: Duration wanted for audio clip
    :return: File-Name of Audio File created
    """
    clip = VideoFileClip(video_file)
    if not video_duration:
        video_duration = clip.duration
    clip = clip.subclip(start_time, start_time + video_duration)
    pre, ext = os.path.splitext(video_file)
    audio_file = pre + '.mp3'
    clip.audio.write_audiofile(audio_file)
    return audio_file


if __name__ == '__main__':
    audio_file_name = convert_video_to_audio('audio_file_in_video_format.mp4')
