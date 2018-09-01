from multiprocessing import Process, Lock
 
 
def greeting(l, i):
    l.acquire()
    print 'hello', i
    l.release()
 
if __name__ == '__main__':
    lock = Lock()
    names = ['Alex', 'sam', 'Bernard', 'Patrick', 'Jude', 'Williams']
 
    for name in names:
        Process(target=greeting, args=(lock, name)).start()
