# Attempts to generate rhythms based on random probability, a less
# preferred method as it can lead to too many recursive calls but
# makes a fun project. lex_runs.py generates every sequence however
# -----------------------------------------------------------------------
# Import Statements
# -----------------------------------------------------------------------
import numpy as np
# -----------------------------------------------------------------------
# Function Definitions
# -----------------------------------------------------------------------
np.random.seed(19680801)
# Future update, use inverse squared probabilities for less fucky results
prob_percent = 0.87
even_beat_prob = 0.75
no_beat_prob = 0.3
n_runs = 100
def n_beats(n):
   # returns an array of length n initialized to zeros
   measure = []
   for i in range(n):
      measure.append(0)
   return measure
def drop_the_beat():
   # Returns either a list with 0 initialized values or a 1, or a 0
   if np.random.rand() <  prob_percent:
      if np.random.rand() < no_beat_prob:
         return 0
      else:
         return 1
   # return a list to be some percent an even integer, and some percent
   # an odd integer
   else:
      subbeat = []
      if np.random.rand() < even_beat_prob:
         # generate a even number
         n = int(-1*np.log(np.random.rand())) + 1
         n *= 2
      else:
         # generate an odd number
         n = int(-1*np.log(np.random.rand())) + 1
         n = 2*n - 1
      for b in range(n):
         subbeat.append(0)
         # Recursively call until we have just ones
         for beat in range(len(subbeat)):
            subbeat[beat] = drop_the_beat()
      return subbeat
# let the length of an array denote the maximum number of beats to fit in
# a measure. with 0 indicating a break
# -----------------------------------------------------------------------
# Main Function
# -----------------------------------------------------------------------
# inside every beat, is either a 1, indicating a quarter note, or another
# list, indicating the length of that list is the number of subdivisions
# of the beat
for j in [2, 4, 6, 8, 10]: 
   for i in range(n_runs):
      a = n_beats(j)
      for i in range(len(a)):
         a[i] = drop_the_beat()
      print(a)
