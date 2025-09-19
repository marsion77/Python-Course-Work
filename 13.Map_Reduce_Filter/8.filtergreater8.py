# my_list = [1,2,3,4,5,12,13,14,14]
# great_8 = list(filter(lambda x: x >8,my_list ))
# print(great_8)


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    # print(result)
  else:
    result = 0
  return result

print(tri_recursion(6))
