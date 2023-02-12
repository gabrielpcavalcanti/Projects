def is_one_digit(v):

    if float(v)  > -10 and float(v) < 10 and float(v).is_integer() == True:
        output = True
        return output
    else:
        output = False
        return output

def check(v1,v2,v3):

    msg = ""

    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6

    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    
    if msg != "":
        msg = msg_9 + msg
        print(msg)
        return msg
    else:
        return


msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

dic_msg = {0:msg_0, 1:msg_1, 2:msg_2, 3:msg_3, 4:msg_4, 5:msg_5, 
           6:msg_6, 7:msg_7, 8:msg_8, 9:msg_9, 10:msg_10, 11:msg_11, 12:msg_12}

lista_results = []

answer = ''
answer_2 = ''
memory = float(0)

while True:

    if answer == 'n':
        break
    
    if answer_2 == 'n':
        break
        
    answer = ''
    
    print(msg_0)

    eq = input()

    eq_lista = eq.split(" ")
    lista_operadores = ["+","-","*","/"]

    eq_lista_2 = [eq_lista[0].replace('.','',1),eq_lista[1].replace('.','',1),eq_lista[2].replace('.','',1)]

    
    if eq_lista_2[0].isnumeric() and eq_lista_2[2].isnumeric() and eq_lista_2[1] in lista_operadores:

        check(v1=float(eq_lista[0]), v2=float(eq_lista[2]), v3=eq_lista[1])

        if eq_lista_2[1] == "+":
            result = float(eq_lista[0]) + float(eq_lista[2])
            lista_results.append(result)
            print(result)

        elif eq_lista_2[1] == "-":
            result = float(eq_lista[0]) - float(eq_lista[2])
            lista_results.append(result)
            print(result)
            
        elif eq_lista_2[1] == "*":
            result = float(eq_lista[0]) * float(eq_lista[2])
            lista_results.append(result)
            print(result)
            
        elif eq_lista_2[1] == "/":
            try:
                result = float(eq_lista[0]) / float(eq_lista[2])
                lista_results.append(result)
                print(result)
            except ZeroDivisionError:
                print(msg_3)
                continue
      
    #if eq_lista_2[0].isnumeric() == False or eq_lista_2[2].isnumeric() == False:
        #print(msg_1)

    # (eq_lista_2[0].isnumeric() and eq_lista_2[2].isnumeric()) and (eq_lista_2[1] not in lista_operadores):
       # print(msg_2)
    
    while True:

        if answer == 'n':
            break

        if answer_2 == 'n':
            break

        if answer == 'y':
            break

        if eq_lista[0] == 'M' and eq_lista[2] == 'M':

            eq_lista[0] = memory
            eq_lista[2] = memory

            check(v1=float(eq_lista[0]), v2=float(eq_lista[2]), v3=eq_lista[1])
            
            result_2_soma = eq_lista[0] + eq_lista[2]
            lista_results.append(result_2_soma)
            if eq_lista_2[1] == "+":
                print(result_2_soma)
                continue
            result_2_sub = eq_lista[0] - eq_lista[2]
            lista_results.append(result_2_sub)
            if eq_lista_2[1] == "-":
                print(result_2_sub)
                continue
            result_2_mult = eq_lista[0] * (eq_lista[2])
            lista_results.append(result_2_mult)
            if eq_lista_2[1] == "*":
                print(result_2_mult)
                continue
            try:
                result_2_div = eq_lista[0] / eq_lista[2]
                lista_results.append(result_2_div)

                if eq_lista_2[1] == "/":
                    print(result_2_div)
                    continue
                
                
            except ZeroDivisionError:
                print(msg_3)
                break
                

        
        elif eq_lista[0] == 'M':

            eq_lista[0] = memory

            check(v1=float(eq_lista[0]), v2=float(eq_lista[2]), v3=eq_lista[1])
            
            result_2_soma = eq_lista[0] + float(eq_lista[2])
            lista_results.append(result_2_soma)
            if eq_lista_2[1] == "+":
                print(result_2_soma)
                continue
            result_2_sub = eq_lista[0] - float(eq_lista[2])
            lista_results.append(result_2_sub)
            if eq_lista_2[1] == "-":
                print(result_2_sub)
                continue
            result_2_mult = eq_lista[0] * float(eq_lista[2])
            lista_results.append(result_2_mult)
            if eq_lista_2[1] == "*":
                print(result_2_mult)
                continue
            try:
                result_2_div = eq_lista[0] / eq_lista[2]
                lista_results.append(result_2_div)

                if eq_lista_2[1] == "/":
                    print(result_2_div)
                    continue
                
                
            except ZeroDivisionError:
                print(msg_3)
                break
                

        elif eq_lista[2] == 'M':

            eq_lista[2] = memory

            check(v1=float(eq_lista[0]), v2=float(eq_lista[2]), v3=eq_lista[1])
            
            result_2_soma = eq_lista[2] + float(eq_lista[0])
            lista_results.append(result_2_soma)
            if eq_lista_2[1] == "+":
                print(result_2_soma)
                continue
            result_2_sub = eq_lista[2] - float(eq_lista[0])
            lista_results.append(result_2_sub)
            if eq_lista_2[1] == "-":
                print(result_2_sub)
                continue
            result_2_mult = eq_lista[2] * float(eq_lista[0])
            lista_results.append(result_2_mult)
            if eq_lista_2[1] == "*":
                print(result_2_mult)
                continue
            try:
                result_2_div = eq_lista[0] / eq_lista[2]
                lista_results.append(result_2_div)

                if eq_lista_2[1] == "/":
                    print(result_2_div)
                    continue
                
            except ZeroDivisionError:
                print(msg_3)
                break
                
        print(msg_4)

        answer = input()

        if answer == 'y':

            memory = result

            if is_one_digit(result):

                msg_index = 10

                while msg_index <= 12:

                    print(dic_msg[msg_index])

                    answer_3 = input()

                    if answer_3 == 'y':

                        msg_index += 1
                        continue

                    if answer_3 == 'n':

                        lista_results.pop()
                        memory = lista_results[-1]

                        break
            
       

            while answer != 'n':

                print(msg_5)

                answer_2 = input()

                if answer_2 == 'y':

                    break
                
                if answer_2 != 'n':
                    
                    continue
                
                if answer_2 == 'n':
                    break

        if answer == 'n':

            answer = ''

            while answer != 'n':

                print(msg_5)

                answer = input()

                if answer == 'y':

                    break
                
                if answer != 'n':
                    
                    continue
                
                if answer == 'n':
                    break
                