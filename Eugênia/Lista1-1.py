
se = input("digite seu sexo:: (h) para homem e (m)para mulher: ")

if se == "h":
   
    altura = float(input("Digite a sua altura : "))    
    peso = (altura * 72.7) -58
    
    print(f"Um HOMEM com a altura de: {altura}m, o peso ideal seria de: {peso:.2f}kg")

else:
    se == "m"
    
    altura = float(input("Digite sua Altura: "))    
    peso = (altura * 62.1)- 44.7    
    print(f"Uma MULHER com altura de: {altura}m, o peso ideal seria de: {peso:.2f} ")

