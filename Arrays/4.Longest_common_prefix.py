import os
os.system('cls')

def longestCommonPrefix(strs):

    prefix = strs[0]

    for i in range(1, len(strs)):
        while not strs[i].startswith(prefix):

            prefix = prefix[:-1]

            if prefix == "":
                return ""

    return prefix

strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))