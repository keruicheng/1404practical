file = 'name.txt'
output_file = open(file,'w')
name = input('Please Enter Your Name:')
print(name,file=output_file)
output_file.close()


input_file = open('name.txt','r')
name = input_file.read().strip()
print('"Your name is {}"'.format(name))
input_file.close()

Num_file = 'Numbers.txt'
num_out_file = open(Num_file,'w')
num1,num2,num3 = 17,42,400
print(num1,file=num_out_file)
print(num2,file=num_out_file)
print(num3,file=num_out_file)
num_out_file.close()

num_in_file = open('Numbers.txt','r')
number1 = int(num_in_file.readline())
number2 = int(num_in_file.readline())
sum = number1 + number2
print(sum)
num_in_file.close()

total_in_file = open('Numbers.txt','r')
total = 0
for i in total_in_file:
    num = int(i)
    total += num
print(total)
total_in_file.close()


