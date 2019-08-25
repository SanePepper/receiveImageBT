# receiveImageBT

This python program is used to save greyscale bluetooth data as an image(.bmp). Send the image pixel by pixel from top-left to bottom-rigt via bluetooth to the computer and run this program to save that as an image.

There should be a 1 second pause between sending each frame and it will have a beep sound after receiving one full image. Program will terminate after processing 100 frames.

Change line 6, 7 and 26 if you use a different COM port and have different image size.
Change line 10 and 27 if you want different naming for the images.
