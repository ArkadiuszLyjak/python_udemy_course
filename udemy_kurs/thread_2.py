import threading
import time


def print_time(thread_name, sleep_time):
    num = 0
    max = 6

    while num < max:
        local_time = time.localtime()
        time_info = time.strftime("%H:%M:%S", local_time)
        print(f"{thread_name} {time_info}")
        time.sleep(sleep_time)
        num += 1

    print(thread_name, "koniec")


t1 = threading.Thread(target=print_time, args=("Thread 1", 0.1))
t2 = threading.Thread(target=print_time, args=("Thread 2", 0.2))
t3 = threading.Thread(target=print_time, args=("Thread 3", 0.3))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
