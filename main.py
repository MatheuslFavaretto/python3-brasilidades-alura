from cpf_cnpj import CpfCnpj
from validate_docbr import CNPJ

#cnpj = CNPJ()
exemplo_cnpj = "35379838000112"
#print(cnpj.validate(exemplo_cnpj))

#cpf_um = Cpf(41400336813)

documento = CpfCnpj(exemplo_cnpj, 'cnpj')
print(documento)
