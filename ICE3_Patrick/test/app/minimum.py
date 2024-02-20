class Minimum: # class minimum
    def find_min(self, nums): # def function, self and num as parameters
        if not nums:
            raise ValueError("Input list is empty") # if empty list, return this
        min_val = nums[0]
        for num in nums: # for loop, fining minimum value
            if not isinstance(num,(int)): # if instance is not an int, display is must be an int
                raise TypeError("Input must be an int")
            if num < min_val: # if value is an int, check if num < min val
                min_val = num # if num < min val, assign it to min_val
        return min_val