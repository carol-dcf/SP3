import os
from math import sin


class Streaming:
    # Class constructor
    def __init__(self, input_path):
        self.input_path = input_path
        # Same input but in different resolutions
        self.input_path_720p = "720p_" + input_path
        self.input_path_480p = "480p_" + input_path
        self.input_path_240p = "240p_" + input_path
        self.input_path_120p = "120p_" + input_path
        # list of different inputs
        self.other_input_paths = [self.input_path_720p, self.input_path_480p, self.input_path_240p, self.input_path_120p]
        self.output_folder = "Results/"
        # create output folder if it does not exist yet
        if not os.path.exists(self.output_folder):
            os.mkdir(self.output_folder)

    # exercise 1: change video codedc
    def change_codec(self, new_codec):
        """
        Change the codec of the videos in different resolutions.
        :param new_codec: codec chosen (VP8, VP9, h265 or AV1)
        :return: output_paths -> list of the paths of the created videos (new codecs used in this case)
        """
        output_paths = []
        for input in self.other_input_paths:
            output_path = self.output_folder + new_codec + "_" + input.split(".")[0]
            output_paths.append(output_path)
            ## Conversion command for each codec
            if new_codec == "VP8":
                codec_command = "ffmpeg -i " + input + " -c:v libvpx -b:v 1M -c:a libvorbis " + output_path + ".webm"
            elif new_codec == "VP9":
                codec_command = "ffmpeg -i " + input + " -c:v libvpx-vp9 -b:v 2M " + output_path + ".webm"
            elif new_codec == "h265":
                codec_command = "ffmpeg -i " + input + " -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k " + output_path + ".mp4"
            elif new_codec == "AV1":
                codec_command = "ffmpeg -i " + input + " -c:v libaom-av1 -crf 30 -b:v 0 " + output_path + ".mkv"
            print(codec_command)
            os.system(codec_command)
        return output_path

    # exercise 2: compare video codecs
    def compare_vcodecs(self, codec1, codec2, codec1_path, codec2_path):
        """
        Show in the same screen each video for 2 different codecs used.
        :param codec1: codec used for first video (eg. VP8)
        :param codec2: codec used for second video (eg. VP9)
        :param codec1_path: first video path
        :param codec2_path: second video path
        :return: output_path -> path of the created video (comparision of video codecs in this case)
        """
        output_path = self.output_folder + codec1 + "_" + codec2 + "_" + "comparision_" + self.input_path
        compare_command = "ffmpeg -i " + codec1_path + " -i " + codec2_path + " -filter_complex hstack " + output_path
        print("\n" + compare_command + "\n")
        os.system(compare_command)
        return output_path

    # exercise 3: live streaming
    def stream2VLC(self, ip):
        """
        Stream a video (locally) to a VLC player for instance.
        :param ip: IP + port to broadcast the video to
        :return:
        """
        stream_command = "ffmpeg -re -i " + self.input_path + " -f flv udp://" + ip
        print("\n" + stream_command + "\n")
        os.system(stream_command)
        return

    # exercise 4: choose IP
    def choose_ip(self):
        """
        Choose IP address which we are going to broadcast to.
        :return: final_ip -> IP address, including the port
        """
        ip = str(input("Input your IP address (eg. 127.0.0.1): "))
        port = str(input("Input your port (eg. 23000): "))
        final_ip = ip + ":" + port
        print("Your chosen IP address to broadcast to is: ", final_ip)
        return final_ip
