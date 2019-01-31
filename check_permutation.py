#O(n^2)
def checkpermutation ( str1, str2 ):
    if(len(str1) != len(str2)):
        return 0
    result = 1
    for ch1 in str1:
        if(result == 0):
            return 0 
        for ch2 in str2:
            if(ch1 == ch2):
                result = 1
                break
            else:
                result = 0
    return 1
#O(nlogn) (Depending on sorting algorithm used)
def checkpermutationbetter ( str1, str2 ):
    if(len(str1) != len(str2)):
        return 0
    s1 = sorted(str1)
    s2 = sorted(str2)

    for i in range(0, len(str1), 1):
        if(s1[i] != s2[i]):
            return 0
    return 1

if __name__ == "__main__":
    print(checkpermutationbetter("blah", "hgab"))