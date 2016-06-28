import collections

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        store = []
        resultSet = set()

        count = collections.Counter(s)

        for n in s:
            count[n] -= 1
            if n in resultSet:
                continue
            while len(store) > 0 and store[-1] > n and count[store[-1]] > 0:
                resultSet.remove(store.pop())
            resultSet.add(n)
            store.append(n)

        return ''.join(store)
