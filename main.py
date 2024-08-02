import requests
import concurrent.futures
import time
from statistics import median

def runHTTPFunction():
  return requests.get('https://www.google.com/humans.txt').content.decode("UTF-8")

def run_cf_api():
  with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
    futures = {executor.submit(runHTTPFunction): i for i in range(100)}
    for future in concurrent.futures.as_completed(futures, timeout=300):
      pass
  return 'Finished'


def measure():
  start = time.time()
  run_cf_api()
  stop = time.time()
  mili = int((stop-start)*1000)
  return mili


def roundup(x):
    return x if x % 100 == 0 else x + 100 - x % 100


if __name__ == "__main__":
  n = [10,20,50,100,500,1000]
  for j in n:
    print("######Results for %d j runs######" % len(range(0,j)))
    l = []
    for i in range(0,j):
      mes = measure()
      l.append(mes)
    med = median(l)
    print("Median: %d" % med)
    start = int(roundup(med))
    while(start < 1000):
        next = start+100
        over = list(filter(lambda x: (x>= start and x< next), l))
        print("Over %d ms: %d" % (start, len(over)))
        start = next
    over_1000 = list(filter(lambda x: (x>= 1000), l))
    print("Over 1000 ms: %d" % len(over_1000))
    print("#################################")
