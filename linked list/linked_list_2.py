from __future__ import annotations
from typing import Optional


class Node:
    data:int
    next:Optional[Node]


    def __init__(self,data:int,next:Optional[Node]):
        self.data=data
        self.next=next
    
    def __repr__(self) -> str:
        if self.next is None:
            return f"{self.data}-> None"
        else:
            return f"{self.data}->{self.next}"


def is_equal(a:Optional[Node],b:Optional[Node]):
    if a==None and b==None:
        return True
    elif a==None or b==None:
        return False
    elif a.data!=b.data:
        return False
    else:
        return is_equal(a.next,b.next)
    


a = Node(110, Node(111, Node(113,Node(114,None))))
b = Node(110, Node(111, Node(113,Node(115,None))))

print(is_equal(a, b))



