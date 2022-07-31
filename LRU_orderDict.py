"""
Python OrderedDict 

OrderedDict preserves the order in which the keys are inserted.

A regular dict doesn’t track the insertion order and iterating it gives the values in an arbitrary order

If the value of a certain key is changed, the position of the key remains unchanged in OrderedDict.

 Deleting and re-inserting the same key will push it to the back as OrderedDict, however, maintains the order of insertion.

popitem(last=True)
The popitem() method for ordered dictionaries returns and removes a (key, value) pair. 
The pairs are returned in LIFO order if last is true or FIFO order if false.

move_to_end(key, last=True)
Move an existing key to either end of an ordered dictionary. The item is moved to the right end if last is true (the default) or to the beginning if last is false. Raises KeyError if the key does not exist:

OrderedDict: https://docs.python.org/3/library/collections.html#ordereddict-objects

Leetcode: https://leetcode.com/problems/lru-cache/

"""


from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self:
            return - 1
        
        self.move_to_end(key)
        return self[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False) 
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
