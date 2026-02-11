class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        minHeap = []

        for num, count in freq.items():

            heapq.heappush(minHeap, (count, num))

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        res = []

        while minHeap:
            res.append(heapq.heappop(minHeap)[1])

        return res