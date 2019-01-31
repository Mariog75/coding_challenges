def isunique ( str ):

    for i in range(len(str)):
        ch = str[i]
        for j in range(i+1, len(str)):
            if(ch == str[j]):
                return 0
    
    return 1

def main():
    print(isunique( "bb" ))

if __name__ == "__main__":
    main()

