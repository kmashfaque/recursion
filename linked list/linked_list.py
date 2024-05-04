from __future__ import annotations
from typing import Optional


class Node:
    data:int
    next: Optional[Node]

    def __init__(self,data:int,next:Optional[Node]):
        self.data=data
        self.next=next


def count(head:Optional[Node])->int:
    if head is None:
        return 0
    
    else:
        after_me=count(head.next)
        return after_me+1

n0=Node(21,None)
n1=Node(22,n0)
n2=Node(23,n1)
n3=Node(24,n2)
n4=Node(22,n3)
print(count(n3))

