nome = str(input("Digite seu nome: "))
salario = float(input("Digite seu salário: "))
percentual = float(input("Digite o valor percentual do bônus: "))/100 


bonus = salario * percentual 
remuneracao_total = salario + bonus 

print(f"\n \t {nome} PARABÉNS!!! \n \t seu bônus total é de: R${bonus} \n \t totalizando a remuneração total de R${remuneracao_total}")


