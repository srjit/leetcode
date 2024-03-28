from collections import Counter
import heapq

class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:

        # count of each tasks
        counts = Counter(tasks)
        heap = [-1 * cnt for cnt in counts]
        heapq.heapify(heap)

        # queue
        time = 0
        q = deque()

        while heap or q:

            time += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt < 0:
                    # task with items cnt can be executed only at T = time+n
                    q.append([cnt, time+n])
                
                if q and q[0][1] == time:
                    heapq.heappush(heap, q.popleft()[0])
        
        return time





