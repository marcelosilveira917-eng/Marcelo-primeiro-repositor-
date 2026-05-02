lista =  [] 
lista = [1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
print(lista) 
lista.clear()
lista.append ("ana")
lista.append ("maria")
lista.append ("joao")
lista.append ("pedro")
 
print(lista) 
lista.sort() 
print(lista)  
lista = [1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
listab = [1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
listac = [1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
print(lista)
lista.reverse()
print(lista) 
lista[0] 

index = lista.index(13) 
print(lista[index]) 
lista.append ("valentina") 
print(lista) 
print(lista.count("valentina"))       
print(lista) 
remove= lista.remove(10) 
remove= lista.remove(17) 
print(lista) 
lista.insert(20, "pedro") 
lista.insert(11, "joao") 
print(lista) 
lista.append(listab)
print(lista) 
listac = listab + lista 
print(listac) 

  