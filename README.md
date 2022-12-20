# Virtual Shepherd

Description

The Virtual Shepherd allows a farmer to view their livestock remotely using a mobile application.

This can potentially prevent the loss/injury of livestock during lambing seasons, dog attacks and theft.

Phase 2 of the application will alert the farmer if an unrecognised human or animal enters the monitored paddock.

## Tools
1 - Raspberry Pi  
2 - WiFi Router  
3 - Raspberry Pi Camera Module  
4 - NGROK  
5 - Blynk  
6 - Smartphone  

  
## Code Language
Python

## Setup

Install Python:

https://raspberrytips.com/install-latest-python-raspberry-pi/

Camera Module Installation & Streaming:

https://www.tomshardware.com/how-to/stream-live-video-raspberry-pi


NGROK installation:

https://dashboard.ngrok.com/get-started/setup

BLYNK installation:

https://blynk.io/en/getting-started

## Using The Application

1. Ssh into Raspberry Pi via the Terminal.

2. Run mjpg streamer with the following command:

`export LD_LIBRARY_PATH=.
./mjpg_streamer  -i "input_uvc.so"`

3. Connect Raspberry Pi to Blynk Application. Run the following in terminal:

`python blynk.py`

4. Request a new NGROK secure URL. Enter the following command into terminal:

`./ngrok http 8080`

5. Enter the new URL into the Blynk Mobile Application via the **Video Streaming Widget**. 

Your stream is now ready to view !

## Issues

Raspberry Pi may require updates along the way. If any issues occur try:

`sudo apt-get update`

Then reboot the device and try again.

## Acknowledgments
Thank you to Frank Walsh for his guidance.

## Contact
Contact me at 20099913@mail.wit.ie 
