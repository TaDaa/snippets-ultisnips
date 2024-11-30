import logging
import vim

def getArgs(input,delim=','):
    output=[]
    carrot = 0
    current = ""
    args = []
    for i in range(0,len(input)):
        ch = input[i]
        if (input[i] == '<'):
            current+=ch
            carrot+=1
            continue
        elif (input[i] == '>'):
            current+=ch
            carrot-=1
            continue
        elif (carrot > 0):
            current+=ch
            continue
        elif (input[i] == delim):
            args.insert(0,current.strip())
            current=""
        else:
            current+=ch
    current = current.strip()
    if current != "":
        args.insert(0,current)


    #first create inputs
    for i in range(len(args)-1,-1,-1) :
        full_arg = args[i]
        last_space_index = full_arg.rfind(' ')
        last_carrot_index = full_arg.rfind('>')
        #print(last_carrot_index)
        if (last_space_index > last_carrot_index):
            output.append([full_arg[0:last_space_index].strip(),full_arg[last_space_index:len(full_arg)].strip()])
        else:
            output.append([full_arg[0:last_carrot_index+1].strip(),full_arg[last_carrot_index+1:len(full_arg)].strip()])

    #print(output)
    return output

def getType(input):
    result = getArgs(input,"")
    if len(result) > 0 and len(result[0]) > 0:
        return result[0][0]
    return ""



#getArgs("Private Test , List<String > wtf,Map<Set,Set>screwsItUp ")
def camelCase(st,upper=False):
    if (st != None and len(st) > 0):
        if (upper == False):
            return st[0].lower() + st[1:]
        else:
            return st[0].upper() + st[1:]
    return ""


def getPackage(st):
    result = st.replace('\\','/').split('src/main/java/')
    if len(result) > 1:
        result = result[-1]
    else:
        result = st
    result = result.replace('/','.')
    return result

def getPackageForCurrentFile():
    file = vim.eval("expand('%p')")
    #if (file == None or file == ""):
        #file = '/src/main/java/com/idexx/limsclient/ui/LKabTestCellRenderer.java'
    #print(file)
    #print(file.split('/')[0:-1])
    dir = file.split('/')[0:-1]
    dir = "/".join(dir)
    print(dir)
    return getPackage(dir)



