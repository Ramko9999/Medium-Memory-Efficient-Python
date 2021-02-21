from memory_profiler import profile
from array import array


'''
Output from profiler:

Filename: arr_perf.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     5   16.254 MiB   16.254 MiB           1   @profile
     6                                         def simulate_list():
     7   16.254 MiB    0.000 MiB           1       amount = 1000000
     8   16.254 MiB    0.000 MiB           1       l = []
     9   35.766 MiB -3538.324 MiB     1000001       for i in range(amount):
    10   35.766 MiB -3519.348 MiB     1000000           l.append(i)
'''

@profile
def simulate_list():
  amount = 1000000
  l = []
  for i in range(amount):
    l.append(i)

'''
Output from profiler:

Filename: arr_perf.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    13   16.164 MiB   16.164 MiB           1   @profile
    14                                         def simulate_array():
    15   16.164 MiB    0.000 MiB           1       amount = 1000000
    16   16.172 MiB    0.008 MiB           1       a = array('i', [])
    17   20.457 MiB    0.012 MiB     1000001       for i in range(amount):
    18   20.457 MiB    4.273 MiB     1000000           a.append(i)
'''
@profile
def simulate_array():
  amount = 1000000
  a = array('i', [])
  for i in range(amount):
    a.append(i)