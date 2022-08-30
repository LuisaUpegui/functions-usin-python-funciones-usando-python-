#Ejercicio 1
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print("-------------")
#Cambiar de la lista en posicion 1 el numero de la posicion 0
x[1][0]=15
print(x)
print("-------------")
#Cambiar el apellido del primer alumno de "Jordan" a "Bryant"
estudiantes[0]['last_name']='Bryant'
print(estudiantes)

print("-------------")
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
#En el directorio_deportes, cambia "Messi" por "Andrés".

directorio_deportes['fútbol'][0]='Andrés'
print(directorio_deportes)
print("-------------")
#Cambia el valor 20 en z a 30.

z = [ {'x': 10, 'y': 20} ]

z[0]['y']=30
print(z)
print("-------------")
#Ejercicio 2

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

for i in estudiantes:
    iterate_Dictionary=""
    for key,value in i.items():
        iterate_Dictionary+= (f" {key}  - {value}")
    print(iterate_Dictionary)
print("-------------")
#Ejercicio 3 
def iterate_Dictionary2(keyname, estudiantes):
    for i in estudiantes:
        print(i[keyname])

#Me imprime el nombre
name= iterate_Dictionary2('first_name',estudiantes)
#Me imprime el apellido
lastname= iterate_Dictionary2('last_name', estudiantes)
print("-------------")
# Ejercicio 4
# Iterar a traves de un diccionario con valores de lista 

dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dicc):
    for key,val in dicc.items():
        print(f"{len(val)}{key.upper()}")
        for i in range(0, len(val)):
            print(val[i])

printInfo(dojo)
