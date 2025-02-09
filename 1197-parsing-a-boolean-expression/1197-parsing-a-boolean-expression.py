class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        def max_depth_search(expression):
            max_depth = 0
            depth = 0
            for e in expression:
                if e == '(':
                    depth += 1
                    max_depth = max(depth, max_depth)
                if e ==')':
                    depth -= 1
            return max_depth
        
        def translation(string):
            exp = []
            for c in string:
                if c == 'f':
                    exp.append(0)
                elif c == 't':
                    exp.append(1)
                elif c == ',':
                    pass                    
                else:
                    exp.append(c)
            return exp
        
        def inner_evaluation(operator, inner):
            #print(operator, inner)
            #return 0
            if operator == '!':
                if len(inner) > 1:
                    return -1
                return 1 - inner[0]
            elif operator == '|':
                if sum(inner) > 0:
                    return 1
                else:
                    return 0
                return -1
            elif operator == '&':
                p = 1
                for val in inner:
                    p *= val
                return p


        max_depth = max_depth_search(expression)
        #print(max_depth)
        exp = translation(expression)
        #print(exp)

        
        while max_depth >= 0 and len(exp) > 1:
            p1 = 0
            depth = 0
            while p1 < len(exp):
                if exp[p1] == '(':
                    depth += 1
                    #print(depth, exp[:p1+1])
                elif exp[p1] == ')':
                    depth -= 1
                if depth == max_depth:
                    p2 = p1 + 1
                    while exp[p2] != ')':
                        p2 += 1
                    #print('______________', p1, p2, exp[p1-1], exp[p1+1:p2] )
                    result = inner_evaluation(exp[p1-1], exp[p1+1:p2])
                    exp[p1-1:p2+1] = [result]
                    #print(exp)
                    depth -= 1
                    p1 -= 1
                if len(exp) == 1:
                    return bool(exp[0])
                p1 += 1
            max_depth -= 1
        return bool(exp[0])
        
        