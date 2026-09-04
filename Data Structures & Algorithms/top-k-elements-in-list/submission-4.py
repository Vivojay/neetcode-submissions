class Solution:
    def children(self, heap: List[tuple[int, int]], n: int) -> List[Optional[int], ...]:
        i = 2*n + 1
        c = [None, None]
        if i + 1 < len(heap):
            c[1] = i + 1
        if i < len(heap):
            c[0] = i
        return c

    def parent(self, n: int) -> Optional[int]:
        if n == 0:
            return None
        return (n - 1) // 2

    def heapify_up(self, heap: List[tuple[int, int]], n: int):
        p = self.parent(n)
        while p is not None and heap[p][1] < heap[n][1]:
            heap[p], heap[n] = heap[n], heap[p]
            n = p
            p = self.parent(n)
    
    def heapify_down(self, heap: List[tuple[int, int]], n: int):
        while True:
            l, r = self.children(heap, n)
            largest = n
            if l is not None and heap[l][1] > heap[largest][1]:
                largest = l
            if r is not None and heap[r][1] > heap[largest][1]:
                largest = r
            if largest == n:
                break
            heap[n], heap[largest] = heap[largest], heap[n]
            n = largest

    def insert(self, heap: List[tuple[int, int]], val: tuple[int, int]):
        heap.append(val)
        self.heapify_up(heap, len(heap) - 1)
    
    def pop(self, heap: List[tuple[int, int]]) -> tuple[int, int]:
        top = heap[0]
        # print('top', top)
        # swap first(top) and last
        heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
        # delete last element
        del heap[len(heap)-1]
        # heapify down
        self.heapify_down(heap, 0)
        return top

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {} # k
        for i in range(len(nums)):
            if nums[i] in d: d[nums[i]] += 1
            else: d[nums[i]] = 1

        # print(d)

        heap = []
        for i in d.items():
            self.insert(heap, i)

        out = []
        for _ in range(k):
            a = self.pop(heap)
            out.append(a)
            # print(a)

        # print(out)

        # r = {}
        # for i in d:
        #     if d[i] in r:
        #         r[d[i]].append(i)
        #     else:
        #         r[d[i]] = [i]

        # l = list(r.keys())
        # print(l, r)
        return [i[0] for i in out]


# [1, 2, 8, 3], 8 -> [8, 2, 1, 3]
# [8, [2, 1, 3]], 3 -> [8, 3, 1, 2]
# [8, 3, 1, 2], 2 -> [8, 3, 2, 1]
