s = " abcdwrqowe"

for i in range(len(s)):
    for j in range(i + 1, len(s)):
        substring = s[i:j]
        print(substring)
