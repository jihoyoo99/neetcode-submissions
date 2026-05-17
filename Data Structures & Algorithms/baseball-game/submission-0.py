class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = []
        for i in range(len(operations)):
            try: 
                x = int(operations[i])
            except ValueError:
                if operations[i] == "+":
                    plus = rec[-1] + rec[-2]
                    rec.append(plus)
                elif operations[i] == "D":
                    double = rec[-1]*2
                    rec.append(double)
                elif operations[i] == "C":
                    rec.pop()
            else: 
                rec.append(x)
        res = sum(rec)
        return res
        

