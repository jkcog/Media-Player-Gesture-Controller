# Media Player Gesture Control
Gesture controller for media player with [MediaPipe](https://mediapipe.dev/), [VLC](https://wiki.videolan.org/Python_bindings/) and [OpenCV](https://opencv.org/).

<br />

# Contents
* [About](#about)
* [Setup](#setup)
* [Usage](#usage)
* [Gesture Guide](#gesture-guide)

<br />

* * *

# About

<br />

A tool for using gestures to control the video playback in VLC media player.

<br />
<img src="/media/demo.gif" alt="controller demonstration">

<br />

# Setup
* Ensure that you have VLC installed on your computer
* `$ pip install -r requirements.txt`
* Run main.py


<br />

# Usage
* Click "Browse" to select a mp4 video and launch the controller
* Type "Q" to quit

<br />
<img src="/media/gui.jpeg" alt="GUI screenshot">
<br />

# Gesture Guide

### Play
Raise open hands above shoulders, with palms facing forwards.
<br />
<br />
<img src="/media/play.jpeg" alt="Play gesture">
<br />

### Pause
Raise hands above shoulders in fists, with palms facing forwards.
<br />
<br />
<img src="/media/stop.jpeg" alt="Pause gesture">
<br />

### Fast forward
Point to the right with both hands in finger guns.
<br />
<br />
<img src="/media/forwards.jpeg" alt="Fast forward gesture">
<br />

### Rewind
Point thumbs to the left with the rest of the fingers curled in fists.
<br />
<br />
<img src="/media/back.jpeg" alt="Rewind gesture">
<br />

### Increase Volume
Point both index fingers up above shoulders, with thumbs sticking out.
<br />
<br />
<img src="/media/up.jpeg" alt="Increase volume gesture">
<br />

### Decrease Volume
With palms facing inwards, level with chest, curl fingers slightly so the are roughly parallel with shoulders.
<br />
<br />
<img src="/media/down.jpeg" alt="Decrease volume gesture">
<br />
<br />
<br />
Improvements for better reading of gestures at a distance will be coming soon. 
In the meantime, best results will come from a similar framing to the demo images above.
<br />
<br />
<br />
<br />
Thanks to [MediaPipe](https://mediapipe.dev/) for their excellent hand tracking model and their thorough [documentation](https://google.github.io/mediapipe/).

