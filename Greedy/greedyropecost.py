import heapq
def greedyropecost(A):
    heapq.heapify(A)  # Turn our input array into a min-heap
    cost = 0 #Initialize our cost to 0
    while len(A) > 1: # Check the size of the heap
        min1 = heapq.heappop(A) # Remove the first minimum element
        min2 = heapq.heappop(A) # " " second " "
        combined = min1 + min2 # Combine the two minimum elements together
        cost += combined # Update the total cost
        heapq.heappush(A, combined) # Add the new candy and its length back to the heap
    
    print(cost)
    return cost
    
A = [6, 9, 1, 2] # Change the array values to whatever you like
greedyropecost(A) # Call the function

'''
Efficiency analysis: 
This algorithm has a runtime of O(n log n) and occupies O(n) additional space. 
Each iteration extracts the two minimums (O(log n) because I used a heap) and combines and re-adds the value to the heap (also O(log n)). 
Therefore, each iteration takes O(log n) + O(log n) = O(log n). 
The while loop will iterate n – 1 times because we remove 1 item from the heap during each iteration and it terminates when the size of the heap is no longer greater than 1. 
So, the total runtime cost is O((n – 1) * log n) = O(n log n). The algorithm requires O(n) additional space because we store n elements in our heap at the beginning of our program.
'''
