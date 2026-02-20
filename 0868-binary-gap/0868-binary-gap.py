class Solution:
    def binaryGap(self, n: int) -> int:
        binary = list(bin(n)[2:])
        indices=[]
        for i in range(len(binary)):
            if (binary[i]=='1'):
                indices.append(i)
        distance=0
        for i in range(1,len(indices)):
            if (indices[i]-indices[i-1]>distance):
                distance=indices[i]-indices[i-1]
        return distance