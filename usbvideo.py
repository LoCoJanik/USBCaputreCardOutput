import argparse
import cv2
import pyaudio
import numpy as np
import threading

class USBCapture:
    def __init__(self, videodeviceid, audiodeviceid, width, height, disableaudio):
        self.videodeviceid = int(videodeviceid)
        self.audiodeviceid = int(audiodeviceid)
        self.width = int(width)
        self.height = int(height)
        self.disableaudio = disableaudio
        self.ThreadsIsStop = False
        video = threading.Thread(target=self.videoOutput)
        audio = threading.Thread(target=self.audioOutput)
        video.start()
        if self.disableaudio != True:
            audio.start()


    def audioOutput(self):
        chunk = 32
        RATE = 48000
        # Connect to audio device
        p = pyaudio.PyAudio()
        # input stream
        stream = p.open(format=pyaudio.paFloat32, rate=RATE, channels=1, input_device_index=self.audiodeviceid, input=True,
                        frames_per_buffer=chunk)
        # output stream
        player = p.open(format=pyaudio.paFloat32, rate=RATE, channels=1, output=True, frames_per_buffer=chunk)

        while True:  # stream audio
            audiodata = np.frombuffer(stream.read(chunk, exception_on_overflow=False), dtype=np.float32)
            player.write(audiodata, chunk)

            if self.ThreadsIsStop == True:
                break

        # closes streams
        stream.stop_stream()
        stream.close()
        p.terminate

    def videoOutput(self):
        # Connect to webcam
        cap = cv2.VideoCapture(self.videodeviceid)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        cv2.namedWindow("USB Capture", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("USB Capture", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        # Loop through every frame until we close our webcam
        while cap.isOpened():
            ret, frame = cap.read()

            # Show image
            cv2.imshow('USB Capture', frame)

            # Checks whether q has been hit and stops the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Releases the webcam
        cap.release()
        # Closes the frame
        cv2.destroyAllWindows()
        self.ThreadsIsStop = True


def gatherArgs():
    # Prepare argparse arguments to be parsed from sys.argv

    parser = argparse.ArgumentParser(description="Show USB Video Input Stream")

    parser.add_argument('--videodeviceid', metavar="VIDEODEVICEID", default="0",
                        help="Index von 0 bis n")
    parser.add_argument('--audiodeviceid', metavar="AUDIODEVICEID", default="0",
                        help="Index von 0 bis n")
    parser.add_argument('--width', metavar="WIDTH", default="1920",
                        help="resolution width in px")
    parser.add_argument('--height', metavar="HEIGHT", default="1080",
                        help="resolution width in px")
    parser.add_argument('--disableaudio', dest='disableaudio', action='store_true')



    # Retrieve arguments or automatically print help if anything is not right
    args = parser.parse_args()

    # Return args object/namespace
    return args


if __name__ == '__main__':
    args = gatherArgs()
    print(args)
    USBCapture(args.videodeviceid, args.audiodeviceid, args.width, args.height, args.disableaudio)