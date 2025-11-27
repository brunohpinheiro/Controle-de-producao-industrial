# BIBLIOTECAS
from datetime import datetime
from tabulate import tabulate
from time import sleep
import os

# CARREGA BASE DE DADOS
def carrega_txt():
    repositorio = {}
    with open("base de dados.txt", 'r', encoding='utf-8') as dados:
        for linha in dados:
            linha = linha.rstrip()
            if not linha:  # Ignora linhas em branco
                continue
            campos = linha.split(',')
            repositorio[int(campos[0])] = [campos[1],int(campos[2]),campos[3],int(campos[4]),int(campos[5]),int(campos[6]),float(campos[7]),campos[8],campos[9]]
    return repositorio

# CARREGA METAS
def carrega_metas():
    d_metas = {}
    with open('metas.txt', 'r',encoding='utf-8') as dados:
        for i in dados:
            linha = i.rstrip().split(',')
            d_metas[int(linha[0])] = int(linha[1])
    return d_metas

# SOBRESCREVE METAS
def write_metas(dicionario): 
    with open ("metas.txt", 'w', encoding='utf-8') as dados:
        for chave,valor in dicionario.items():
            dados.write (f"{chave},{valor}\n")

# SOBRESCREVE REPOSITÓRIOS
def write_repo(dicionario): 
    with open ("base de dados.txt", 'w', encoding='utf-8') as dados:
        for chave,valores in dicionario.items():
            dados.write (f"{chave},{valores[0]},{valores[1]},{valores[2]},{valores[3]},{valores[4]},{valores[5]},{valores[6]},{valores[7]},{valores[8]}\n")

# LIMPA TERMINAL
def limpartela():
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela de acordo com o SO

# ADICIONA REGISTROS AO REPOSITORIO
def inclui_txt(linha):
    with open("base de dados.txt", 'a', encoding='utf-8') as dados:
        dados.write(linha + ' \n')

# CORES ANSI
cor = {
    'padrao': '\033[m',      
    'vermelho': '\033[31m',
    'azul': '\033[34m',}

# CABEÇALHOS
def cabec (n,t):
    print(f"{'='*n}\n{t.center(n).upper()}\n{'='*n}")
    
# MENU PRINCIPAL 
def menu():
    while True:
        limpartela()
        cabec(100,'Sistema de registro de produção')
        print('[1] Cadastrar turno\n[2] Consulta de registros\n[3] Metas\n[4] Alterar registro\n[5] Excluir registro\n[6] Relatório geral\n[0] Sair\n    ')
        try:
            opcao = int(input('Escolha uma opção: '))
        except:
            print(f'Para acessar um menu, digite o seu respectivo {cor["vermelho"]}número{cor["padrao"]}')
            sleep(1.5)
            continue
        else:
            if opcao <= 7 and opcao > 0 :
                break
            elif opcao == 0:
                print('Programa encerrado ')
                break
            else:
                print(f'Digite uma opção {cor["vermelho"]}válido{cor["padrao"]}')
                sleep(1.5)
                continue        
    return opcao

