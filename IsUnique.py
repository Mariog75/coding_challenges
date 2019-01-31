#O(n^2)
def isunique ( str ):

    for i in range(len(str)):
        ch = str[i]
        for j in range(i+1, len(str)):
            if(ch == str[j]):
                return 0
    
    return 1
#O(n)
def isuniquebetter ( str ):
    if(len(str) > 128):
        return 0
    arr = [None] * 128

    for ch in str:
        if(arr[ord(ch)] != None):
            return 0
        else:
            arr[ord(ch)] = 1
    
    return 1


def main():
    print(isuniquebetter( "badrtyui" ))

if __name__ == "__main__":
    main()

