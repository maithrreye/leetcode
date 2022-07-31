"""
Linear stack,queue and list are all O(N) in most of the operation 

So Link list with Hash is one solution 

Doubly LL is better than SLL.
One advantage of double linked list is that the node can remove itself without other reference. 

In addition, it takes constant time to add and remove nodes from the head or tail.

#Time Complexity : O(1)
#Space Complexity : O(capacity)

You can also directly use Ordered Dict in python it combines behind both hashmap and linked list 

Problem: https://leetcode.com/problems/lru-cache/

"""


class Node:
    
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None
    
    

class LRUCache:

    def __init__(self, capacity: int):
        """
        Create Head, tail dummy node
        Create hashmap to store key and Node(val)
        Put capacity for size check 
        Init all the next , prev pointers
    
        """
        
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.hash={}
        self.capacity=capacity 
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def addToHead(self,node):
        """
        First set the node's next and prev
        now set heads's next and head's older next
    
        """
        
        node.next=self.head.next
        node.prev=self.head
        self.head.next=node
        node.next.prev=node
        
    def remove(self,node):
        """
        Remove the given node
        node.prev.next
        node.next.prev
        
        """
        node.prev.next=node.next
        node.next.prev=node.prev
        

    def get(self, key: int) -> int:
        """
        Using key, get the node 
        remove node from last and put near head 
        
        """
        if key not in self.hash:
            return -1
        node=self.hash[key]
        self.remove(node)
        self.addToHead(node)
        
        return node.val
        

    def put(self, key: int, value: int) -> None:
        
        """
        Two cases : whether key is in hash or not 
        
        Key in Hash:
            get the existing node 
            update value 
            remove that Node
            add this node to head
        
        When Key not in Hash:
            create new node
            check capacity 
                if capacity full , remove least recently used 
            add the new node to head 
            add this to hash 
        """
        
        if key in self.hash:
            node= self.hash[key]
            node.val=value
            self.remove(node)
            self.addToHead(node)
        else:
            newnode=Node(key,value)
            if(self.capacity==len(self.hash)):
                #remove least used which is tail prev 
                tailprev=self.tail.prev
                self.remove(tailprev)
                del self.hash[tailprev.key]
            self.addToHead(newnode)
            self.hash[newnode.key]=newnode
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
