'''
這題要根據學生 report 的內容計分，回傳分數最高的前 k 個 student id。

計分規則：
- 出現 positive feedback word：+3
- 出現 negative feedback word：-1
- 其他 word：0

排序規則：
1. 分數高的排前面
2. 分數相同時，student id 小的排前面

核心想法：
positive_feedback 和 negative_feedback 都轉成 set，讓查詢單字是否存在是 O(1)。
每份 report 用空白切成 words，逐字累加分數。

最後排序時使用 key = (-score, student_id)：
- -score 讓分數高的排前面
- student_id 讓 id 小的排前面

時間複雜度：O(total_words + n log n)
空間複雜度：O(p + q + n)
'''

class Solution:
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        positive = set(positive_feedback)
        negative = set(negative_feedback)
        scores = []

        for text, sid in zip(report, student_id):
            score = 0

            for word in text.split():
                if word in positive:
                    score += 3
                elif word in negative:
                    score -= 1

            scores.append((score, sid))

        scores.sort(key=lambda item: (-item[0], item[1]))
        return [sid for _, sid in scores[:k]]


s = Solution()
print(s.topStudents(
    ["smart", "brilliant", "studious"],
    ["not"],
    ["this student is studious", "the student is smart"],
    [1, 2],
    2
))
print(s.topStudents(
    ["smart", "brilliant", "studious"],
    ["not"],
    ["this student is not studious", "the student is smart"],
    [1, 2],
    2
))
