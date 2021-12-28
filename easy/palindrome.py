def isPalindrome(s):
    return s == s[::-1]


# ծրագրավորում
s = str(input("Ներմուծիր լատինատառ բառը։ "))
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")