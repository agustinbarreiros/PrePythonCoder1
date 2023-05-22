
import json
import os

print("Bienvenido a Pagina Random de Internet")


i=0

def logueo_usuario():
    usuario = input("Ingrese Nombre de usuario\n")
    pwd = input("Ingrese Contraseña\n")
    os.system("cls")
    with open("users.json", "r") as file:
            data = json.load(file)
            for user in data["usuarios"]:
                if(user["usuario"]==usuario and user["pwd"]== pwd):
                    print(f"Bienvenido {usuario}")
                    file.close
                    return True
                               
            else:
                    print("Usuario y/o Contraseña erroneos")
                    return False    
            
       
def registrar_usuario():
    usuario = input("Escriba para crear su Nombre de usuario\n")
    pwd = input("Escriba para crear su Contraseña\n")
    with open("users.json", "r") as file:
        data = json.load(file)
        for user in data["usuarios"]:
            if user["usuario"] == usuario:
                print("Este usuario ya existe, elija otro")
                return
    newdata = {'usuario': usuario, 'pwd': pwd}
    data["usuarios"].append(newdata)
    with open("users.json", "w") as file:
        json.dump(data, file)
        file.close
    print("Registrado con éxito") 


def mostrar_usuarios():
    with open("users.json", "r") as file:
        data = json.load(file)
    print("Lista de usuarios y contraseñas:")    
    for usuario, pwd in data.items():       
        print(f"{usuario} : {pwd}")          
 
while i == 0 :
    inicio = int(input("Escriba 1 Inicio Sesion\nEscriba 2 Registrarse\nEscriba 3 Mostrar usuarios\nEscriba 4 Para salir "))
    if inicio == 1 :
        if logueo_usuario():
             i = 1
    elif inicio == 2:
        registrar_usuario()
    elif inicio == 3:
         mostrar_usuarios()
         
    elif inicio ==4:
         i = 1         
    else:
        print("Por favor escriba el numero de las opciones >:D")
        
    