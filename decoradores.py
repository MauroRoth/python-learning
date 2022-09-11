# DECORADORES - Función Decoradora en Python - 

def funcion_decoradora(funcion_a_decorar):
	def funcion_docorada(*args):
		print("\nCalculando:")
		funcion_a_decorar(*args)
		print("\nFin del Cálculo!")
	return funcion_docorada


@funcion_decoradora
def suma(a,b):
	print("suma: ", a+b)

@funcion_decoradora
def resta(a,b):
	print("resta: ", a-b)


suma(20,6)
resta(20,6)


