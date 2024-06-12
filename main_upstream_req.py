import sys

sys.path.insert(0, "/home/jo/.local/lib/python3.12/site-packages/")

import requests
import concurrent.futures
import time

def runHTTPFunction():
  return requests.get('https://www.google.com/humans.txt').content.decode("UTF-8")

def run_cf_api():
  with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
    futures = {executor.submit(runHTTPFunction): i for i in range(100)}
    for future in concurrent.futures.as_completed(futures, timeout=300):
      pass
  return 'Finished'

if __name__ == "__main__":
  start = time.time()
  run_cf_api()
  stop = time.time()
  print(stop-start)
