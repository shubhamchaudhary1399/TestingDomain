import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def bubbleSort(array):
	for i in range(len(array)):
		flag = False
		for j in range(len(array)-i-1):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
				flag = True
		if flag == False:
			break
	return array

for _ in range(int(input())):
	n = int(input())
	array = list(map(int, input().strip().split()))
	# print(n, array)
	print(bubbleSort(array))