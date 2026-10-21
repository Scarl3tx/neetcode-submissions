class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hash = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in anagram_hash:
                anagram_hash[sorted_string] = [string]
            else:
                anagram_hash[sorted_string].append(string)
        return [v for k,v in anagram_hash.items()]
