import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

def quickSort(array):
	quickSortHelper(array, 0, len(array) -1)
	return array

def quickSortHelper(array, startIdx, endIdx):
	if startIdx >= endIdx:
		return

	pivotIdx = startIdx
	leftIdx = startIdx + 1
	rightIdx = endIdx

	while leftIdx <= rightIdx:
		if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
			array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]
		if array[leftIdx] <= array[pivotIdx]:
			leftIdx += 1
		if array[rightIdx] >= array[pivotIdx]:
			rightIdx -= 1
	array[rightIdx], array[pivotIdx] = array[pivotIdx], array[rightIdx]
	leftSubarrayIsSmaller = (rightIdx - 1) - startIdx < endIdx - (rightIdx + 1)
	if leftSubarrayIsSmaller:
		quickSortHelper(array, startIdx, rightIdx-1)
		quickSortHelper(array, rightIdx+1, endIdx)
	else:
		quickSortHelper(array, rightIdx+1, endIdx)
		quickSortHelper(array, startIdx, rightIdx - 1)

for _ in range(int(input())):
	n = int(input())
	array = list(map(int, input().split()))
	print(quickSort(array))