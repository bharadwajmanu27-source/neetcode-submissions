class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        freq1={}
        freq2={}

        for i in nums1:
            if i in freq1:
                freq1[i]+=1
            else:
                freq1[i]=1

        for i in nums2:
            if i in freq2:
                freq2[i]+=1
            else:
                freq2[i]=1


        common=[]
        for i in freq1:
            if i in freq2:
                common.append(i)

        return common
