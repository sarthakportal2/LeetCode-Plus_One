class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):#iterating till digit's length 
            if digits[i]==9:digits[i]=0#assigning digits[0] val and 9th index val pos and digits
            else:digits[i]=digits[i]+1;return digits#printing the incremented digits[ndx]
        return [1]+digits#printing digit's 2nd th idx pos