# CADASTRAR TURNO 
def cadastro():
    # Entrada dos dados
    while True:
        limpartela()
        cabec(100,'Cadastrar turno')
        # Data do registro
        while True:
            limpartela()
            cabec(100,'Cadastrar turno')
            data_string = input(f"Informe a data do registro ({cor['azul']}DD/MM/AAAA{cor['padrao']}) ou aperte Enter para utilizar a data atual: ").strip()
            try:
                if data_string == '':
                    data = datetime.now().date().strftime("%d/%m/%Y")
                                    
                else:
                    data = datetime.strptime(data_string,"%d/%m/%Y").strftime("%d/%m/%Y")
                    
            except ValueError:
                print(f"Insira uma data válida no formato{cor['vermelho']} DD/MM/AAAA{cor['padrao']} para prosseguir")
                sleep(1.5)
            else:
                ano = datetime.strptime(data, "%d/%m/%Y").year
                if not datetime.now().year -1 <= ano <= datetime.now().year + 1:
                    print(f'O ano deve ser entre {cor["vermelho"]}{datetime.now().year -1}{cor["padrao"]} e {cor["vermelho"]}{datetime.now().year +1}{cor["padrao"]}. Tente novamente.')
                    sleep(1.5)
                    continue
                break

        # Turno (Manhã, Tarde, Noite)
        while True:
            limpartela()
            cabec(100,'Cadastrar turno')
            print(f'Data do registro: {cor["azul"]}{data}{cor["padrao"]}')
            try:    
                turno = int(input(f'Selecione o turno: \n{cor["azul"]}[1]{cor["padrao"]} Manhã \n{cor["azul"]}[2]{cor["padrao"]} Tarde \n{cor["azul"]}[3]{cor["padrao"]} Noite \nDigite o número da opção desejada: '))

            except ValueError:
                print(f'Entrada inválida. Escolha um {cor["vermelho"]}número{cor["padrao"]} da lista de turnos')
                sleep(1.5)
            else:
                if turno not in [1,2,3]:
                    print(f'{cor["vermelho"]}{turno}{cor["padrao"]} não corresponde a {cor["vermelho"]}nenhuma opção válida{cor["padrao"]}. Tente novamente.')
                    sleep(1.5)
                else:
                    break

        # Criar chave única composta
        id = (datetime.strptime(data,"%d/%m/%Y").strftime("%Y/%m/%d").replace('/','')) + str(turno)
        repositorio = carrega_txt()
        if int(id) in repositorio.keys(): #Evita duplicidade de registros
            print('Registro já realizado. Insira outros dados ou altere o registro existente.')
            sleep(1.5)
            continue
        else: 
            break

    
    # Nome do operador
    while True:
        limpartela()
        cabec(100,'Cadastrar turno')
        print(f'Data do registro: {cor["azul"]}{data}{cor["padrao"]}\nTurno: {cor["azul"]}{turno}{cor["padrao"]}')
        operador = input('Nome do operador: ').title()[:20]
        if len(operador) == 0:
            print(f'O campo nome é {cor["vermelho"]}obrigatório{cor["padrao"]}!')
            sleep(1.5)
        else:
            break

    # Produção do turno
    while True:
        limpartela()
        cabec(100,'Cadastrar turno')
        print(f'Data do registro: {cor["azul"]}{data}{cor["padrao"]}\nTurno: {cor["azul"]}{turno}{cor["padrao"]}\nNome do operador: {cor["azul"]}{operador}{cor["padrao"]}')
        try:
            producao = int(input('Produção do turno: '))
        except ValueError:
            print(f'Entrada inválida. Apenas {cor["vermelho"]}números{cor["padrao"]} são permitidos!')
            sleep(1.5)
        else:
            if producao < 0:
                print(f'Produção não pode ser um {cor["vermelho"]}valor negativo({producao}){cor["padrao"]}. Tente novamente!')
                sleep(1.5)
            else:
                break

    # Perdas do turno
    while True:
        limpartela()
        cabec(100,'Cadastrar turno')
        print(f'Data do registro: {cor["azul"]}{data}{cor["padrao"]}\nTurno: {cor["azul"]}{turno}{cor["padrao"]}\nNome do operador: {cor["azul"]}{operador}{cor["padrao"]}\nProdução do turno: {cor["azul"]}{producao}{cor["padrao"]}')
        try:
            perdas = int(input('Perdas do turno: '))
        except ValueError:
            print(f'Entrada inválida. Apenas {cor["vermelho"]}números{cor["padrao"]} são permitidos!')
            sleep(1.5)
        else:
            if perdas < 0:
                print(f'Perdas não pode ser um {cor["vermelho"]}valor negativo({perdas}){cor["padrao"]}. Tente novamente!')
                sleep(1.5)  
            elif perdas > producao:
                print('As perdas não podem ser superiores a produção')
                sleep(1.5)
            else:
                break

    # Calcula a taxa da meta atigida
    while True:
        limpartela()
        cabec(100,'Cadastrar turno')
        print(f'Data do registro: {cor["azul"]}{data}{cor["padrao"]}\nTurno: {cor["azul"]}{turno}{cor["padrao"]}\nNome do operador: {cor["azul"]}{operador}{cor["padrao"]}\nProdução do turno: {cor["azul"]}{producao}{cor["padrao"]}\nPerdas do turno: {cor["azul"]}{perdas}{cor["padrao"]}')
         # Se a meta não estiver cadastrada, redireciona para o menu de cadastro de metas
        try:
            d_metas = carrega_metas()
            taxa_meta = (f'{100*((producao)/d_metas[int(id[:6]+id[8:])]):.1f}')
        except:
            input(f'{cor['vermelho']}Meta ainda não definida para este turno deste mês.{cor['padrao']} Pressione Enter para ir ao menu de cadastro de metas.') 
            metas()
            continue
        else:
            break

    # Parada de equipamento (S/N)
    while True:
        limpartela()
        cabec(100,'Cadastrar turno')
        print(f'Data do registro: {cor["azul"]}{data}{cor["padrao"]}\nTurno: {cor["azul"]}{turno}{cor["padrao"]}\nNome do operador: {cor["azul"]}{operador}{cor["padrao"]}\nProdução do turno: {cor["azul"]}{producao}{cor["padrao"]}\nPerdas do turno: {cor["azul"]}{perdas}{cor["padrao"]}\nTaxa da meta atingida: {cor["azul"]}{taxa_meta}%{cor["padrao"]}')
        parada = input('Houve parada de equipamento neste turno? (S/N): ').strip().upper()
        if parada in ['S','N']:
            if parada == 'S':
                parada = 'Sim'
            else:
                parada = 'Não'              
            break
        else:
            print(f'Entrada inválida! Digite {cor["vermelho"]}S{cor["padrao"]} para Sim ou {cor["vermelho"]}N{cor["padrao"]} para não.')
            sleep(1.5)

    # Observações
    limpartela()
    cabec(100,'Cadastrar turno')
    print(f'Data do registro: {cor["azul"]}{data}{cor["padrao"]}\nTurno: {cor["azul"]}{turno}{cor["padrao"]}\nNome do operador: {cor["azul"]}{operador}{cor["padrao"]}\nProdução do turno: {cor["azul"]}{producao}{cor["padrao"]}\nPerdas do turno: {cor["azul"]}{perdas}{cor["padrao"]}\nTaxa da meta atingida: {cor["azul"]}{taxa_meta}%{cor["padrao"]}\nParada de equipamento: {cor["azul"]}{parada}{cor["padrao"]}')
    observacoes = input('Observações: ')[:40]

    # Adicionar o registro no repositório
    registro = (id,data,turno,operador,producao,perdas,d_metas[int(id[:6]+id[8:])],f'{float(taxa_meta):.2f}',parada,observacoes)
    linha = ','.join(str(item) for item in registro)
    inclui_txt(linha)
    limpartela()
    cabec(100,'Cadastrar turno')
    print(f'Data do registro: {cor["azul"]}{data}{cor["padrao"]}\nTurno: {cor["azul"]}{turno}{cor["padrao"]}\nNome do operador: {cor["azul"]}{operador}{cor["padrao"]}\nProdução do turno: {cor["azul"]}{producao}{cor["padrao"]}\nPerdas do turno: {cor["azul"]}{perdas}{cor["padrao"]}\nTaxa da meta atingida: {cor["azul"]}{taxa_meta}%{cor["padrao"]}\nParada de equipamento: {cor["azul"]}{parada}{cor["padrao"]}\nObservações: {cor["azul"]}{observacoes}{cor["padrao"]}')
    print('\nDados registrados com sucesso.')
    sleep(1.5)

