# USBCaputreCardOutput
This are a Project to use VideoCaputreCard with an error in OBS (DecodeDeviceId failed)

This Python Script open the Video Source in Fullscreen.

# Install Python Libraries

```
pip install opencv-python
pip install pyaudio
```

# Start without changes:

```
./usbvideo.py
```

```
Default is --videodeviceid 0 --audiodeviceid 0 --width 1920 --height 1080
```
# Start with changes:

When your CaptureCard have another Output Options you must try 0 - n, equel of your Video Devices and Audio Devices

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
./usbvideo.py --videodeviceid n --audiodeviceid n --width x --height y
```
```
./usbvideo.py --disableaudio
```
```
./usbvideo.py --videodeviceid n --disableaudio --width x --height y 
```

# Quit the Fullscreen Window:
You can Close the Window with Q-Button (Quit)-Button


# Test:

Test only on Windows 10 & 11
