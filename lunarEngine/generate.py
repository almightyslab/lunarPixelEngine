def cls():  
    print("\n" * 100)  

def draw():
    try:
        sizeofmap = int(input("Enter Size: "))
    except:
        import sys
        sys.exit("Must be int")
    
    filleduni = "██"
    unfilleduni = "░░"
    
    maprangesize = sizeofmap * sizeofmap
    
    result = {}
    resultshow = ""
    
    for i in range(maprangesize):
        cls()
        i += 1
        print(resultshow)
        inputx = input("For put enter 1 for blank press 2: ")
        if inputx == "1":
            result[i] = True
            resultshow = resultshow + filleduni
            if i%sizeofmap==0:
                resultshow = resultshow+"\n"
        elif inputx == "2":
            result[i] = False
            resultshow = resultshow + unfilleduni
            if i%sizeofmap==0:
                resultshow = resultshow+"\n"
        else:
            while True:
                cls()
                print(resultshow)
                inputx = input("For put enter 1 for blank press 2: ")
                if inputx == "1" or "2":
                    break
            if inputx == "1":
                result[i] = True
                resultshow = resultshow + filleduni
                if i%sizeofmap==0:
                    resultshow = resultshow+"\n"
            elif inputx == "2":
                result[i] = False
                resultshow = resultshow + unfilleduni
                if i%sizeofmap==0:
                    resultshow = resultshow+"\n"
    
    cls()
    print(resultshow)
    print(str(result))