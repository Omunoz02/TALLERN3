
def AgregarFuncionario():
    funcionario={}
    continua="s"
    while continua=="s":
        ID=int(input("\n Ingrese el ID del Funcionario:\n "))
        nombre=input("\n Ingrese El nombre del Funcionario: \n")
        cargo=(input("\n Ingrese el cargo del Funcionario: \n"))
        salario=float(input(" \n Ingrese el salario del Funcionario: \n"))
        funcionario[ID]=(nombre,cargo,salario)
        continua=input("\n Desea cargar otro producto[s/n]? \n")
    return funcionario
def imprimirLista(funcionario):
    

    for ID in funcionario:
        print("<<<<<<<<<<Listado completo de Funcionarios:>>>>>>>>>")
        print("ID---NOMBRE-CARGO-SALARIO")
        print(ID,funcionario[ID][0],funcionario[ID][1],funcionario[ID][2])


def consultaFuncionario(funcionario):
    ID=int(input("\n Ingrese el ID del funcionario a consultar:\n"))
    if ID in funcionario:
        print(funcionario[ID][0],funcionario[ID][1],funcionario[ID][2])
   