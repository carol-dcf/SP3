from streaming import Streaming

if __name__ == "__main__":
    # create instance
    sp3 = Streaming("bbb.mp4")

    # Interactive menu
    ex = 1
    while ( ex != 0 ):
        print("\033[1m\nChoose an exercise:\033[0m")
        print("\t 1. Change video codec" + "\n\t 2. Compare video codecs" + "\n\t 3. Stream and Choose IP" + "\n\t 0. Exit")

        ex = int(input())

        #### 1 #####
        if (ex == 1):
            print("\033[1mEXERCISE 1\033[0m")
            sp3.change_codec("VP8")
            sp3.change_codec("VP9")
            sp3.change_codec("h265")
            sp3.change_codec("AV1")

        #### 2 #####
        elif (ex == 2):
            print("\n\033[1mEXERCISE 2\033[0m")
            sp3.compare_vcodecs("VP8", "VP9", "Results/VP8_720p_bbb.webm", "Results/VP9_720p_bbb.webm")


        elif (ex == 3):
            #### 3 #####
            print("\n\033[1mEXERCISE 3\033[0m")
            ip = sp3.choose_ip()
            sp3.stream2VLC(ip)

        elif (ex == 0):
            print("Application closed.")
        else:
            print("Not a valid option.")