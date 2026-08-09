class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {"".join(sorted(strs[0])): [strs[0]]}

        for x in range(1,len(strs)):
            myDict.setdefault("".join(sorted(strs[x])),[]).append(strs[x])

        return list(myDict.values())