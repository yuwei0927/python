import queue
import threading

thread_count = 20
threads = []

def pr():
    while not queue.empty():
        num = queue.get()
        print(num)

queue = queue.Queue()
for i in range(0,1000):
    queue.put(i)

for num in range(thread_count):
    t = threading.Thread(target=pr)
    #t = threading.Thread(target=pr())
    threads.append(t)
    t.start()

for t in threads:
    t.join()
