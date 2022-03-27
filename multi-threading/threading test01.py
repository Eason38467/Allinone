import threading
import time


def sing():

    # get threading ID
    current_thread = threading.current_thread()
    print('sing:', current_thread)
    for i in range(3):
        print('singing')
        time.sleep(0.2)



if __name__ == '__main__':

    current_thread = threading.current_thread()
    print('main_thread:', current_thread)
    sing_thread = threading.Thread(target=sing)
    sing_thread.start()