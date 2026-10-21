class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_hash = {}
        for num in nums:
            if num in count_hash:
                count_hash[num] += 1
            else:
                count_hash[num] = 1
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Step 3: Map the data directly to the index position
        for num, count in count_hash.items():
            buckets[count].append(num)
            
        # Step 4: Extract the winners without sorting
        out_lst = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                out_lst.append(num)
                if len(out_lst) == k:
                    return out_lst
        