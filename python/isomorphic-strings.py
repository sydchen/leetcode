class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 長度不同必定不可能同構
        if len(s) != len(t):
            return False

        map_s_t = {}
        map_t_s = {}

        for ch_s, ch_t in zip(s, t):
            # 檢查 s->t 映射
            if ch_s in map_s_t:
                if map_s_t[ch_s] != ch_t:
                    return False
            else:
                map_s_t[ch_s] = ch_t

            # 檢查 t->s 映射
            if ch_t in map_t_s:
                if map_t_s[ch_t] != ch_s:
                    return False
            else:
                map_t_s[ch_t] = ch_s

        return True

sol = Solution()

print(sol.isIsomorphic("egg", "add"))    # True  (e→a, g→d)
print(sol.isIsomorphic("foo", "bar"))    # False (f→b OK, o→a then o→r 衝突)
print(sol.isIsomorphic("paper", "title"))# True  (p→t, a→i, p→t, e→l, r→e)

