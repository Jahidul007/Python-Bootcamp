class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        my_list = nums
        another_list = nums
        my_list.extend(another_list)
        print(my_list)
        return my_list
