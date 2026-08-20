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
        # now we just need to read the integer up to before the delimiter, and ignore the delimeter, then take the # of char by the integer size, and store it into the returning list
        # make a new list
        result = []
        # while the s still has char
        counter = 0
        # we increment our counter by 1 

        # if it is #, take the char from s[0] to s[counter] to make it into integer, then take the s[counter + 1, counter + 1 + count + 1) 
        # remove all char from s[0] to s[counter + count + 2]
        # make the counter = 0
        while s:
            if s[counter] == "#":
                size = int(s[:counter])
                result.append(s[counter + 1: counter +1 + size ])
                s = s[counter + size + 1:]

                counter = 0
            else:
                counter = counter + 1

        return result



