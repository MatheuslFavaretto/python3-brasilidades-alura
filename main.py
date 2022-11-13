from TelefonesBr import TelefonesBr
import re

#padrao_molde = "(xx)aaaa-wwww"
#padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
#texto = "eu gosto do numero 2126451234"
#resposta = re.search(padrao,texto)

#print(resposta)
telefone = "552126481234"
telefone_objeto = TelefonesBr(telefone)

print(telefone_objeto)