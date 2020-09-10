def eliminarfuncionario(funcionario):
    
    del funcionario[int(input("\n Ingrese el ID del funcionario a eliminar: \n "))]
    print("\n Se ha eliminado \n  ")

    print("\n Listado completo de Funcionarios:\n ")
    for ID in funcionario:
        print(ID,funcionario[ID][0],funcionario[ID][1],funcionario[ID][2])




funcionario=AgregarFuncionario()
imprimirLista(funcionario)
consultaFuncionario(funcionario)
eliminarfuncionario(funcionario)