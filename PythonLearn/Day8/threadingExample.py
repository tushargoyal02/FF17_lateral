import threading


print(threading.current_thread().getName())

def valueGenerate():
    for count in range(0,12):
        print(count,threading.current_thread().getName())



t1=threading.Thread(target=valueGenerate )
t2=threading.Thread(target=valueGenerate )
t1.start()
t2.start()

t1.join()
t2.join()
print("########### hey user ########", threading.current_thread().getName())

