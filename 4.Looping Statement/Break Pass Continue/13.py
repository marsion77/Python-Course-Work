# 13.Skip the first half of a list, process the second half, use pass for future.
numbers = [9,4,6,2,4,6,7,9] 

first_half = len(numbers) // 2  

for i in range(len(numbers)):
    if i < first_half: 
        pass      
        print(numbers[i])
