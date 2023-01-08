class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_words = s.split()
        if len(pattern) != len(s_words):
            return False
        pattern_dict = {}
        s_dict = {}
        pattern_str = ''
        s_str = ''
        p_counter = 0
        s_counter = 0
        for i in range(len(pattern)):
            p_found = pattern_dict.get(pattern[i], None)
            s_found = s_dict.get(s_words[i], None)
            if not p_found:
                pattern_dict[pattern[i]] = str(p_counter)
                pattern_str += str(p_counter)
                p_counter += 1
            else:
                pattern_str += p_found
            if not s_found:
                s_dict[s_words[i]] = str(s_counter)
                s_str += str(s_counter)
                s_counter += 1
            else:
                s_str += s_found
        return s_str == pattern_str

obj = Solution()
print(obj.wordPattern("abba", "dog dog dog dog"))