# Parallel_example
An example of using ipyparallel


I always forget how to do things in parallel in python, so here's my quick example.


The problem is usually that there's a n object that can't be pickled, so you need to build the object on the engines, and have each engine get the data it needs, then collect the results.