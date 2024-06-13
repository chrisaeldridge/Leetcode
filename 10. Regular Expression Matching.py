class Solution:
    # BOTTOM-UP Dynamic Programming
    def isMatchBU(self, s: str, p: str) -> bool:
        cache = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        cache[len(s)][len(p)] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                match = i < len(s) and (s[i] == p[j] or p[j] == ".")

                if (j + 1) < len(p) and p[j + 1] == "*":
                    cache[i][j] = cache[i][j + 2]
                    if match:
                        cache[i][j] = cache[i + 1][j] or cache[i][j]
                elif match:
                    cache[i][j] = cache[i + 1][j + 1]

        return cache[0][0]


    # TOP DOWN MEMOIZATION
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            # we've iterated to the end of the string and the pattern, so we've found a match
            if i >= len(s) and j >= len(p):
                return True
            # past the end of the pattern and did not find a match
            if j >= len(p):
                return False

            # check if this pattern character matches this string character, also make sure string char in bounds 
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            
            # if next pattern char is a wildcard then recursive call both with and without the wildcard
            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[(i, j)] = ( dfs(i, j + 2) or            # dont use *
                                (match and dfs(i + 1, j) ) )  # use *
                return cache[(i, j)]
            
            # if we found a match then increment the string and pattern and recursive call again
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            
            # we did not find a match
            cache[(i, j)] = False
            return False

        return dfs(0, 0)

print(f'answer = {Solution().isMatch("aab","a*aab*")}')
print(f'answer = {Solution().isMatch("aaab.ght","a*")}')
print(f'answer = {Solution().isMatch("ab",".*c")}')
print(f'answer = {Solution().isMatch("aaa","a*a")}')
print(f'answer = {Solution().isMatch("bbbba",".*a*a")}')
print(f'answer = {Solution().isMatch("aaabaaa","a*b*a*")}')