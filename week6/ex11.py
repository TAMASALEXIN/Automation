import cProfile
import queue
import threading
import psutil
import time
from ex2 import download_site

def main():
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 20

    num_worker_threads = 1

    def worker(task_queue):
        while True:
            task = task_queue.get()
            if task is None:
                break
            download_site(task)
            task_queue.task_done()

    while num_worker_threads <= 8:
        cpu_percent = psutil.cpu_percent()
        virtual_memory = psutil.virtual_memory()
        if cpu_percent < 80 and virtual_memory.available > 1e9:  # 1 GB
            task_queue = queue.Queue()
            threads = []
            for i in range(num_worker_threads):
                t = threading.Thread(target=worker, args=(task_queue,))
                t.start()
                threads.append(t)

            for site in sites:
                task_queue.put(site)

            # block until all tasks are done
            task_queue.join()

            # stop workers
            for i in range(num_worker_threads):
                task_queue.put(None)
            for t in threads:
                t.join()

            print(f"Downloaded {len(sites)} in {num_worker_threads} threads")
            num_worker_threads += 1
        else:
            print(f"Resource usage too high (CPU: {cpu_percent}%, Memory: {virtual_memory.percent}%), waiting...")
            time.sleep(10)

if __name__ == "__main__":
    cProfile.run('main()')