# CONSULTA DOS REGISTROS
def consulta():
    limpartela()
    cabec(100,'Consulta de registros')
    repositorio = carrega_txt().items()

    # Entrada de data
    while True:
        limpartela()
        cabec(100,'Consulta de registros')
        data1 = input(f"Informe a data inicial ({cor['azul']}DD/MM/AAAA{cor['padrao']}): ").strip()
        try:
            data1 = datetime.strptime(data1, '%d/%m/%Y')
        except ValueError:
            print(f"Insira uma data válida no formato{cor['vermelho']} DD/MM/AAAA{cor['padrao']} para prosseguir")
            sleep(1.5)
        else:
            break
    while True:
        limpartela()
        cabec(100,'Consulta de registros')
        print(f'Data inicial: {cor["azul"]}{data1.strftime("%d/%m/%Y")}{cor["padrao"]}')
        data2 = input(f"Informe a data final ({cor['azul']}DD/MM/AAAA{cor['padrao']}): ").strip()
        try:
            data2 = datetime.strptime(data2, '%d/%m/%Y')
        except ValueError:
            print(f"Insira uma data válida no formato{cor['vermelho']} DD/MM/AAAA{cor['padrao']} para prosseguir")
            sleep(1.5)
        else:
            break

    # Entrada do turno
    while True:
        limpartela()
        cabec(100,'Consulta de registros')
        print(f'Data inicial: {cor["azul"]}{data1.strftime("%d/%m/%Y")}{cor["padrao"]}\nData final: {cor["azul"]}{data2.strftime("%d/%m/%Y")}{cor["padrao"]}')
        try:    
            turno = int(input(f'Selecione o turno: \n{cor["azul"]}[1]{cor["padrao"]} Manhã \n{cor["azul"]}[2]{cor["padrao"]} Tarde \n{cor["azul"]}[3]{cor["padrao"]} Noite \n{cor["azul"]}[0]{cor["padrao"]} Todos \nDigite o número da opção desejada: '))
        except ValueError:
            print(f'Entrada inválida. Escolha um {cor["vermelho"]}número{cor["padrao"]} da lista de turnos')
            sleep(1.5)
        else:
            if turno not in [1,2,3,0]:
                print(f'{cor["vermelho"]}{turno}{cor["padrao"]} não corresponde a {cor["vermelho"]}nenhuma opção válida{cor["padrao"]}. Tente novamente.')
                sleep(1.5)
            else:
                limpartela()
                cabec(100,'Consulta de registros')
                print('Gerando relatório...')
                sleep(1.5)
                break
                
    # Tabela com resultados (tabulate)
    cabecalho = ['Data', 'Turno', 'Operador', 'Produção', 'Perdas', 'Meta' , 'Desempenho (%)', 'Paradas', 'Observações']
    lista = list()
    limpartela()
    turnos = {1:'Manhã',2:'Tarde',3:'Noite'}
    prodtotal = perdtotal = 0

    for linha in [valores for chave, valores in repositorio]:
        if  data1 <= datetime.strptime(linha[0],'%d/%m/%Y') and data2 >= datetime.strptime(linha[0],'%d/%m/%Y') and turno == 0:
            prodtotal += linha[3]
            perdtotal += linha[4]
            linha[1] = turnos[linha[1]] # Converte número do turno para texto
            lista.append(linha)

        elif data1 <= datetime.strptime(linha[0],'%d/%m/%Y') and data2 >= datetime.strptime(linha[0],'%d/%m/%Y') and turno == linha[1]:
            prodtotal += linha[3]
            perdtotal += linha[4]
            linha[1] = turnos[linha[1]] # Converte número do turno para texto
            lista.append(linha)

    try:
        lista = sorted(lista, key=lambda x: x[0])
        print(tabulate(lista, headers=cabecalho, missingval="N/A", tablefmt="fancy_grid",colalign=("center","center","left","center","center","center","center","center","left")))
        # Rodapé com informações sobre o período definido
        print(f'Produção total: {prodtotal} \nPerdas totais: {perdtotal} \nMédia de produção diária: {prodtotal/((data2-data1).days + 1):.0f} \nPerdas médias diárias: {perdtotal/((data2-data1).days + 1):.0f}')
    except:
        cabec(100,'Consulta de registros')
        print('Nenhum resultado encontrado')
    input('\nPressione Enter para retornar ao menu principal ')

