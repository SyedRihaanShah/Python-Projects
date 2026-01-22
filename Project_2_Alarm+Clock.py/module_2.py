import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Indicates some task being done
def func(seconds):
  print(f"Sleeping for {seconds} seconds")
  time.sleep(seconds)#time.sleep() stops the code at the particular line for the following time 
  return seconds

def main():
  time1 = time.perf_counter()
  # Normal Code
  # func(4) 
  # func(2)
  # func(1)
  
  
  # Same code using Threads
  t1 = threading.Thread(target=func, args=[4])
  t2 = threading.Thread(target=func, args=[2])
  t3 = threading.Thread(target=func, args=[1])
  t1.start()
  t2.start()
  t3.start()
  
  t1.join()#.join() is used to wait for the longest time taking thread
  t2.join()
  t3.join()
  # Calculating Time 
  time2 = time.perf_counter()
  print(time2 - time1)


def poolingDemo():
  with ThreadPoolExecutor() as executor:
#  What is ThreadPoolExecutor and why it is used : 
# It is a thread pool manager that:
# Creates a set number of worker threads
# Lets you submit tasks (functions) to run in those threads

# Handles scheduling, execution, and returning results
    # future1 = executor.submit(func, 3)
    # future2 = executor.submit(func, 2)
    # future3 = executor.submit(func, 4)
    # print(future1.result())
    # print(future2.result())
    # print(future3.result())
    l = [3, 5, 1, 2]
    results = executor.map(func, l)
    for result in results:
      print(result)


poolingDemo()