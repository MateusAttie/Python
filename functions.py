def sum(a,b):
	return a + b

def salario_descontado_imposto(salario,imposto=27.):
	return salario - (salario * imposto * 0.01)

c = sum(1,3)
print(c)

salario_real = salario_descontado_imposto(5000)
print(salario_real)
