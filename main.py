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


def measure():
  start = time.time()
  run_cf_api()
  stop = time.time()
  mili = int((stop-start)*1000)
  return mili



if __name__ == "__main__":
  l = []
  for i in range(0,10):
    mes = measure()
    print(mes)
    l.append(mes)
  over_8 = list(filter(lambda x: (x>= 800 and x< 900), l))
  over_9 = list(filter(lambda x: (x>= 900 and x< 1000), l))
  over_10 = list(filter(lambda x: (x>= 1000), l))
  print("Over 800ms:")
  print(len(over_8))
  print("Over 900ms:")
  print(len(over_9))
  print("Over 1000ms:")
  print(len(over_10))
  for i in over_10:
      print(i)
