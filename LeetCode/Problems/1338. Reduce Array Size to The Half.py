import collections
class Solution:
    def minSetSize(self, arr):
        arrLen = len(arr)
        counts = collections.Counter(arr).most_common()

        list1 = []
        tmpcnt = 0
        for item in counts:
            if tmpcnt >= int(arrLen/2):
                break
            else:
                tmpcnt += item[1]
                list1.append(item[0])

        return len(list1)