# METAS
def metas():
    metas_txt = carrega_metas()
    
    # Entrada do ano
    while True:
        limpartela()
        cabec(100,'Meta de produção')
        try:
            ano = int(input(f'Para qual ano você quer definir a meta? '))
        except:
            print(f'Digite um {cor["vermelho"]}número{cor["padrao"]} válido para o ano')
            sleep(1.5)
        else:
            if not int(datetime.now().strftime("%Y")) - 1 <= ano <= int(datetime.now().strftime("%Y")) + 1:
                print(f'O ano deve estar entre {cor["vermelho"]}{int(datetime.now().strftime("%Y"))- 1}{cor["padrao"]} e {cor["vermelho"]}{int(datetime.now().strftime("%Y"))+ 1}{cor["padrao"]}. Tente novamente.')
                sleep(1.5)
                continue
            break

    # Entrada do mês
    meses = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}
    turnos = {1:'Manhã',2:'Tarde',3:'Noite'}
    while True:
        limpartela()
        cabec(100,'Meta de produção')
        try:
            mes = int(input("Para qual mês você quer definir a meta? (Digite um número de 1 a 12): "))
        except:
            print(f'Digite um {cor["vermelho"]}número{cor["padrao"]} entre 1 e 12')
            sleep(1.5)
        else:
            if mes > 12 or mes < 1:
                print(f'Valor {cor["vermelho"]}fora do intervalo{cor["padrao"]}! O mês deve ser um número de 1 a 12.')
                sleep(1.5)
                continue
            elif len(str(mes)) == 1:
                mes = str(0) + str(mes)
            break


    # Entrada do turno
    while True:
        limpartela()
        cabec(100,'Meta de produção')
        try:    
            turno = int(input(f'Selecione o turno de {cor["azul"]}{meses[int(mes)]}{cor["padrao"]}: \n{cor["azul"]}[1]{cor["padrao"]} Manhã \n{cor["azul"]}[2]{cor["padrao"]} Tarde \n{cor["azul"]}[3]{cor["padrao"]} Noite \nDigite o número da opção desejada: '))

        except ValueError:
            print(f'Entrada inválida. Escolha um {cor["vermelho"]}número{cor["padrao"]} da lista de turnos')
            sleep(1.5)
        else:
            if turno not in [1,2,3]:
                print(f'{cor["vermelho"]}{turno}{cor["padrao"]} não corresponde a {cor["vermelho"]}nenhuma opção válida{cor["padrao"]}. Tente novamente.')
                sleep(1.5)
            else:
                break
    
    # Cria o ID
    id_meta = str(ano) + str(mes) + str(turno)  

    # Define a meta
    while True:
        limpartela()
        cabec(100,'Meta de produção')
        if int(id_meta) in metas_txt.keys():
            print(f'Já existe uma meta cadastrada para {meses[int(mes)]} de {ano}, turno {turnos[turno]}: {cor["azul"]}{metas_txt[int(id_meta)]}{cor["padrao"]}')
            sleep(3)
            break
        try:
            meta = int(input(f'Meta de produção: '))
        except:
            print(f'Erro. Digite um {cor["vermelho"]}número{cor["padrao"]}')
            sleep(1.5)
        else:
            if meta < 0:
                print('Valor inválido. Tente novamente')
                sleep(1.5)
            else:
                while True:
                    limpartela()
                    cabec(100,'Meta de produção')
                    print(f'Ano selecionado: {cor["azul"]}{ano}{cor["padrao"]}\n'
                        f'Mês selecionado: {cor["azul"]}{meses[int(mes)]}{cor["padrao"]}\n'
                        f'Turno: {cor["azul"]}{turnos[turno]}{cor["padrao"]}\n'
                        f'Meta: {cor["azul"]}{meta}{cor["padrao"]}')
                    
                    confirma = input('Confirmar (S/N)? ').upper().strip()
                    if confirma not in ['S','N']:
                        print(f'Entrada inválida! Digite {cor["vermelho"]}S{cor["padrao"]} para Confirmar ou {cor["vermelho"]}N{cor["padrao"]} para Cancelar.')
                        sleep(1.5)
                    elif confirma == 'N':
                        print(f'{cor["vermelho"]}Cadastro cancelado{cor["padrao"]}.')
                        sleep(1.5)
                        break
                    else:
                        # Sobrescreve metas.txt com o novo registro
                        metas_txt[int(id_meta)] = meta
                        write_metas(metas_txt)
                        print('Cadastro realizado com sucesso.')
                        sleep(1.5)
                        break
        break

