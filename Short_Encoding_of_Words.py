class Solution:

    def find(self, input_str, search_str):
        length = len(search_str)
        index = 0
        while index < length:
            i = search_str.find(input_str, index)
            if i == -1:
                return -1
            if search_str[i+len(input_str)] == '#':
                return i
            index = i + 1
        return -1

    def minimumLengthEncoding(self, words) -> int:
        if len(words) == 1:
            return len(words[0]) + 1

        sorted_words = sorted(words, key=lambda x: len(x), reverse=True)
        reference = ''
        indices = []
        for word in sorted_words:
            found = self.find(word, reference)
            if found != -1:
                indices.append(found)
            else:
                if reference == '':
                    indices.append(0)
                else:
                    indices.append(len(reference))
                reference += word + '#'
        return len(reference)
            

obj = Solution()
print(obj.minimumLengthEncoding(["time","me","bell"]))
print(obj.minimumLengthEncoding(["t"]))
print(obj.minimumLengthEncoding(["me","time"]))
print(obj.minimumLengthEncoding(["feipyxx", "mine", "e"]))
print(obj.minimumLengthEncoding(["mine", "feipyxx", "e"]))
print(obj.minimumLengthEncoding(["feipyxx","e"]))