import thread

gl  = 35

def worker(num):
    global gl
    num = int(num)
    ourstr = ''
    for i in range(num):
        ourstr += str(i)
        gl += 1
        print(gl)
    # print(ourstr)
    return


if __name__ == '__main__':
    N = 50
    while True:
        for i in range(N):
            thread.start_new_thread(worker, (15,))
        if input() == 'q':
            break
