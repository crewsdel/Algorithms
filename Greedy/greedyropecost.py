import heapq
def greedyropecost(A):
    heapq.heapify(A)
    cost = 0
    while len(A) > 1:
        min1 = heapq.heappop(A)
        min2 = heapq.heappop(A)
        combined = min1 + min2
        cost += combined
        heapq.heappush(A, combined)
    
    print(cost)
    return cost
    
A = [6, 9, 1, 2]
greedyropecost(A)