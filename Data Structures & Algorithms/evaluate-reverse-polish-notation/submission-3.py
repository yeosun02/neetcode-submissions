class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = []
        for op in tokens:
            if op not in ['+', '-', '*', '/']:
                ops.append(int(op))
                continue

            op2 = ops.pop()
            if op == '+':
                ops[-1] += op2
            elif op == '-':
                ops[-1] -= op2
            elif op == '*':
                ops[-1] *= op2
            else:
                ops[-1] = int(ops[-1] / op2)
        
        return ops[-1]