class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = {}
        for c in magazine:
            if c not in hash_map:
                hash_map[c] = 1
            else:
                hash_map[c] += 1
        # print(hash_map)
        for c in ransomNote:
            if c not in hash_map or hash_map[c] == 0:
                return False
            hash_map[c] -= 1
        return True
        