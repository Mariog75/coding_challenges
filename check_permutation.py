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


def main():
    print(checkpermutation( "badab", "daba" ))

if __name__ == "__main__":
    main()