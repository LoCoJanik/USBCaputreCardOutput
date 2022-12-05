# USBCaputreCardOutput
This are a Project to use VideoCaputreCard with an error in OBS (DecodeDeviceId failed)

This Python Script open the Video Source in Fullscreen.

# Install Python Libraries

```
pip install opencv-python
```

# Start without changes:

```
./usbvideo.py
```
```
Default is --deviceid 0 --width 1920 --height 1080
```
# Start with changes:

When your CaptureCard have another Output Options you must try 0 - n equel of your VideoDevices

When you are need the another Resolution Option:

```
--width 1920 --height 1080
```

For Example with full options: 

```
./usbvideo.py --deviceid 0 --width 1920 --height 1080
```

# Quit the Fullscreen Window:
You can Close the Window with Q-Button (Quit)-Button
