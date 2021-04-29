def calculate_hapiness(nums, A, B):
  happiness = 0

  for num in nums:
    if num in A:
      happiness += 1
    elif num in B:
      happiness -= 1

  return happiness

def convert_to_int(nums):
  return [int(i) for i in nums]

n, m = convert_to_int(input().split(' '))
nums = convert_to_int(input().split(' '))
A = set(convert_to_int(input().split(' ')))
B = set(convert_to_int(input().split(' ')))

if len(nums) == n or len(A) == len(B) == m: 
  print(calculate_hapiness(nums, A, B))

else:
  print('[-] Please, verified size of arrays')