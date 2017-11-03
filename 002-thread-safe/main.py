import thread


def worker(s):
    print 'hello ' + str(s)
    return


if __name__ == '__main__':
    N = 5
    while True:
        for i in range(N):
            thread.start_new_thread(worker, ('world',))
        if input() == 'q':
            break
