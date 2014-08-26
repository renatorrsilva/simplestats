import math

def mean(vals):
	"""Computes the mean from a list of values"""
	total = sum(vals)
	length = len(vals)
	return float(total)/float(length)
	
def test_float_mean():
	assert(mean[1,2]== 1.5)
	
def test_mean():
	assert(mean([2,4])== 3)
	
def median(vals):
    vals.sort()
    length = len(vals)
    index = length / 2
    if length % 2 == 0:
       return mean([vals[index], vals[index - 1]])
    else:
       return vals[index]