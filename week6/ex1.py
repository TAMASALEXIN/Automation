# Task1: Write a script to asynchronously download 5 websites using the asyncio module.
# Use the asyncio module to define asynchronous functions for downloading websites (download_site) and downloading all sites concurrently (download_all_sites).
# Execute the script using asyncio.run() or by creating an event loop with asyncio.get_event_loop().run_until_complete().   


# Task2: Enhance the previous script to handle exceptions gracefully using try-except blocks in the download_site function.
# Implement error handling within the download_site function using try-except blocks to catch exceptions raised during the HTTP request.
# Consider handling specific exceptions like aiohttp.ClientError for better error reporting.


# Task5: Implement a semaphore mechanism using asyncio.Semaphore to limit the maximum number of concurrent downloads.
# Acquire and release the semaphore appropriately within the download_site function to control concurrency.


import asyncio
import aiohttp
from asyncio import Semaphore

async def download_site(url, session, semaphore):
    await semaphore.acquire()
    try:
        async with session.get(url) as response:
            print("Read {0} from {1}".format(response.content_length, url))
    except aiohttp.ClientError as ce:
        print(f"Error: {ce}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        semaphore.release()

async def download_all_sites(sites,semaphore):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(url, session, semaphore))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    sites = [
        "http://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 5
    # asyncio.run(download_all_sites(sites))

    # Alternatively, create an event loop and run until complete
    
    loop = asyncio.get_event_loop()
    semaphore = asyncio.Semaphore(5)
    loop.run_until_complete(download_all_sites(sites, semaphore))


    