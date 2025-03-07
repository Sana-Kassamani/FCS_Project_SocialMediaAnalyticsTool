# static class containing helping methods

class Utilities:
    @staticmethod
    def subtract(a,b):
        #O(1)
        return a-b 
    
    @staticmethod
    def compareWeights(node1,node2):
        #O(1)
        return Utilities.subtract(node1.weight,node2.weight)



    @staticmethod
    def mergeSort(items,low,high, cmp):
        #O(NlogN) N being length of items
        if low< high:
            mid = (low+high)//2
            Utilities.mergeSort(items,low,mid,cmp)
            Utilities.mergeSort(items,mid+1,high,cmp)
            Utilities.merge(items,low,mid,high,cmp)


    @staticmethod
    def merge(items,low,mid,high,cmp):
        #O(N) N being length of items
        left_size=mid-low+1
        right_size=high-mid

        left=[0]*left_size
        right=[0]*right_size

        for i in range(left_size):
            left[i]=items[low+i]
        for j in range(right_size):
            right[j]=items[mid+1+j]

        left_index= right_index=0
        merge_index=low

        while left_index < left_size and right_index < right_size:
            if cmp(left[left_index],right[right_index]) <=0:
                items[merge_index]=left[left_index]
                left_index+=1
            else:
                items[merge_index]=right[right_index]
                right_index+=1
            merge_index+=1
        
        while left_index < left_size:
            items[merge_index]=left[left_index]
            left_index+=1
            merge_index+=1

        while right_index < right_size:
            items[merge_index]=right[right_index]
            right_index+=1
            merge_index+=1


        