'''
print("Ola mundo!") 
print (1 + 1)
nome = "sara" 
idade = 25 
print (" nome:", nome)
print("idade:",idade )
print(f"nome:{nome},idade: {idade}")
print (" nome:"+ nome)
print("idade:"+ str (idade))
a= 2
b= 4
c= 6 
if a + b == c:
    print('c é maior que a e b')
B0= True
B1= True
if B0 and B1:
    print ('resultado ou verdadeiro(1 )')
else:
    print('resultado ou falso(0)') 

N1= 4
if N1 % 2 ==0:
    print('numero divisivel por 2')
elif N1 % 3 ==0: 
    print ('numero divisivel por 3 ')
else: 
    print (' nao divisivel nem por 2 nem por 3')


Marcelo= range(1,6)
for I in Marcelo: 
    if I ==3:     
        break
    print (I)
'''

contador=5
while contador <=10: 
    print (contador) 
    if contador == 5: 
        break # sai do loop quando o contador fot igual a 5 
    contador += 1 
    if contador ==3 :
        continue # pula o restante do código quando o contador for igual a 3 
    print(contador) 