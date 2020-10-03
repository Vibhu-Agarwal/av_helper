# av_helper
![Publish Python Package](https://github.com/Vibhu-Agarwal/av_helper/workflows/Publish%20Python%20Package/badge.svg)
[![DeepSource](https://deepsource.io/gh/Vibhu-Agarwal/av_helper.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/Vibhu-Agarwal/av_helper/?ref=repository-badge)  
An Audio-Video Helper Utility Package in Python

## Installation
```
$ pip3 install av-helper
```
[Visit](https://pypi.org/project/av-helper/) the PyPI page of the package.

## Usage

```python
>>> from av_helper import convert_video_to_audio
>>> audio_file_name = convert_video_to_audio('audio_file_in_video_format.mp4')

>>> from av_helper import merge_audio_video as merge_av
>>> output_video = merge_av(audio_file_name, 'video_file_name.mp4')

>>> from av_helper import save_audio_video_file as save_av
>>> save_av(output_video)
```

## Instant Docs

```python
>>> pprint(convert_video_to_audio.__doc__)
('\n'
 '    Convert A Video File to mp3 format\n'
 '    :param video_file: File Name of Video\n'
 '    :param start_time: Starting Time (in s) at which clipping has to do\n'
 '    :param video_duration: Duration wanted for audio clip\n'
 '    :return: File-Name of Audio File created\n'
 '    ')
```

```python
>>> pprint(merge_av.__doc__)
('\n'
 '    Function to merge Audio File into Video File\n'
 '    :param audio_file: File-Name of Audio\n'
 '    :param video_file: File-Name of Video\n'
 '    :param frame_number: Frame Number at which audio file to add in Video File\n'
 '    :param volume_factor: Factor by which Volume of Audio has to be modified\n'
 '    :return: Video Clip (with Audio merged) of type moviepy.video.VideoClip\n'
 '    ')

```
