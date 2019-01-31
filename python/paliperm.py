def paliperm( str ):
    str1 = ''.join(str.lower().replace(" ", ""))
    sortedstr = ''.join(sorted(str1))
    print(sortedstr)
    for i in range(0, len(sortedstr), 2):
        print(sortedstr[i])
        print(sortedstr[i+1])
        if(sortedstr[i].lower() != sortedstr[i+1].lower()):
            return 0
    return 1

if __name__ == "__main__":
    print(paliperm("Tact Coa"))