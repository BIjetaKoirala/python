#list
nums = [ 1, 2, 4, 5, 6]  # array of numbers 
nums[0] , nums[4] = nums[4] , nums[0]
print(nums[ -1])
print(nums[2:])
print(nums[:2])
nums.append(9)
print(nums)
nums.pop()
print(nums)


# tuples 

#movies = (
 #   "intersteller",
  #  "the prestige",
   # "eternal sunsine of the spotless mind",
    #"memento",
#)
#movies [0], movies [-1] = movies[-1], movies[0]
#print(movies)

#set
movies = {
    "intersteller",
    "intersteller",
    "the prestige",
    "eternal sunsine of the spotless mind",
    "memento",
}
print(movies)