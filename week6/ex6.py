# Task6: Integrate asyncio with ThreadPoolExecutor to combine the advantages of asynchronous I/O and thread-based parallelism.
# Use asyncio.to_thread() function to execute blocking I/O operations within a separate thread.

import concurrent.futures
import requests
import threading
import time
import asyncio



thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

async def download_all_sites(sites):
    tasks = [asyncio.to_thread(download_site, site) for site in sites]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    asyncio.run(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")


# Downloaded 160 in 1.7198529243469238 seconds 
# Downloaded 160 in 2.878246784210205 seconds (max_workers=5)
# Downloaded 160 in 1.9196999073028564 seconds (max_workers=10)x
