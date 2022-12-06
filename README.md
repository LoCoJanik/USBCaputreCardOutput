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
Default is --videodeviceid 0 --audiodeviceid 0 --width 1920 --height 1080 
```
# Start with changes:

When your CaptureCard have another Output Options you must try 0 - n, equel of your VideoDevices

```
./usbvideo.py --videodeviceid 0
```
```
./usbvideo.py --videodeviceid 0 --audiodeviceid 0
```
```
./usbvideo.py --width 1920 --height 1080
```
```
./usbvideo.py --videodeviceid n --width 1920 --height 1080
```

# Quit the Fullscreen Window:
You can Close the Window with Q-Button (Quit)-Button


# Test:

Test only on Windows 10 & 11
