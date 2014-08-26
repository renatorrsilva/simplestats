<<<<<<< HEAD
def mean(vals):
    """Computes the mean from a list of values."""
    try:
        total = float(sum(vals))
        length = len(vals)
    except TypeError:
        raise TypeError("The list was not numbers.")
    except:
        print "Something unknown happened with the list."
    return total/length

def median(numlist):
    numlist.sort()
    length = len(numlist)
    index = length/2

    if length % 2 == 0:
        return mean([numlist[index], numlist[index - 1]])
    else:
        return numlist[index]

def mode(vals):
    """Computes the mode from a list of values."""
    pass
=======
import math
>>>>>>> ad163593aa3d50f6b7b5fd9ba97deb43a00c8d16

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
