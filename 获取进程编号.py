import multiprocessing
import time
import os

def dance():

    dance_id=os.getpid()
    dance_parent_id = os.getppid()
    print(f"dance_id:{dance_id}, dance_parent_id:{dance_parent_id}")


    for i in range(3):
        print("跳舞中。。。")
        time.sleep(0.2)


def sing():
    sing_id = os.getpid()
    sing_parent_id = os.getppid()
    print(f"dance_id:{sing_id}, dance_parent_id:{sing_parent_id}")

    for i in range(3):
        print("唱歌中。。。")
        time.sleep(0.2)


if __name__ == '__main__':

    Mail_process_id = os.getpid()

    print("Mail_process_id:" , Mail_process_id)

    dance_process = multiprocessing.Process(target=dance)
    dance_process.start()

    sing()