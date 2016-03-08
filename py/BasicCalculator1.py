class Solution(object):
    def calcOps(self, a, b, ops):
      return a+b if ops == '+' else a-b
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
          return 0

        numvec, opsvec = [], []

        num = ''
        for c in s:
          if c.isdigit():
            num += c
          else:
            if num:
              tmp = int(num)
              numvec.append(tmp)
              num = ''
            if c == '(':
              numvec.append(c)
            elif c == ')':
              while len(numvec) > 0:
                n1 = numvec.pop()
                if n1 == '(':
                  break
                n2 = numvec.pop()
                if n2 == '(':
                  numvec.append(n1)
                  break
                if len(opsvec) > 0:
                  ops = opsvec.pop()
                  newnum = self.calcOps(n1, n2, ops)
                  numvec.append(newnum)
            elif c == '+' or c == '-':
              opsvec.append(c)

        if len(num) > 0:
            numvec.append(int(num))
        if len(opsvec) > 0 and len(numvec) > 0:
          for op in opsvec:
            n1 = numvec.pop()
            n2 = numvec.pop()
            newnum = self.calcOps(n1, n2, op)
            numvec.append(newnum)
          return numvec[0]
        else:
          return numvec[0]
