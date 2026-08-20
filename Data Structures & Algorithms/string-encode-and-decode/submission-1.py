class Solution:

    def encode(self, strs: List[str]) -> str:
        # We can't just put all of the strings together since we wouldnt be able to decode it back
        # we need some way knowing how to split the string to decode it
        # we can't just put a delimeter between each word because the word itself can contain that delimeter
        # we can count the len(str) for each word and put it in the front, then add a delimeter to the end of the Integer

        result = ""
        for word in strs:
            length = len(word)
            result = result + str(length) + "#" + str(word)

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            result.append(s[j+1: j+1+length])

            i = j + 1 + length

        return result



