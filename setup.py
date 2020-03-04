import setuptools
import av_helper

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.readlines()

setuptools.setup(
    name=av_helper.__name__,
    version=av_helper.__version__,
    author=av_helper.__author__,
    author_email="vibhu4agarwal@gmail.com",
    description="An Audio-Video Helper Utility Package in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vibhu-Agarwal/av_helper",
    packages=setuptools.find_packages(),
    license='GPLv3+',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    keywords='audio video av moviepy',
    install_requires=requirements
)
