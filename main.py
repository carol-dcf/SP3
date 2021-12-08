from streaming import Streaming

if __name__ == "__main__":
    # create instance
    sp3 = Streaming("cut_bbb.mp4")

    # Interactive menu
    ex = 1
    while ( ex != 0 ):
        print("\033[1m\nChoose an exercise:\033[0m")
        print("\t 1. Change video codec" + "\n\t 2. Compare video codecs" + "\n\t 3. Stream" + "\n\t 4. Choose IP" + "\n\t 0. Exit")

        ex = int(input())

        #### 1 #####
        if (ex == 1):
            print("\033[1mEXERCISE 1\033[0m")


        #### 2 #####
        elif (ex == 2):
            print("\n\033[1mEXERCISE 2\033[0m")


        elif (ex == 3):
            #### 3 #####
            print("\n\033[1mEXERCISE 3\033[0m")
            sp3.stream2VLC("rtp://92.178.211.111:9999")

        elif (ex == 4):
            #### 4 #####
            print("\n\033[1mEXERCISE 4\033[0m")

        elif (ex == 0):
            print("Application closed.")
        else:
            print("Not a valid option.")