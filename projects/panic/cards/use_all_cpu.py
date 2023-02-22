import os
import threading
import hashlib

def busy():
  s = 'P' * 1024 * 1024
  b = s.encode("utf-8")
  while True:
    # do useless work
    # compute the SHA256 checksum
    # of 1048576 Ps: PPPPPP..
    hashlib.sha256(b)

n_cores = os.cpu_count()

# create n_cores * 2 threads
# each running the busy function
threads = []
for i in range(n_cores * 2):
  t = threading.Thread(target=busy)
  t.start()

  threads.append(t)

# wait for the threads to finish
for t in threads:
  t.join()
