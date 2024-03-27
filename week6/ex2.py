# Task3: Modify the ThreadPoolExecutor to have a higher value for max_workers parameter (e.g., 10) to increase concurrency.
# Ensure that the system can handle the increased concurrency level without exhausting resources such as CPU or memory.

# Task4: Implement a mechanism to measure the time taken by each site download individually and print it out.
# Track the start and end time for each site download within the download_site function.
# Calculate the time taken for each site download and print it out along with the site URL.


# Task7: Experiment with different values for the max_workers parameter in ThreadPoolExecutor to find the optimal concurrency level.
# Measure the script's performance for each concurrency level to determine the most efficient setting.

# Task8: Implement error handling using try-except blocks within the download_site function similar to the asyncio script.
# Handle exceptions raised during HTTP requests and ensure proper error reporting and logging.

# Task9: Optimize memory usage by avoiding unnecessary data duplication or excessive resource allocation.
# Use streaming or chunked transfer encoding for large responses to minimize memory consumption.

# Task10: Implement resource management techniques such as resource pooling or dynamic resource allocation to efficiently utilize system resources.
# Monitor resource usage using system utilities or libraries like psutil and adjust concurrency accordingly.

# Task11: Implement a load balancing mechanism to evenly distribute workload across available threads or processes.
# Use techniques such as round-robin scheduling or weighted load balancing based on system metrics.
# Monitor the load on each worker and dynamically adjust the workload distribution if necessary.

import concurrent.futures
import requests
import threading
import time
import psutil

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    start_time = time.time()
    try:
        with session.get(url, stream=True) as response:
            content_length = sum(len(chunk) for chunk in response.iter_content(1024))
            print(f"Read {content_length} from {url}")
    except requests.exceptions.RequestException as re:
        print(f"Error: {re}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        end_time = time.time()
        print(f"Downloaded {url} in {end_time-start_time} seconds")


def download_all_sites(sites, max_workers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 10
    durations = {}
    max_workers = 1
    while max_workers <= 20:
        cpu_percent = psutil.cpu_percent()
        virtual_memory = psutil.virtual_memory()
        if cpu_percent < 80 and virtual_memory.available > 1e9:  # 1 GB
            start_time = time.time()
            download_all_sites(sites, max_workers)
            duration = time.time() - start_time
            durations.update({f"max_workers={max_workers}": f"{duration}"})
            print(f"Downloaded {len(sites)} in {duration} seconds (max_workers={max_workers})")
            max_workers += 1
        else:
            print(f"Resource usage too high (CPU: {cpu_percent}%, Memory: {virtual_memory.percent}%), waiting...")
            time.sleep(10)
    
    print(durations)
    print(f"Optimal concurrency level: {min(durations, key=durations.get)}")


# Downloaded 160 in 2.878246784210205 seconds (max_workers=5)
# Downloaded 160 in 1.9196999073028564 seconds (max_workers=10)x

