class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        arr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
               ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
               ".--","-..-","-.--","--.."]
        f = lambda x: "".join([arr[ord(e) - 97] for e in x])
        s = {f(w) for w in words}
        return len(s)
