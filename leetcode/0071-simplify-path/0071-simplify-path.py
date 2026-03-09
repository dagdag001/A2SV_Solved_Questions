class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        st= []
        for i in path:
            if i == "..":
                if st:
                    st.pop()
            elif i == "." or i == "" :
                continue
            else:
                st.append(i)
        return '/' + "/".join(st)

        
