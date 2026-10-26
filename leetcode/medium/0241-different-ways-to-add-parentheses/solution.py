# T.C : O(n*2^n)
# S.C : O(2^n) The result vector stores all possible outcomes. The number of results is at most exponential in terms of the number of operators, so the space required to store the results is O(2^n).

class Solution:
    def solve(self, expression: str)-> list[int]:
        n = len(expression)
        result = []

        for i in range(0, n):
            ch = expression[i]

            if(ch == '+' or ch == '-' or ch == '*'):

                leftList = self.solve(expression[0: i])
                rightList = self.solve(expression[i + 1:])

                for x in leftList:
                    for y in rightList:

                        if(ch == '+'):
                            result.append(x + y)
                        elif(ch == '-'):
                            result.append(x - y)
                        else: 
                            result.append(x * y)

        if not result:
            result.append(int(expression))
        
        return result

    def diffWaysToCompute(self, expression: str) -> list[int]:
        return self.solve(expression)
        