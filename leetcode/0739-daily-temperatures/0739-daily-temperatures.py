class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        temp= {}
        res = [0] * len(temperatures)
        for t in range(len(temperatures)):
            curr = temperatures[t]
            while st and temperatures[st[-1]] < curr:
                val = st.pop()
                temp[val] = t - val
            st.append(t)
        return [temp[x] if x in temp else 0 for x in range(len(temperatures))]