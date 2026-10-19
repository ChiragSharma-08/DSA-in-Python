import heapq

hospital = []
# lower number = higher priority
heapq.heappush(hospital, (3,"Broken finger"))
heapq.heappush(hospital, (1,"Broken Finger"))
heapq.heappush(hospital, (2,"High Feaver"))
heapq.heappush(hospital, (1,"Hart Attack"))

print(heapq.heappop(hospital))
print(heapq.heappop(hospital))
print(heapq.heappop(hospital))
print(heapq.heappop(hospital))