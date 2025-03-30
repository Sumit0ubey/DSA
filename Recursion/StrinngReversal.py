from helperFunction import substring

def reverseString(String:str) -> str:
    if String == "":
        return ""
    return reverseString(substring(String, 1)) + String[0]

print(reverseString("hello"))
print(reverseString("sumit"))