import turtle

#1) AB; |AB| = 5 cm
#2) k; k(A; 5 cm)
#END

# Global vars:
direct_input = ""
prev_i = ""
inp = []
out = []

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

        # Removes closing brackets
        if ")" in direct_input:
            continued_inp = ""
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


print(inp)

