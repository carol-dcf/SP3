# SP3
## SP3 of SCAV subject
In this project you can see applied some functionalities of the ffmpeg software into the BBB video (for computational reasons a shorter version is used). All the functions can be applied to any other video if the input_path is changed in the *main.py* file.

To run the program, run the *main.py* and a fully interactive menu will appear. There, you can navigate trough the different proposed exercises.

Instructions are really clear once you are running the files, however, here's a quick guide on how to use it.

| Num | Title         | Short explanation of the function                                                                                                                |
|-----|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Change video codec     | Given an input file (and all the versions: 720p, 480p, 360x240 & 160x120), converts it to the following formats/codecs: VP8, VP9, h265 & AV1. |
| 2   | Compare video codecs | Given two input files (from previous exercise), export a comparision between them. In this output file we will se both videos with different codecs in the same screen. |
| 3   | Stream and Choose IP  | Given an input file and an IP (chosen via terminal), broadcast it, so it can be streamed in VLC player.  This uses UPD protocol and needs an IP and port. Once the ffmpeg command is running, open VLC player and play network media pasting the url of the IP (@) and port chosen (eg. udp://localhost:23000). | 
| 0   | Exit          | Close application. |

(All the files generated in the different exercises on the BBB video can be seen in the Results folder)

Regarding exercise 2: we can see how the two are very similar since the chosen codecs (VP8 and VP9) do not differ that much. However, when using better resolutions, like in the 720p file, VP9 offers a better solution.

A comment about exercise 3 is that due to the high bitrate of the video, it cannot be streamed by VLC player. However if we look at the terminal we see that the frame packets are being sent. Moreover, we could see this streamed file if we open a new terminal in parallel and run the following command:
"ffplay udp://<IP>:<port>"
  you should be able to see the video.
