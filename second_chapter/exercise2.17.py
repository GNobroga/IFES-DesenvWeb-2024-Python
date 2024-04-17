
age = int(input("Enter: "))

if age < 0:
    print("Você ainda está dentro da barriga da mãe!")
elif age < 21 :
    print("Você é jovem")
elif 21 <= age <= 60:
    print("Você é adulto")
else:
    print("Você é idoso")