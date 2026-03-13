class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for ch in s:

            if ch == "]":
                chars = ""
                while st and st[-1] != "[":
                    chars = st.pop() + chars
                st.pop()
                num = ""
                while st and st[-1].isdigit():
                    num =st.pop() + num
                st.append(chars  * int(num))
            else:
                st.append(ch)
        return "".join(st)
            



            