# ALTERAR REGISTRO
def altera_registro():
    registros = carrega_txt()

    # Entrada de data
    while True:
        limpartela()
        cabec(100,'Alterar registro')
        data = input(f"Data do registro ({cor['azul']}DD/MM/AAAA{cor['padrao']}): ").strip()
        try:
            data = datetime.strptime(data,"%d/%m/%Y").strftime("%d/%m/%Y")
        except ValueError:
            print(f"Insira uma data válida no formato{cor['vermelho']} DD/MM/AAAA{cor['padrao']} para prosseguir")
            sleep(1.5)
        else:
            break

    # Entrada do turno
    while True:
        limpartela()
        cabec(100,'Alterar registro')
        print(f'Data do registro: {cor["azul"]}{data}{cor["padrao"]}')
        try:    
            turno = int(input(f'Selecione o turno: \n{cor["azul"]}[1]{cor["padrao"]} Manhã \n{cor["azul"]}[2]{cor["padrao"]} Tarde \n{cor["azul"]}[3]{cor["padrao"]} Noite \nDigite o número da opção desejada: '))
        except ValueError:
            print(f'Entrada inválida. Escolha um {cor["vermelho"]}número{cor["padrao"]} da lista de turnos')
            sleep(1.5)
        else:
            if int(turno) not in [1,2,3]:
                print(f'{cor["vermelho"]}{turno}{cor["padrao"]} não corresponde a {cor["vermelho"]}nenhuma opção válida{cor["padrao"]}. Tente novamente.')
                sleep(1.5)
            else:
                break

    # Cria a chave composta
    id = int((datetime.strptime(data,"%d/%m/%Y").strftime("%Y/%m/%d").replace('/','')) + str(turno))
    
    while True:
        limpartela()
        cabec(100,'Alterar registro')
        # Verifica se o ID existe
        if id not in registros:
            print(f'{cor["vermelho"]}Registro inexistente{cor["padrao"]}')
            print('Retornando ao menu principal ')
            sleep(1.5)
            break
        else:
            # Escolha do campo a ser alterado
            while True:
                limpartela()
                cabec(100,'Alterar registro')
                print(f'Alterando registro de data: {cor["azul"]}{data}{cor["padrao"]} turno: {cor["azul"]}{turno}{cor["padrao"]}\n')
                try:
                    opcao = int(input(f'''Qual campo deseja alterar?  
{cor["azul"]}[1]{cor["padrao"]} Operador
{cor["azul"]}[2]{cor["padrao"]} Produção
{cor["azul"]}[3]{cor["padrao"]} Perdas
{cor["azul"]}[4]{cor["padrao"]} Parada de equipamento
{cor["azul"]}[5]{cor["padrao"]} Observações
{cor["azul"]}[0]{cor["padrao"]} Cancelar
'''))
                except:
                    print(f'Digite um {cor['vermelho']}número{cor['padrao']} válido')
                    sleep(1.5)
                else:    
                    if opcao > 5 or opcao < 0:
                        print(f'Escolha uma opção válida ({cor["vermelho"]}0 a 5{cor["padrao"]})')
                        sleep(1.5)
                        continue
                    
                    # Sair
                    if opcao == 0:
                        break

                    # Operador
                    if opcao == 1:
                        while True:
                            limpartela()
                            cabec(100,'Alterar registro')
                            registros[id][2] = input('Nome do operador: ').title()[:20]
                            if len(registros[id][2]) == 0:
                                print(f'O campo nome é {cor["vermelho"]}obrigatório{cor["padrao"]}!')
                                sleep(1.5)
                            else:
                                print(f'Campo Operador alterado com sucesso')
                                sleep(1.5)
                                break

                    # Produção
                    elif opcao == 2:
                            while True:
                                limpartela()
                                cabec(100,'Alterar registro')
                                try:
                                    registros[id][3] = int(input('Produção do turno: '))
                                except ValueError:
                                    print(f'Entrada inválida. Apenas {cor["vermelho"]}números{cor["padrao"]} são permitidos!')
                                    sleep(1.5)
                                else:
                                    if registros[id][3] < 0:
                                        print(f'Produção não pode ser um {cor["vermelho"]}valor negativo({registros[id][3]}){cor["padrao"]}. Tente novamente!')
                                        sleep(1.5)
                                    else:
                                        print(f'Campo Produção alterado com sucesso')
                                        sleep(1.5)
                                        break
                                
                            # Recalculo do desempenho
                            registros[id][6] = round(100*(registros[id][3]/registros[id][5]),2)
                    # Perdas                            
                    elif opcao == 3:
                        while True:
                            limpartela()
                            cabec(100,'Alterar registro')
                            try:
                                registros[id][4] = int(input('Perdas do turno: '))
                            except ValueError:
                                print(f'Entrada inválida. Apenas {cor["vermelho"]}números{cor["padrao"]} são permitidos!')
                                sleep(1.5)
                            else:
                                if registros[id][4] < 0:
                                    print(f'Perdas não pode ser um {cor["vermelho"]}valor negativo({registros[id][4]}){cor["padrao"]}. Tente novamente!')
                                    sleep(1.5)
                                elif registros[id][4] > registros[id][3]:
                                    print('As perdas não podem ser superiores a produção')
                                    sleep(1.5)
                                else:
                                    print(f'Campo Perdas alterado com sucesso')
                                    sleep(1.5)
                                    break
                        # Recalculo do desempenho
                        registros[id][6] = round(100*(registros[id][3]/registros[id][5]),2)

                    # Parada de equipamento                 
                    elif opcao == 4:
                        while True:
                            limpartela()
                            cabec(100,'Alterar registro')
                            registros[id][7] = input('Houve parada de equipamento neste turno? (S/N): ').strip().upper()
                            if registros[id][7] in ['S','N']:
                                if registros[id][7] == 'S':
                                    registros[id][7] = 'Sim'
                                else:
                                    registros[id][7] = 'Não'              
                                print(f'Campo Parada de equipamento alterado com sucesso')
                                break
                            else:
                                print(f'Entrada inválida! Digite {cor["vermelho"]}S{cor["padrao"]} para Sim ou {cor["vermelho"]}N{cor["padrao"]} para não.')
                                sleep(1.5)
                        
                    # Observações    
                    elif opcao == 5:
                        limpartela()
                        cabec(100,'Alterar registro')
                        registros[id][8] = input('Observações: ')[:40]
                        print(f'Campo Observações alterado com sucesso')
                        sleep(1.5)
            
                    # Sobrescreve repositório        
                    print('Atualizando registro...')
                    sleep(1.5)
                    write_repo(registros)
                    break
            break

