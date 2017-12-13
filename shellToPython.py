import re

def returnFunctionName(line):
    matcher = re.match("(?:function )+(?P<function_name>[aA-zZ]*)", line)
    return matcher.group('function_name')

def returnEchoPrint(line):
    matcher = re.match("(?:echo )+(.*)", line.strip())
    return matcher.group(1)

def returnSystemCommand(line):
    return "call(\"{}\")".format(line)

def echoLineToPythonPrint(line):
    if 'echo' in line:
        return "    print({})".format(returnEchoPrint(line))
    else:
        return "    {}".format(returnSystemCommand(line))

def shellFunctionsToPython():
    with open('jarvis') as f:
        with open("jarvis.py", "a") as myfile:
            write = False
            for line in f:
                if '}' in line:
                    write = False
                    myfile.write("\n")
                elif 'function' in line:
                    write = True
                    function_name = returnFunctionName(line)
                    myfile.write("def {}():\n".format(function_name))
                elif write == True:
                    write = True
                    myfile.write("{}\n".format(echoLineToPythonPrint(line.strip())))

shellFunctionsToPython()
