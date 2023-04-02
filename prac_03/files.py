name = input("Please enter your name: ")
out_file = open("name.txt","w")
print(name,file=out_file)
out_file.close()

out_file = open("name.txt","r")
content = out_file.read()
print(f"Your name is {content}")
out_file.close()

FILE = "numbers.txt"
out_file = open(FILE,"w")
out_file.write("17\n42\n400")
out_file.close()

in_file = open(FILE,"r")
num1 = int(in_file.readline())
num2 = int(in_file.readline())
total = num1 + num2
print(total)
in_file.close()

in_file = open(FILE,"r")
lines = in_file.readlines()
total = 0
for line in lines:
    total += int(line.strip())
print(total)
in_file.close()