# Sistema de controle de produção por turnos
# Repositório: txt | Interface: Caracteres | Desenvolvido em Python

# Bibliotecas
import funcoes as fn

while True:
    # Menu principal
    fn.limpartela()
    opcao = fn.menu()

    # Opção 1 (Cadastrar turno)
    if opcao == 1:
        fn.cadastro()

    # Opção 2 (Consulta de registros)
    elif opcao == 2:
        fn.consulta()

    # Opção 3 (Metas)
    elif opcao == 3:
        fn.metas()
        
    # Opção 4 (Atualizar registro)
    elif opcao == 4:
        fn.altera_registro()

    # Opção 5 (Excluir registro)
    elif opcao == 5:
        fn.exclui_registro()

    # Opção 6 (Relatório geral)
    elif opcao == 6:
        fn.relatorio()

    # Opção 7 (Sair)
    elif opcao == 0:
        break

