def Action(List):
   
    non_transiton = []
    transition = []
    num = int(List[0])
    alphabet = List[1]
    alphabet = alphabet.split(",")

    for i in range(4,len(List)):
        _temp = List[i].split(",")
        if _temp[3] != "" :
            transition.append(List[i])
        else:
            non_transiton.append(List[i])

    CFG = []
    for l in range(num):

        if l == 0:
            for i in range(len(transition)):

                _temp = transition[i].split(",")
                l_str = ""
                l_str = l_str + str(_temp[0])
                l_str = l_str + str(_temp[2])
                l_str = l_str + str(_temp[4])
                CFG.append(l_str)

                for j in range(num - 1):
                    l_str = ""
                    l_str = l_str.join(_temp[1])
                    CFG.append(l_str)


                    for m in range(0,num):

                        l_str = ""
                        if len(_temp[3])>1:
                            l_str = l_str.join(str("("+_temp[0]+str(_temp[3][0])+
                                                   "q"+str(m)+")"
                                                   +"("+"q"+
                                                   str(m)+
                                                   str(_temp[3][1])+
                                                   _temp[4]+")"))
                        else:
                            l_str = l_str.join(str("(" + _temp[0] +
                                                  str(_temp[3][0]) + 
                                                  "q" + 
                                                  str(m) + ")"))
                        CFG.append(l_str)

        else:
            for i in range(len(transition)):

                _temp = transition[i].split(",")
                l_str = ""
                l_str = l_str + str(_temp[0])
                l_str = l_str + str(_temp[2])
                l_str = l_str + "qf"
                CFG.append(l_str)

                for j in range(num - 1):
                    l_str = ""
                    l_str = l_str.join(_temp[1])
                    CFG.append(l_str)

                    for m in range(0, num):
                        l_str = ""
                        if (len(_temp[3]) > 1):
                            l_str = l_str.join(str(
                                "(" + _temp[0] +
                               str(_temp[3][0]) +
                              "q" + str(m) +
                             ")" + "(" + 
                             "q" + str(m) + str(
                                    _temp[3][1]) +
                            "qf" + ")"))
                        else:
                            l_str = l_str.join(str(
                                "(" + _temp[0] +
                                str(_temp[3][0])
                                + "q" + 
                               str(m) + ")"))

                        CFG.append(l_str)


    o = Other_transition(non_transiton)
    for i in range(len(o)):

        CFG.append(o[i])
    return CFG

def Other_transition(lst):

    yCFG = []
    for i in range(len(lst)):

        string = ""
        temp = lst[i].split(",")
        string = string + str(temp[0])
        string = string + str(temp[2])
        string = string + str(temp[4])
        string = string + " -> "

        if temp[1] != "":
            string = string + str(temp[1])
        else:
            string = string + "_"

        yCFG.append(string)
    return yCFG


def process(File):

    input = []
    for line in File:
        line = line.split("\n")
        input.append(line)

    for i in range(len(input)):
        if input[i][-1] == '':
            del input[i][-1]

    List = []
    for i in range(len(input)):
        List.append(input[i][0])

    List = [s.replace('*', '') for s in List]
    List = [s.replace('_', '') for s in List]
    List = [s.replace('->', '') for s in List]
   

    return List


def main():
    input= open("input.txt" , 'r')
    pro = process(input)
    list = Action(pro)

    for i in range(4 * int(pro[0])):
        print(list[0] + " -> " + list [1] + list[2] + " | " + list[1] + list[3])

        for j in range(2 * int(pro[0])):
            del list[0]

    for i in range(len(list)):
        print(list[i])

if __name__ == "__main__":
    main()



