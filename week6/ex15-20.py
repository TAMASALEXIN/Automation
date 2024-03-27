# Exercise 15: Task Prioritization
# Task: Implement task prioritization to ensure that more important tasks are processed first.
# Assign priority levels to each download task based on criteria such as site importance, urgency, or expected download time.
# Use priority queues or scheduling algorithms like Shortest Job First (SJF) to order tasks based on priority.
# Exercise 16: Resource Allocation
# Task: Experiment with different resource allocation strategies to optimize performance and resource utilization.
# Allocate resources such as CPU cores, memory, and network bandwidth based on task requirements and system constraints.
# Monitor resource usage and adjust allocation dynamically to adapt to changing workload conditions.
# Exercise 17: Fault Tolerance
# Task: Enhance fault tolerance by implementing mechanisms for handling network failures, timeouts, and other errors.
# Use retry strategies with exponential backoff to recover from transient failures.
# Implement circuit breaker patterns to temporarily suspend requests to failing services and prevent cascading failures.
# Exercise 18: Optimizing Network IO
# Task: Optimize network IO operations by minimizing latency and maximizing throughput.
# Use techniques such as connection pooling, persistent connections, and pipelining to reduce overhead and improve efficiency.
# Experiment with different HTTP client libraries and configurations to find the optimal settings for performance.
# Exercise 19: Parallelism in Real-world Applications
# Task: Apply parallelism techniques learned to real-world scenarios such as web scraping, API integration, or data processing.
# Identify opportunities for parallelism in existing applications and refactor code to leverage parallel execution.
# Measure the impact of parallelism on application performance and scalability.
# Exercise 20: Benchmarking and Optimization
# Task: Benchmark the performance of different parallelism strategies and optimize the script for maximum efficiency.
# Identify performance bottlenecks using profiling tools and performance monitoring.
# Optimize code, configuration, and resource allocation to improve overall performance and scalability.


import concurrent.futures
import requests
import threading
import time
import psutil
import asyncio
from asyncio import Semaphore
import aiohttp
from queue import PriorityQueue
import cProfile

class Sentinel:
    def __lt__(self, other):
        return True

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    session = get_session()
    for _ in range(3):  # retry up to 3 times
        try:
            with session.get(url, stream=True) as response:
                content_length = sum(len(chunk) for chunk in response.iter_content(1024))
                print(f"Read {content_length} from {url}")
                break  # if the download was successful, break the loop
        except requests.exceptions.RequestException as re:
            print(f"Error: {re}")
        except Exception as e:
            print(f"Error: {e}")

def download_all_sites(sites, max_workers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(download_site, sites)

def worker(task_queue):
    while True:
        priority, task = task_queue.get()
        if isinstance(task, Sentinel):
            break
        download_site(task)
        task_queue.task_done()

def main():
    sites = [
        (1, "https://www.jython.org"),
        (2, "http://olympus.realpython.org/dice"),
    ] * 10

    num_worker_threads = 1

    while num_worker_threads <= 8:
        cpu_percent = psutil.cpu_percent()
        virtual_memory = psutil.virtual_memory()
        if cpu_percent < 80 and virtual_memory.available > 1e9:  # 1 GB
            
            task_queue = PriorityQueue()

            for priority, site in sites:
                task_queue.put((priority, site))

            threads = []
            for i in range(num_worker_threads):
                t = threading.Thread(target=worker, args=(task_queue,))
                t.start()
                threads.append(t)

            # block until all tasks are done
            task_queue.join()

            # stop workers
            for i in range(num_worker_threads):
                task_queue.put((0, Sentinel()))
            for t in threads:
                t.join()

            print(f"Downloaded {len(sites)} in {num_worker_threads} threads")
            num_worker_threads += 1
        else:
            print(f"Resource usage too high (CPU: {cpu_percent}%, Memory: {virtual_memory.percent}%), waiting...")
            time.sleep(10)

if __name__ == "__main__":
    cProfile.run('main()')

