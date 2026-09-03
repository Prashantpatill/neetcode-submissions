class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
      n = len(arr)
      ans = [0]*n
      for i in range(n):
        rm=-1
        for j in range (i+1,n):
            rm = max(rm,arr[j])
        ans[i]=rm
      return ans