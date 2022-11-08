from sys import *
tokens = []
nums_stack = []
symbols = {}
def open_file(filenaame):
    data = open(filenaame,"r").read()
    data += "<EOF>"
    return data
def lex(filedata):
    filedata = list(filedata)
    numss = str([x for x in range(10)])
    tok = ""
    strng = "" #for strings or text
    expr = ""  #for math and numbers
    isexpr = 0
    state = 0 #used for "" "
    n = 0#stands for number
    var = "" #used for variables
    varStarted = 0
    for char in filedata:
        tok +=char
        if(tok==" "):
            if(state == 0):
                tok =""
            else:
                tok = " "
        elif tok=="\n" or tok=="<EOF>":
            if expr != "" and isexpr == 1:
                tokens.append("EXPR:"+expr)
                #print(expr+"EXPR")
                expr = ""
            elif  expr != "" and isexpr == 0:
                tokens.append("NUMS:" + expr)
                #print(expr+"nums")
                expr = ""
            elif var!="":
                tokens.append("VAR:"+ var)
                var = ""
                varStarted = 0
            tok = ""
        elif(tok == "=" and state ==0):
            if (var!= ""):
                tokens.append("VAR:"+var)
                var = ""
                varStarted = 0
            tokens.append("EQUALS")
            tok = ""
        elif(tok == "prnt"):
            tokens.append("PRINT")
            tok = ""
        elif (tok == "inpt"):
            tokens.append("INPUT")
            tok = ""
        elif (tok == "if"):
            tokens.append("IF")
            tok = ""
        elif (tok == "then"):
            tokens.append("THEN")
            tok = ""
        elif (tok in numss):
            #print("num found")
            expr += tok
            tok = ""
        elif tok=="+" or tok == "*"or tok == "/"or tok == "("or tok == ")"or tok == "-" or tok == "%":
            isexpr = 1
            expr+=tok
            tok=""
        elif(tok == "\"" or tok == " \""):
            if state == 0:
                state = 1
            elif state ==1:
                tokens.append("STRING:"+strng+"\"")
                strng=""
                state = 0
                tok = ""
        elif (tok == "~" and state ==0):
            varStarted =1
            var+=tok
            tok = ""
        elif (varStarted ==1):
            if (tok == "<" or tok == ">"):
                if var != "":
                    tokens.append("VAR:" + var)
                    var = ""
                    varStarted = 0
            var+=tok
            tok = ""
        elif(state == 1):
            strng += tok
            tok = ""
    #print(expr) #prints all the numbers
    #print(tokens)
    #print(symbols)
    #return ""
    return tokens
def doPrint(toPrint):
    if(toPrint[0:6]=="STRING"):
        toPrint = toPrint[8:]
        toPrint = toPrint[:-1]
    elif(toPrint[0:3]=="NUMS"):
        toPrint = toPrint[3:]
    elif (toPrint[0:4] == "EXPR"):
        toPrint = exp_eval(toPrint[5:])
    print(toPrint)

def exp_eval(expr):
    '''
    expr = ","+expr
    i = len(expr)-1
    num = ""
    while(i>=0):
        if (expr[i] == "+" or expr[i]== "-"or expr[i]== "/"or expr[i]== "*"or expr[i]== "%"):
            num= num[::-1]
            nums_stack.append(num)
            nums_stack.append(expr[i])
            num = ""
        elif(expr[i]==","):
            num = num[::-1]
            nums_stack.append(num)
            num=""
        else:
            num += expr[i]
        i-=1
    print(nums_stack)'''
    return eval(expr)
def doAssign(varName,varValue):
    symbols[varName[4:]] = varValue
def getVar(varName):
    varName = varName[4:]
    if varName in symbols:
        #print("True")
        return symbols[varName]
    else:
        return "ERROR 7989: UNDF"
        exit()
def getInput(String,varname):
    i = input(String[1:-1]+ " ")
    symbols[varname] = "STRING:\"" + i+"\""
def parse(tokns):
    i =0
    while(i<len(tokns)):

        if(tokns[i]+" "+tokns[i+1][0:6]=="PRINT STRING" or tokns[i]+" "+tokns[i+1][0:4]=="PRINT NUMS" or tokns[i]+" "+tokns[i+1][0:4]=="PRINT EXPR" or tokns[i]+" "+tokns[i+1][0:3]=="PRINT VAR"):
            if(tokns[i+1][0:6]=="STRING"):
                doPrint(tokns[i+1])
            elif(tokns[i+1][0:4]=="NUMS"):
                doPrint(tokns[i + 1])
            elif (tokns[i + 1][0:4] == "EXPR"):
                doPrint(tokns[i + 1])
            elif (tokns[i + 1][0:3] == "VAR"):
                doPrint(getVar(tokns[i + 1]))
            #print("found")
            i+=2
        elif(tokns[i][0:3]+" "+tokns[i+1]+" "+tokns[i+2][0:6] == "VAR EQUALS STRING" or tokns[i][0:3]+" "+tokns[i+1]+" "+tokns[i+2][0:4] == "VAR EQUALS NUMS" or tokns[i][0:3]+" "+tokns[i+1]+" "+tokns[i+2][0:4] == "VAR EQUALS EXPR"  or tokns[i][0:3]+" "+tokns[i+1]+" "+tokns[i+2][0:3] == "VAR EQUALS VAR" ):

            if (tokns[i + 2][0:6] == "STRING"):
                doAssign(tokns[i], tokns[i + 2])
            elif (tokns[i + 2][0:4] == "NUMS"):
                doAssign(tokns[i], tokns[i + 2])
            elif (tokns[i + 2][0:4] == "EXPR"):
                doAssign(tokns[i], "NUMS:"+str(exp_eval(tokns[i + 2][5:])))
            elif (tokns[i + 2][0:3] == "VAR"):
                doAssign(tokns[i],getVar(tokns[i + 2]))
            #doAssign(tokns[i],tokns[i+2])
            i+=3
        elif(tokns[i]+" "+tokns[i+1][0:6]+" "+tokns[i+2][0:3]=="INPUT STRING VAR"):
            getInput(tokns[i+1][7:],tokns[i+2][4:])
            i+=3
    #print(symbols)


def run():
    data = open_file(argv[1])
    #lex(data)
    toks = lex(data)
    parse(toks)

run()
