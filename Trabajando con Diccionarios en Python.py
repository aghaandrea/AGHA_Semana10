print("**************")
print("Diccionario sin modificar")
print("***************")

# dicionario inicial con informacion _ personal fistica
informacion_personal= {
"nombre": "Andrea",
"edad": 36,
"ciudad":"Quito"
}

#ordena los datos
for key in informacion_personal:
    print(f"{key}: {informacion_personal[key]}")


#Accede al valor asociado con la clave "ciudad" y modifícalo.
informacion_personal ["ciudad"]="Quito"

#Agrega una nueva clave-valor al diccionario que represente la "profesion y el numero de telefono" de la persona
informacion_personal ["profesion"]="tecnologias de la informacion"
informacion_personal ["telefono"]="0999333126" # numero de telefono fisticio

#Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio.
if "telefono" in informacion_personal:
    print("El numero de telefono no existe en este diccionario")
else:
    print("El numero de telefono  existe en diccionario")

# Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.
del informacion_personal ["edad"]

# Imprime el diccionario resultante después de realizar todas las operaciones.
print("*****************")
print("Diccionario modificado")
print("****************")

#pone los datos en columnas
for key in informacion_personal:
    print(f"{key}: {informacion_personal[key]}")

#verifica el numero de telefono en el diccionario actual
if "telefono" in informacion_personal:
    print("El numero de telefono existe en este  diccionario")
else:
    print("El numero de telefono  no existe en este diccionario")
print("****************")