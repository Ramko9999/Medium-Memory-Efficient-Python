from memory_profiler import profile

class Dog:  
  def __init__(self, name, age):
    self.name = name
    self.age = age

class SlotDog:    
   __slots__=("name", "age")
   def __init__(self, name, age):
     self.name = name
     self.age = age

'''
Output from profiler:

Filename: slots_perf.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    14     18.6 MiB     18.6 MiB           1   @profile
    15                                         def sim_no_slots():
    16     35.1 MiB     16.5 MiB      100003     dogs = [Dog("James", 5) for i in range(100000)]
'''

@profile
def sim_no_slots():
  dogs = [Dog("James", 5) for i in range(100000)]

'''
Output from profiler:

Filename: slots_perf.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    27     18.6 MiB     18.6 MiB           1   @profile
    28                                         def sim_slots():
    29     24.4 MiB      5.8 MiB      100003     dogs = [SlotDog("James", 5) for i in range(100000)]

'''
@profile
def sim_slots():
  dogs = [SlotDog("James", 5) for i in range(100000)]