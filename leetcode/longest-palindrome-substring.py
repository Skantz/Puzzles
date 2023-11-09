class Solution:
    def is_palindrome(self, s : str) -> bool:
        n = len(s)
        for i in range(0, len(s)//2):
            if (s[i] != s[n - i - 1]):
                return False
        return True

    def longestPalindrome(self, s: str) -> str:
        odds = [(i, i) for i, _ in enumerate(s)]
        evens = [(i, i + 1) for i in range(len(s) - 1) if s[i] == s[i + 1]]
        i = 1
        j = 2
        n = len(s)
        s_odds = []
        s_evens = []
        cont = True
        while cont:
            cont = False
            s_odds = [e for e in odds]
            s_evens = [e for e in evens]
            odds = []
            evens = []
            for (e1, e2) in s_odds:
                if e1 > 0 and e2 < n - 1:
                    if s[e1 - 1] == s[e2 + 1]:
                        cont = True
                        odds.append((e1 - 1, e2 + 1))
            for (e1, e2) in s_evens:
                if e1 > 0 and e2 < n - 1:
                    if s[e1 - 1] == s[e2 + 1]:
                        cont = True
                        evens.append((e1 - 1, e2 + 1))
        if s_odds and s_evens:
            if len(s_odds[0]) > len(s_evens[0]):
                return s[s_odds[0][0]:s_odds[0][1] + 1]
            else:
                return s[s_evens[0][0]:s_evens[0][1] + 1]
        if s_evens:
            return s[s_evens[0][0]:s_evens[0][1] + 1]
        return s[s_odds[0][0]:s_odds[0][1] + 1]

    def longest_palindrome_naive(self, s: str) -> str:
        maxx = 0
        maxp = ""
        n = len(s)
        if n <= 1:
            return s
        for w in range(1, len(s) + 1):
            for i in range(0, n - w + 1):
                isp = self.is_palindrome(s[i:i + w])
                if isp:
                    maxx = max(maxx, w)
                    maxp = s[i:i + w]
        return maxp
