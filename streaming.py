import os
from math import sin


class Streaming:
    def __init__(self, input_path):
        self.input_path = input_path
        self.output_folder = "Results/"
        if not os.path.exists(self.output_folder):
            os.mkdir(self.output_folder)

    # exercise 1: change video codedc
    def video_motion_vectors(self):
        output_path = self.output_folder + "analysis_" + self.short_input_path
        analysis_command = "ffmpeg -flags2 +export_mvs -i " + self.short_input_path + " -vf codecview=mv=pf+bf+bb " + output_path
        os.system(analysis_command)
        return output_path

    # exercise 2: compare video codecs
    def compare_vcodecs(self, codec1, codec2):
        output_path = self.output_folder + "comparision_" + self.input_path
        return output_path

    # exercise 3: live streaming
    def stream2VLC(self, ip):
        #stream_command = "ffmpeg -re -i " + self.input_path + " -acodec libmp3lame -ar 11025 -f rtp rtp://localhost:8888"
        stream_command = "ffmpeg -re -i " + self.input_path + " -v 0 -vcodec libx264 -pix_fmt yuv420p -f mpegts udp://localhost:23000"
        # stream_command = "ffmpeg -i " + self.input_path + " -v 0 -vcodec libx264 -pix_fmt yuv420p -f mpegts udp://127.0.0.1:23000"
        # stream_command = "ffmpeg -i " + self.input_path + " -f mpegts tcp://localhost:8888"
        #stream_command = "ffmpeg -i " +  self.input_path + " -f mpegts udp://localhost:8888"
        os.system(stream_command)
        return
