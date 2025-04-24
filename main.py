import turtle

copy_this = """1) AB; |AB| = 5 cm
2) k; k(A; 5 cm)
END"""

direct_input = ""
inp = []
out = []

while direct_input != "END":
    direct_input = input()
    print(direct_input)
    if ")" in direct_input:
        continued_inp = ""
        for i in direct_input:
            if i == ")":
                continue
            try:
                i = int(i)
                continue
            except:
                pass
            continued_inp += i
        print(continued_inp)
                
        inp.append(continued_inp)


print(inp)

