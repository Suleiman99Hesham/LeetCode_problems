class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        groups = {}
        for i in range(len(s1)):
            added = False
            merging_keys = []
            s1_i = s1[i]
            s2_i = s2[i]
            for key, group in groups.items():
                if s1_i in group or s2_i in group:
                    group.update(s1_i, s2_i)
                    merging_keys.append(key)
                    added = True
            if not added:
                groups[min(s1[i],s2[i])] = {s1[i], s2[i]}
            else:
                temp = {'temp_key' : set()}
                for key in merging_keys:
                    temp['temp_key'].update(groups[key])
                    del groups[key]
                groups[min(temp['temp_key'])] = temp['temp_key']
        out = ''
        for i in baseStr:
            found = False
            for key, group in groups.items():
                if i in group:
                    out += key
                    found = True
                    break
            if not found:
                out += i
        return out
        
obj = Solution()
print(obj.smallestEquivalentString('parker', 'morris', 'parser'))
print(obj.smallestEquivalentString('adkbbjigibahbjjgdkkiighagijfdfjkcdaakdkbjcidgjjfga', 'hbfahdikgchbkigebgjghdhadaikhccjejafkaibdgffichcbb', 'hotutsrhanyvpzusrnsxbncpqhnxrvgmbrpcbhheqotadyzfyl'))