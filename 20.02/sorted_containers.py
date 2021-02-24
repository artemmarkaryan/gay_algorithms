import pprint
from collections import *
from typing import Type

pp = pprint.PrettyPrinter().pprint


# namedtuple()
# factory function for creating tuple subclasses with named fields
Point = namedtuple("Point", ["x", "y"])
pp(Point(x=1, y=1))

# deque
# list-like container with fast appends and pops on either end
d = deque()
d.append(1)
d.appendleft(0)
pp(d)

# ChainMap
# dict-like class for creating a single view of multiple mappings
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
pp(list(ChainMap(adjustments, baseline)))

# Counter
# dict subclass for counting hashable objects
#
# OrderedDict
# dict subclass that remembers the order entries were added
#
# defaultdict
# dict subclass that calls a factory function to supply missing values
#
# UserDict
# wrapper around dictionary objects for easier dict subclassing
#
# UserList
# wrapper around list objects for easier list subclassing
#
# UserString
# wrapper around string objects for easier string subclassing
