class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        most_occur=0
        answer=0
        for number, count in freq.items():
            if count > most_occur:
                most_occur = count
                answer = number

        return answer

        
        

        
