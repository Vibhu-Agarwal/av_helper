import cv2
from moviepy.editor import AudioFileClip, VideoFileClip, concatenate_videoclips


def starting_point_in_time(video_file_name: str, frame_number: int):
    """
    Get starting point in time from Frame Number in a Video File
    :param video_file_name: File-Name of Video
    :param frame_number: Frame Number (less than total number of frames of video)
    :return: Tuple of (Starting Time (in s) and Video's frame-per-second speed
    """
    video = cv2.VideoCapture(video_file_name)
    video_fps = video.get(cv2.CAP_PROP_FPS)
    start_time = frame_number / video_fps
    return start_time, video_fps


def merge_audio_video(audio_file: str, video_file: str, frame_number: int = 0, volume_factor=1):
    """
    Function to merge Audio File into Video File

    :param audio_file: File-Name of Audio
    :param video_file: File-Name of Video
    :param frame_number: Frame Number at which audio file to add in Video File
    :param volume_factor: Factor by which Volume of Audio has to be modified
    :return: Video Clip (with Audio merged) of type moviepy.video.VideoClip
    """
    audio_clip = AudioFileClip(audio_file)
    video_clip = VideoFileClip(video_file)

    start_time, video_fps = starting_point_in_time(video_file, frame_number)

    orig_video_duration = video_clip.duration
    orig_audio_duration = audio_clip.duration

    audio_clip = audio_clip.subclip(0, min(orig_video_duration - start_time, orig_audio_duration))
    audio_clip = audio_clip.volumex(volume_factor)

    first_part = video_clip.subclip(0, start_time)
    second_part = video_clip.subclip(start_time, orig_video_duration)

    second_part.audio = audio_clip

    final_video_clip = concatenate_videoclips([first_part, second_part])
    return final_video_clip


if __name__ == '__main__':
    output_video = merge_audio_video('audio_file_name.mp3', 'video_file_name.mp4')
