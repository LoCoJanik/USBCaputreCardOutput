import argparse
import cv2
#from matplotlib import pyplot as plt

def gatherArgs():
    # Prepare argparse arguments to be parsed from sys.argv

    parser = argparse.ArgumentParser(description="Zeigt einen USB Video Input an")

    parser.add_argument('--deviceid', metavar="DEVICEID", default="0",
                        help="Index von 0 bis n")
    parser.add_argument('--width', metavar="WIDTH", default="1920",
                        help="Breite bei der Auflösung")
    parser.add_argument('--height', metavar="HEIGHT", default="1080",
                        help="Höhe der Auflösung")



    # Retrieve arguments or automatically print help if anything is not right
    args = parser.parse_args()

    # Return args object/namespace
    return args


if __name__ == '__main__':
    args = gatherArgs()
    print(args)
    # Connect to webcam
    cap = cv2.VideoCapture(int(args.deviceid))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(args.width))
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(args.height))
    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Loop through every frame until we close our webcam
    while cap.isOpened():
        ret, frame = cap.read()

        # Show image
        cv2.imshow('window', frame)

        # Checks whether q has been hit and stops the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Releases the webcam
    cap.release()
    # Closes the frame
    cv2.destroyAllWindows()