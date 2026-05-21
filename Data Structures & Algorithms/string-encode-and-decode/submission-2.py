class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        if len(s) == 0:
            return res
        else:
            sep = s.find("#")

            leng = int(s[:sep])

            res.append(s[sep+1:leng+sep+1])
   
            return res + self.decode(s[leng+sep+1:])

