import atexit
import requests
import logging
import shelve

# Set up logging with timestamp and level
logging.basicConfig(
    # Put the timestamp at the beginning of each log message
    # Put level next
    format="%(levelname)s: %(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.WARN,
)

# store data in a file
cache = shelve.open(".cache")


def close_cache():
    logging.info("Closing cache")
    cache.close()


atexit.register(close_cache)


# Generate headers for the request
def generate_headers():
    return {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }


# Get HTTP response from the API or from the cache
def get_or_cache(url):
    if url in cache:
        return cache[url]
    response = requests.get(url, headers=generate_headers())
    cache[url] = response.text
    return cache[url]
