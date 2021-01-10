import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

# O(N^2) time | O(1) space
for _ in range(int(input())):
	n = int(input())
	array = list(map(int, input().strip().split()))
	for i in range(len(array) - 1):
		smallestIdx = i
		for j in range(i+1, len(array)):
			if array[smallestIdx] > array[j]:
				smallestIdx = j
		array[smallestIdx], array[i] = array[i], array[smallestIdx]
	print(array)
