from __future__ import print_function

import multiprocessing
import os
import signal
import time


def run_worker(delay):
    print("In a worker process", os.getpid())
    time.sleep(delay)


def main():
    print("Initializng 2 workers")
    print("In a main process", os.getpid())
    original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
    original_sigterm_handler = signal.signal(signal.SIGTERM, signal.SIG_IGN)
    pool = multiprocessing.Pool(2)
    signal.signal(signal.SIGINT, original_sigint_handler)
    signal.signal(signal.SIGTERM, original_sigterm_handler)
    try:
        print("Starting 2 jobs of 5 seconds each")
        res = pool.map_async(run_worker, [50, 50])
        print("Waiting for results")
        # Without the timeout this blocking call ignores all signals.
        res.get(60)
    except KeyboardInterrupt:
        print("Caught KeyboardInterrupt, terminating workers")
        pool.terminate()
    except SystemExit:
        print("Caught KeyboardInterrupt, terminating workers")
        pool.terminate()
    else:
        print("Normal termination")
        pool.close()
    pool.join()


if __name__ == "__main__":
    main()
