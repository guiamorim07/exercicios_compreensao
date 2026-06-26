vogais= ['a', 'e' , 'i', 'o' , 'u']
string= "texto"

def contarvogais(vogais, string):
	numvogais= letra for letra in string if letra in vogais
	return len(numvogais)
	
resultado= contarvogais(vogais,string)
print(resultado)