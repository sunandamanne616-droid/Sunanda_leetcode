class Solution(object):
    def rearrangeArray(self, arr):
        pos_arr=[]
        neg_arr=[]
        for i in arr:
            if i>0:
                pos_arr.append(i)
            else:
                neg_arr.append(i)
        pos=0
        neg=0
        for i in range(0,len(arr)):
            if i%2==0:
                arr[i]=pos_arr[pos]
                pos+=1
            else:
                arr[i]=neg_arr[neg]
                neg+=1
        return arr


