import multiprocessing

def show_info(name,age):
    print(name,age)

if __name__=='__main__':
    sub_procress=multiprocessing.Process(target=show_info(1,15))

    sub_procress.start()