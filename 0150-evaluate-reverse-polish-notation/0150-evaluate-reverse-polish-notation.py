class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in tokens:
            if i not in ["+", "-", "*", "/"]:
                st.append(int(i))
            else:
                b = st.pop()
                a = st.pop()
                match(i):
                    case '+':
                        st.append(a+b)
                    case '-':
                        st.append(a-b)
                    case '*':
                        st.append(a*b)
                    case '/':
                        st.append(int(a/b))
        return st.pop()