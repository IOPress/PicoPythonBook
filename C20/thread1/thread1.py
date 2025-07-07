import _thread
import time
counter=0

#myLock=_thread.allocate_lock()
def task():    
    global counter,myLock
    print("thread started")

    for i in range(1000):
      #  myLock.acquire()
        counter=counter+1     
      #  myLock.release()   

_thread.start_new_thread(task,())
for i in range(1000):
     #   myLock.acquire()
        counter=counter+1     
     #   myLock.release() 
time.sleep(0.5)    
print(counter)