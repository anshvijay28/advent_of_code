from collections import deque

def simulate(test_polymer):
    stack = deque()

    for char in test_polymer:
        if stack and abs(ord(char) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(char)
    return len(stack)

def solve(polymer):
    letters = [chr(ord('A') + i) for i in range(26)]
    res = float("inf")

    for letter in letters:
        # remove all instaces of letter in polymer (in O(n) as opposed to O(n^2))
        test_polymer = []
        for char in polymer:
            if char.upper() == letter:
                continue
            test_polymer.append(char)

        sim = simulate(test_polymer)        
        res = min(res, sim)

    return res


test = "dabAcCaCBAcCcaDA"
ids = "" # was really big, don't want to bloat file size for github

print(solve(ids))

# for part 2, brute force would be just doing this 26 times, (once for each letter)