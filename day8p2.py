with open('input8.txt', 'r') as f:
    data=f.readlines()

result_list=[]

for line in data:
    output_list=[]
    example_list=[]
    output= line.split('|')[1].split()
    example=line.split('|')[0].split()
    output_list+=output
    example_list+=example
    four=""
    seven=""
    eight=""
    lowle=""
    output_number=""
    for examples in example_list:
        if len(examples)==4:
            four=examples
        elif len(examples)==3:
            seven=examples
        elif len(examples)==7:
            eight=examples
    number_decoded=[four, seven, eight]
    #print(example_list, output_list)
    #print(number_decoded)
    for char in eight:
        bOK=False
        if char in four:
            continue
        elif char in seven:
            continue
        else:
            bOK=True
        if bOK:
            lowle+=char
    #print(lowle)
    for number in output:
        if len(number)==2:
            output_number+="1"
        elif len(number)==4:
            output_number+="4"
        elif len(number)==3:
            output_number+="7"
        elif len(number)==7:
            output_number+="8"
        else:
            if len(number)==5:
                sc=0
                lc=0
                bOK=True
                for char in seven:
                    if char in number:
                        sc+=1
                if sc==3:
                    output_number+="3"
                    bOK=False
                elif bOK:
                    for char in lowle:
                        if char in number:
                            lc+=1
                    if lc==2:
                        output_number+="2"
                    else:
                        output_number+="5"
            elif len(number)==6:
                sc=0
                fc=0
                bOk=True
                for char in four:
                    if char in number:
                        fc+=1
                if fc==4:
                    output_number+="9"
                    bOk=False
                elif bOk:
                    for char in seven:
                        if char in number:
                            sc+=1
                    if sc==3:
                        output_number+="0"
                    else:
                        output_number+="6"
    result_list.append(int(output_number))
print(sum(result_list))                