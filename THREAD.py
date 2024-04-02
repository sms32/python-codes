from threading import *
class Buffer:
    def put(self,data):
        cv.acquire()
        self.data = data
        print('Producer:',self.data)
        cv.notify()
        cv.wait()
        cv.release()

    def take(self):
        cv.acquire()
        print('Consumer:',self.data)
        cv.notify()
        cv.wait()
        cv.release()

class Producer(Thread):
    def __init__(self,bufferObj):
        Thread.__init__(self)
        self.bufferObj=bufferObj

    def run(self):
        for i in range(1,6):
            self.bufferObj.put(i)


class Consumer(Thread):
    def __init__(self,bufferObj):
        Thread.__init__(self)
        self.bufferObj=bufferObj

    def run(self):
        for i in range(1,6):
            self.bufferObj.take()


    
    

cv=Condition()
bufferObj=Buffer()
producer=Producer(bufferObj)
producer.start()
consumer=Consumer(bufferObj)
consumer.start()
producer.join()
consumer.join()
