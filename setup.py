from setuptools import setup, find_packages
import codecs
import os

NAME = 'a7a'
EMAIL = 'aya_haga@a7a.com'
VERSION = '0.0.13'
DESCRIPTION = 'a pack that say a7a'

# Setting up
setup(
    name=NAME,
    version=VERSION,
    author="Ana",
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    #install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
