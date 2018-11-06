
print("please input your name:/n")
a = input()
with open('python_learning\pi_digits.txt','a') as file_object:
    file_object.write(a)
    
