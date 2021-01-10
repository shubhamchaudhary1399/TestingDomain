import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

def binarySearch(array, target):
	left = 0
	right = len(array) - 1
	while left <= right:
		middle = left + (right-left)//2
		potentialMatch = array[middle]
		if target == potentialMatch:
			return middle
		elif target < potentialMatch:
			right = middle - 1
		else:
			left = middle + 1
	return -1

for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	print(binarySearch(arr, n))
