total = 0
homens = 0
mulheres = 0 
homensmaiortrinta = 0
mulherjovem = 0
idadetotal = 0
for i in range(101):
    sexo = input('Insira a letra correspondente ao sexo: M - Masculino | F - Feminino: ').upper()
    idade = int(input('Insira a idade: '))
    estadocivil = input('Insira a letra correspondente ao estado civil: S para Solteiro| C para Casado| V para Viúvo | D para Divorciado: ').upper()
    if sexo == 'M':
        homens += 1
    elif sexo == 'F':
        mulheres += 1
    if sexo == 'M' and idade > 30 and estadocivil == 'C':
        homensmaiortrinta +=1
    elif sexo == 'F' and idade < 20 and estadocivil == 'S':
        mulherjovem +=1
        
    idadetotal += idade
    total += 1
    
print(f'O percentual de mulheres: {(mulheres/total)*100:.2f}%')
print(f'O percentual de homens {(homens/total)*100:.2f}%')
print(f'A média de idade das pessoas: {idadetotal/total} anos')
print(f'A quantidade de mulheres solteiras com idade inferior a 20 anos: {mulherjovem}')
print(f'A quantidade de homens casados com idade superior a 30 anos: {homensmaiortrinta}')