# EXCLUIR REGISTRO
def exclui_registro():
    registros = carrega_txt()
    while True:
        # Entrada de data
        while True:
            limpartela()
            cabec(100,'Excluir registro')
            data = input(f"Data do registro ({cor['azul']}DD/MM/AAAA{cor['padrao']}): ").strip()
            try:
                data = datetime.strptime(data,"%d/%m/%Y").strftime("%d/%m/%Y")
            except ValueError:
                print(f"Insira uma data válida no formato{cor['vermelho']} DD/MM/AAAA{cor['padrao']} para prosseguir")
                sleep(1.5)
            else:
                break

        # Entrada do turno
        while True:
            limpartela()
            cabec(100,'Excluir registro')
            try:    
                turno = int(input(f'Selecione o turno: \n{cor["azul"]}[1]{cor["padrao"]} Manhã \n{cor["azul"]}[2]{cor["padrao"]} Tarde \n{cor["azul"]}[3]{cor["padrao"]} Noite \nDigite o número da opção desejada: '))

            except ValueError:
                print(f'Entrada inválida. Escolha um {cor["vermelho"]}número{cor["padrao"]} da lista de turnos')
                sleep(1.5)
            else:
                if int(turno) not in [1,2,3]:
                    print(f'{cor["vermelho"]}{turno}{cor["padrao"]} não corresponde a {cor["vermelho"]}nenhuma opção válida{cor["padrao"]}. Tente novamente.')
                    sleep(1.5)
                else:
                    break

        # Cria a chave composta
        id = int((datetime.strptime(data,"%d/%m/%Y").strftime("%Y/%m/%d").replace('/','')) + str(turno))
        break

    if id in registros:
        print(f'Registro encontrado')
        while True:
            limpartela()
            cabec(100,'Excluir registro')
            print(f'Dados do registro:\n'
                  f'Data: {cor["vermelho"]}{registros[id][0]}{cor["padrao"]}\n'
                  f'Turno: {cor["vermelho"]}{registros[id][1]}{cor["padrao"]}\n'
                  f'Operador: {cor["vermelho"]}{registros[id][2]}{cor["padrao"]}\n'
                  f'Produção: {cor["vermelho"]}{registros[id][3]}{cor["padrao"]}\n'
                  f'Perdas: {cor["vermelho"]}{registros[id][4]}{cor["padrao"]}\n'
                  f'Meta: {cor["vermelho"]}{registros[id][5]}{cor["padrao"]}\n'
                  f'Desempenho (%): {cor["vermelho"]}{registros[id][6]}{cor["padrao"]}\n'
                  f'Paradas: {cor["vermelho"]}{registros[id][7]}{cor["padrao"]}\n'
                  f'Observações: {cor["vermelho"]}{registros[id][8]}{cor["padrao"]}\n')
            permissao = input(f'Está ação é {cor["vermelho"]}IRREVERSÍVEL{cor["padrao"]}. Deseja continuar (S/N)? ').upper()
            if permissao not in ['S','N']:
                print(f'Digite {cor["vermelho"]}S{cor["padrao"]} para confirmar ou {cor["vermelho"]}N{cor["padrao"]} para cancelar ')
                sleep(1.5)
            elif permissao == 'S':
                del registros[id]
                write_repo(registros)
                print('Excluindo o registro...')
                sleep(1.5)
                break
            elif permissao == 'N':
                print('Operação cancelada.')
                sleep(1.5)
                break
            else:
                print('Opção inválida')
                sleep(1.5)
    else:
        print(f'Registro não encontrado.')
        sleep(1.5)
        
# RELATÓRIO GERAL
def relatorio():
    limpartela()
    cabec(141,'Relatório geral')
    dados = list(carrega_txt().values())
    dados = sorted(dados, key=lambda x: x[1]) # Ordena a lista por turno como int
    turnos = {1:'Manhã',2:'Tarde',3:'Noite'}
    for registro in dados:
        registro[1] = turnos[registro[1]] 
    
    dados = sorted(dados, key=lambda x: x[0]) # Ordena a lista ordenada por data
    cabecalho = ['Data', 'Turno', 'Operador', 'Produção', 'Perdas', 'Meta' , 'Desempenho (%)', 'Paradas', 'Observações']
    
    prodtotal = perdtotal = 0
    print(tabulate(dados,headers=cabecalho,tablefmt="fancy_grid",colalign=("center","center","left","center","center","center","center","center","left")))
    input('Pressione Enter para retornar ao menu principal ')