import heapq

# Create an empty heap
heap = []

# Push three items into the heap
heapq.heappush(heap, ('V', 1))
heapq.heappush(heap, ('V', 3))
heapq.heappush(heap, ('V', 2))

# Display items in the heap
print("Items in the heap:")
for item in heap:
    print(item)

print("----------------------")

# Retrieve the smallest item from the heap without popping
print("The smallest item in the heap:")
print(heap[0])

print("----------------------")

# Pop and return the smallest item from the heap
print("Pop the smallest item in the heap:")
while heap:
    smallest = heapq.heappop(heap)
    print(smallest)
