import turtle

#1) AB; |AB| = 5 cm
#2) k; k(A; 5 cm)
#END

# Global vars:
direct_input = ""
prev_i = ""
inp = []
out = []
distance_amplifier = 10

# Parses  ⊙.⊙
class Parser:

    # Determines if input (num) is an int
    def is_number(num):
        try:
            num = int(num)
            return True
                                            
        except:
            return False
        
    #Repeats until you type "END"
    while direct_input != "END":
    #Takes your input
        direct_input = input()
        continued_inp = ""

        # Removes closing brackets
        if ")" in direct_input:
            for i in direct_input:

                if direct_input[0] == i and is_number(i) == True:
                    prev_i = i
                    continue
                                    
                elif is_number(prev_i) == True and i == ")":
                    prev_i = i
                    continue

                prev_i = i
                continued_inp += i
                    
        inp.append(continued_inp.strip())
    inp.pop(len(inp) - 1)

class Reading:
    for i in inp:
        for i2 in range(len(i)):
            print(i2)
            if i[i2] == "=":
                turtle.left(180)
                print(i)
                turtle.forward(int(i[(i2 + 2)]) / 2 * distance_amplifier)
                turtle.left(180)
                turtle.forward(int(i[(i2 + 2)]) * distance_amplifier)

print(inp)

