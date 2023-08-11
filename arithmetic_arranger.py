def arithmetic_arranger(problems,sol=False):
    ### Condition 1
    arranged_problems = ''
    if len(problems) > 0 and len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems
    ### Condition 2
    operators = list(map(lambda x: x.split()[1],problems))
    accept = {'+','-'}
    if set(operators) != accept and len(set(operators)) > 2:
        arranged_problems = "Error: Operator must be '+' or '-'."
        return arranged_problems
    ### Condition 3
    for i in range(0,len(problems)):
        NumCheck = list(map(lambda x: x.split()[0],problems)) + list(map(lambda x: x.split()[2],problems))
    if not all(map(lambda x: x.isdigit(),NumCheck)):
        arranged_problems = "Error: Numbers must only contain digits."
        return arranged_problems
    ### Condition 4
    if not all(map(lambda x: len(x)<=4,NumCheck)):
        arranged_problems = "Error: Numbers cannot be more than four digits."
        return arranged_problems
    firstrow = ''
    secondrow = ''
    dashline = ''
    lastrow = ''
    solutions = list(map(lambda x: eval(x), problems))
    ## First row
    for i in range(0,len(problems)):
        spacewidth = max(len(problems[i].split()[0]),len(problems[i].split()[2]))+2 ## plus 2 for operator and space
        if i != len(problems)-1:
            firstrow += problems[i].split()[0].rjust(spacewidth) + ' '*4
            dashline += '-'*spacewidth + ' '*4
            lastrow += str(solutions[i]).rjust(spacewidth) + ' '*4
        else:
            firstrow += problems[i].split()[0].rjust(spacewidth) + '\n'
            dashline += '-'*spacewidth
            lastrow += str(solutions[i]).rjust(spacewidth)
    ## Second row
    for i in range(0,len(problems)):
        spacewidth = max(len(problems[i].split()[0]),len(problems[i].split()[2]))+1 ## plus 1 for pace
        #print(spacewidth)
        if i != len(problems)-1:
            secondrow += problems[i].split()[1] + problems[i].split()[2].rjust(spacewidth) + ' '*4
        else:
            secondrow += problems[i].split()[1] + problems[i].split()[2].rjust(spacewidth) + '\n'
    if sol:
        arranged_problems = ''.join([firstrow,secondrow,dashline+'\n',lastrow])
    else:
        arranged_problems = ''.join([firstrow,secondrow,dashline])
    return arranged_problems