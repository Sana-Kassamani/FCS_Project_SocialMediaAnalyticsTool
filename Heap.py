# class Heap definition
# this class is useful in implementing dijkstra's algorithm in Network class
from Node import Node


class Heap:
    
    def __init__(self):
        self.size=0
        self.max_size=10
        self.list=[None]*(self.max_size+1)
        self.list[0]=-1

    def extendHeap(self):
        #O(N), N being self.max_size
        extended=[None]*(self.max_size+1)
        self.max_size *= 2
        self.list.extend(extended)

    def getParentIndex(self,index):
        #O(1)
        return index // 2
    
    def getLeftChildIndex(self,index):
        #O(1)
        return index * 2
    
    def getRightChildIndex(self,index):
        #O(1)
        return (index * 2) + 1
    
    def percolateUp(self,index):
        #O(logN), N being size of heap
        while index > 1 and self.list[index].weight < self.list[self.getParentIndex(index)].weight:
            parent_index=self.getParentIndex(index)
            self.list[index], self.list[parent_index]= self.list[parent_index],self.list[index]
            index = parent_index

    def percolateDown(self,index):
        #O(logN), N being size of heap
        while self.getLeftChildIndex(index) <= self.size :
            childIndex= self.getLeftChildIndex(index)
            if self.getRightChildIndex(index) <= self.size and self.list[self.getRightChildIndex(index)].weight < self.list[childIndex].weight:
                childIndex=self.getRightChildIndex(index)
            if self.list[childIndex].weight < self.list[index].weight:
                self.list[index],self.list[childIndex]=self.list[childIndex],self.list[index]
                index = childIndex
            else:
                index = self.size           




    def heapify(self,list):
        #O(N), N being size of heap
        self.size=len(list)
        while self.size >= self.max_size:
            self.extendHeap()

        for i in range(len(list)):
            self.list[i+1]=list[i]
        
        for index in range((self.size // 2),0,-1):
            self.percolateDown(index)

    def enqueue(self,node):
        #O(logN), N being size of heap
        if self.size >= self.max_size +1:
            self.extendHeap()
        self.size+=1
        self.list[self.size]=node
        self.percolateUp(self.size)
        print("added ", node.user.name,"to heap")

    def removeMin(self):
        #O(logN), N being size of heap
        if not self.size:
            print("heap is empty")
            return
        minimum = self.list[1]
        self.list[1]=self.list[self.size]
        self.size-=1
        self.percolateDown(1)
        return minimum
    
    def isEmpty(self):
        #O(1)
        return self.size ==0
    
    def includesUser(self,user):
        #O(N), N being size of heap
        for i in range(1,self.size+1):
            if self.list[i].user.id == user.id:
                return self.list[i], i
        return None,None

    def displayNodes(self):
        #O(N), N being size of heap
        if not self.size:
            print("Heap is empty!")
            return
        for i in range(1,self.size+1):
            curr= self.list[i]
            print("(",curr.user.name,",", curr.user.id,",",curr.weight,")" , end=" -> ")

        print('\n')

    def changeWeight(self,index,weight):
        #O(logN), N being size of heap
        self.list[index].weight=weight
        self.percolateUp(index)
        