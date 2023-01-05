from collections import Counter
class Solution:
    def minimumRounds(self, tasks) -> int:
        tasks_grouped = Counter(tasks)
        myKeys = list(tasks_grouped.keys())
        myKeys.sort()
        tasks_grouped_sorted = {i: tasks_grouped[i] for i in myKeys}
        count = 0
        for k, v in tasks_grouped_sorted.items():
            if v == 1:
                return -1
            reminder_3 = v % 3
            if reminder_3 == 0:
                count += (v // 3)
            else:
                count += (v // 3) + 1
        return count