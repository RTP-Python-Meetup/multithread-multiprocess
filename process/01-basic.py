from multiprocessing import Process
 
 
def square(x):
 
    for x in numbers:
        print('%s squared  is  %s' % (x, x**2))
 
if __name__ == '__main__':
    numbers = [43, 50, 5, 98, 34, 35]
 
    p = Process(target=square, args=('x',))
    p.start()
    p.join
    print "Done"
