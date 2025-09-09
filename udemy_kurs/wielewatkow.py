import _thread
import time


def print_time(thread_name, sleep_time):
    num = 0
    max = 6

    while num < max:
        local_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"{thread_name} {local_time}")
        time.sleep(sleep_time)
        num += 1

    print(thread_name, "koniec")


_thread.start_new_thread(print_time, ("Thread 1", 1))
_thread.start_new_thread(print_time, ("Thread 2", 2))

while True:
    pass
