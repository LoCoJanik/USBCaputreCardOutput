# USBCaputreCardOutput
This are a Project to use VideoCaputreCard with an error in OBS (DecodeDeviceId failed)

This Python Script open the Video Source in Fullscreen.

# Start without changes

```
./usbvideo.py
```
```
Default is --deviceid 0 --width 1920 --height 1080
```

When your CaptureCard have another Output Options you must try 0 - n equel of your VideoDevices

When you are need the Resolution Option you need:

```
--width 1920 --height 1080
```

For Example: 

```
./usbvideo.py --deviceid 0 --width 1920 --height 1080
```

You can Close the Window with Q (Quit)

# Install Python Libraries

```
pip install opencv-python
```
