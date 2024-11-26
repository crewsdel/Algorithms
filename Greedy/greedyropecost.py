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
