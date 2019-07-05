
def find(List):

    lf = []
    first = List[4][0]
    first = first.split(',')

    for i in range(len(first)):
        if first[i][0] == "-":
            lf.append(first[i][2 : ])
            break

    last = List[-1][0]
    last = last.split(',')

    for i in range(len(last)):
        if last[i][0] == "*":
            lf.append(last[i][1:])
            break

    return lf

def stack(stack):
    if stack:
        return stack[-1]

def process(File):
    input = []
    for line in File:
        line = line.split("\n")
        input.append(line)

    for i in range(len(input)):
        if input[i][-1] == '':
            del input[i][-1]
    return input

def show(Start , _stack , _temp , stringIn):
    Stack =[_temp]

    for i in range(1,len(stringIn)):
        Stack.append(str(stringIn[0 : i] + "(" + Start + _stack[i] + Start +  ")" + _temp))

    Stack.append(stringIn + _temp)
    Stack.append(stringIn)
    return Stack

def main():
    input_file = open("input.txt", 'r')
    pro = process(input_file)
    found = find(pro)

    Start = found[0]

    last = found[1]

    Grammar = []
    for i in range(4,len(pro)):
        Grammar.append(pro[i])

    f_grammar = []
    for i in range(len(Grammar)):
        f_grammar.append(Grammar[i][0])

    
    Grammar = [s.replace('->', '') for s in f_grammar]
    Grammar = [s.replace('_', '') for s in Grammar]
    Grammar = [s.replace('*', '') for s in Grammar]
  

    _temp = Grammar[-1]
    _temp = _temp.split(",")
    _temp = "(" + _temp[0] + _temp[2] + _temp[4] + ")"


    Stack = ["$"]
    stringIn = input("string?")

    _stack = []
    length  = len(Grammar)

    for i in range(len(stringIn)):
        for j in range(len(Grammar)):
            c_grammar = Grammar[j].split(",")
            peek = stack(Stack)


            if(stringIn[i] == c_grammar[1] and peek == c_grammar[2] and Start == c_grammar[0]):
                Start = c_grammar[4]
                Stack.pop()

                for y in range( len(c_grammar[3])-1 , -1, -1):
                    Stack.append(c_grammar[3][y])
                    _stack.append(c_grammar[3][y])

                break


    FinalDirect = Grammar.pop()
    FinalDirect = FinalDirect.split(",")
    dummy = ""



    for i in range(len(Stack)):
        dummy = dummy.join(Stack[i])

    if(dummy == FinalDirect[2]):
        print("Output")
        print("True")
        TLA = show(Start , _stack, _temp, stringIn)

        for j in range(len(TLA)-1):
            print(TLA[j] , end = " => ")
        print(TLA[len(TLA)-1])

    else:
        print("Output")
        print("False")

if __name__ == "__main__":
    main()