# -*- coding:utf-8 -*-
from typing import List
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import datetime
import json
import matplotlib.pyplot as plt

plt.style.use('ggplot')

janela_atual = None
janela_login = None
tela_escolha_solicitacoes_usuario = None
tela_escolha_chamados_avaliacao = None
tela_mensagem_erro_chamados_avaliacao = None
tela_mensagem_erro_chamados = None
tela_confirmacao_atualizar_dados_usuario = None
tela_mensagem_login = None
tela_confirmacao_av = None
tela_confirmacao_chamado = None
tela_mensagem_erro_minha_conta = None
tela_mensagem_erro_confirmacao_chamado = None
tela_mensagem_erro_confirmacao_avaliacao = None
tela_mensagem_zero_chamados = None
contador_login: int = 0
email_verif: str = ""


# A função "fechando_janelas_secundarias" encerra todas as janelas secundárias quando da abertura de uma nova janela
def fechando_janelas_secundarias():
    global tela_escolha_solicitacoes_usuario
    global tela_escolha_chamados_avaliacao
    global tela_mensagem_erro_chamados_avaliacao
    global tela_mensagem_erro_chamados
    global tela_mensagem_login
    global tela_confirmacao_av
    global tela_confirmacao_chamado
    global tela_confirmacao_atualizar_dados_usuario
    global tela_mensagem_erro_minha_conta
    global tela_mensagem_erro_confirmacao_chamado
    global tela_mensagem_erro_confirmacao_avaliacao
    global tela_mensagem_zero_chamados

    if tela_escolha_solicitacoes_usuario is not None:
        try:
            tela_escolha_solicitacoes_usuario.destroy()
        except:
            pass
    if tela_escolha_chamados_avaliacao is not None:
        try:
            tela_escolha_chamados_avaliacao.destroy()
        except:
            pass
    if tela_mensagem_erro_chamados_avaliacao is not None:
        try:
            tela_mensagem_erro_chamados_avaliacao.destroy()
        except:
            pass
    if tela_mensagem_erro_chamados is not None:
        try:
            tela_mensagem_erro_chamados.destroy()
        except:
            pass
    if tela_mensagem_login is not None:
        try:
            tela_mensagem_login.destroy()
        except:
            pass
    if tela_confirmacao_av is not None:
        try:
            tela_confirmacao_av.destroy()
        except:
            pass
    if tela_confirmacao_chamado is not None:
        try:
            tela_confirmacao_chamado.destroy()
        except:
            pass
    if tela_confirmacao_atualizar_dados_usuario is not None:
        try:
            tela_confirmacao_atualizar_dados_usuario.destroy()
        except:
            pass
    if tela_mensagem_erro_minha_conta is not None:
        try:
            tela_mensagem_erro_minha_conta.destroy()
        except:
            pass
    if tela_mensagem_erro_confirmacao_chamado is not None:
        try:
            tela_mensagem_erro_confirmacao_chamado.destroy()
        except:
            pass
    if tela_mensagem_erro_confirmacao_avaliacao is not None:
        try:
            tela_mensagem_erro_confirmacao_avaliacao.destroy()
        except:
            pass
    if tela_mensagem_zero_chamados is not None:
        try:
            tela_mensagem_zero_chamados.destroy()
        except:
            pass


# A função "fechando_janela_login" encerra as janelas de login secundárias que o usuário poderia abrir incorretamente
def fechando_janela_login():
    global janela_login
    if janela_login is not None:
        try:
            janela_login.destroy()
        except:
            pass


# A função "fechando_janela_atual" encerra todas as instâncias de janela_atual abertas quando da criação
# de uma nova janela
def fechando_janela_atual():
    global janela_atual
    if janela_atual is not None:
        try:
            janela_atual.destroy()
        except:
            pass


# Função para formatar a data e hora (dia-mês-ano e hora-min-seg)
def data_e_hora_formatada() -> str:
    data_e_hora: datetime = datetime.datetime.now()
    return data_e_hora.strftime("%d-%m-%Y %H:%M:%S")


# A função "validar_entrada_numero" checa se uma string é numérica
def validar_entrada_numero(senha: str) -> bool:
    verif_num = False
    if senha.isnumeric():
        verif_num = True
    return verif_num


# A função "validar_entrada_str_av" checa se o usuário selecionou alguma opção na área de avaliação de chamados
def validar_entrada_str_av(entrada: str) -> bool:
    verif_entrada = True
    if entrada == "Selecione":
        verif_entrada = False
    return verif_entrada


# A função "validar_entrada_str" checa a existência de uma string vazia
def validar_entrada_str(entrada: str) -> bool:
    verif_entrada = True
    if entrada == "":
        verif_entrada = False
    return verif_entrada


# A função "retirandoEspacos" recebe uma string e devolve uma lista com todos os números contidos nessa string
# após retirar os espaços entre os números
def retirando_espacos(entrada: str) -> List[int]:
    conjunto_termos = []
    termo = ""
    for caractere in entrada:
        if caractere == " " and termo != "":
            conjunto_termos.append(int(termo))
            termo = ""
        elif caractere != " ":
            termo += caractere
    if termo != "":
        conjunto_termos.append(int(termo))
    return conjunto_termos


# S-GEMAPy Módulo Gestor (Em construção)
# O módulo gestor será construído a posteiori


# A função "tela_opcoes_area_gestor" apresenta a primeira tela da área do gestor onde é possível escolher a
# atividade que se deseja realizar
def tela_opcoes_area_gestor():
    global janela_atual
    fechando_janela_atual()
    fechando_janela_login()

    janela_atual = Tk()
    janela_atual.title("S-GEMAPy - Área do gestor")
    janela_atual.iconbitmap("icon.ico")
    janela_atual["bg"] = "white"
    janela_atual.geometry("800x600+250+50")
    janela_atual.resizable(width=False, height=False)

    # Label com a indicação do acesso a área do gestor
    lb1_t4 = Label(janela_atual, text="S-GEMAPy: Área do Gestor", background="white",
                   font="ComicSansMS 16 bold")
    lb1_t4.place(x=258, y=125)

    # Label com texto explicativo sobre as opções disponíveis para área do gestor
    lb2_t4 = Label(janela_atual, text="Este módulo está em construção!",
                   background="white", font="ComicSansMS 14")
    lb2_t4.place(x=259, y=200)

    # Label com imagem informando que o módulo está em construção
    img_temp = Image.open("coming_soon.gif")
    img_cs = ImageTk.PhotoImage(img_temp)
    lb3_t4 = Label(janela_atual, image=img_cs, borderwidth=0, highlightthickness=0)
    lb3_t4.place(x=272, y=250)

    # Botão para voltar para a tela de escolha da área (usuário ou gestor)
    img_bt1_t4_temp = Image.open("back.gif")
    img_bt1_t4 = ImageTk.PhotoImage(img_bt1_t4_temp)
    bt1_t4 = Button(janela_atual, height=20, width=75, text="Voltar", image=img_bt1_t4, compound=LEFT,
                    background="white", font="ComicSansMS 12 bold", command=tela_escolha_area)
    bt1_t4.place(x=675, y=550)

    janela_atual.mainloop()


# S-GEMAPy Módulo Usuário (100% concluído)


# A função "total_chamados_por_situação" retorna uma string com a quantidade de chamados por situação separados por um
# espaço vazio
def total_chamados_por_situacao() -> str:
    total_chamados_nao_definidos: int = 0
    total_chamados_em_analise: int = 0
    total_chamados_agendados: int = 0
    total_chamados_encerrados: int = 0
    total_chamados_avaliados: int = 0
    arquivo_busca_chamados_json: json = None
    try:
        # O arquivo "chamados.json" armazena um dicionário que tem como chave os números dos chamados cadastrados
        # no sistema e como valores a associados a chave as informações associadas aos chamados
        arquivo_busca_chamados_json = open('chamados.json', 'r', encoding='latin-1')
        dados_arquivo_busca_chamado_json = json.load(arquivo_busca_chamados_json)
        for chamado in dados_arquivo_busca_chamado_json:
            if dados_arquivo_busca_chamado_json[chamado][8] == email_verif:
                if dados_arquivo_busca_chamado_json[chamado][10] == "Não definida":
                    total_chamados_nao_definidos += 1
                elif dados_arquivo_busca_chamado_json[chamado][10] == "Solicitação em análise":
                    total_chamados_em_analise += 1
                elif dados_arquivo_busca_chamado_json[chamado][10] == "Solicitação agendada":
                    total_chamados_agendados += 1
                elif dados_arquivo_busca_chamado_json[chamado][10] == "Solicitação encerrada":
                    total_chamados_encerrados += 1
                elif dados_arquivo_busca_chamado_json[chamado][10] == "Avaliado":
                    total_chamados_avaliados += 1
                    #    except:
    #        print("Não foi possível ler o arquivo JSON que armazena os chamados cadastradas no sistema. "
    #              "Esse arquivo precisa estar acessível no mesmo diretório que o programa.")
    finally:
        if arquivo_busca_chamados_json:
            arquivo_busca_chamados_json.close()

    return str(total_chamados_nao_definidos) + " " + str(total_chamados_em_analise) + " " + \
           str(total_chamados_agendados) + " " + str(total_chamados_encerrados) + " " + str(total_chamados_avaliados)


# A função "numero_chamados_por_situacao" retorna um gráfico apresentando o número de chamados por situação
def numero_chamados_por_situacao() -> plt:
    global tela_mensagem_zero_chamados
    chamados_str: str = total_chamados_por_situacao()
    num_chamados: List[int] = retirando_espacos(chamados_str)
    if sum(num_chamados) != 0:
        situacao: List[str] = ['Situação não definida', 'Em análise', 'Agendados', 'Encerrados', 'Avaliados',
                               "Nº Total de chamados"]
        chamados: List[int] = [num_chamados[0], num_chamados[1], num_chamados[2], num_chamados[3], num_chamados[4],
                               sum(num_chamados)]
        situacao_pos = [i for i, _ in enumerate(situacao)]
        plt.barh(situacao_pos, chamados, color=['#A83D39', '#F1F584', '#F5706C', '#53ADF5', '#427BA8', '#52A889'],
                 edgecolor='black')
        plt.ylabel("Situação")
        plt.xlabel("Número de chamados")
        plt.title(" Número de chamados por situação ")

        plt.yticks(situacao_pos, situacao)

        plt.show()
    else:
        tela_mensagem_zero_chamados = Tk()
        tela_mensagem_zero_chamados.title("Error")
        tela_mensagem_zero_chamados.geometry("300x50+500+325")
        tela_mensagem_zero_chamados.iconbitmap("icon_error.ico")
        lb_tmzc = Label(tela_mensagem_zero_chamados, text="\nNão há chamados registrados!\n", font="ComicSansMS 12")
        lb_tmzc.pack()
        tela_mensagem_zero_chamados.mainloop()


# A função "percentual_chamados_por_situacao" retorna um gráfico apresentando o percentual de chamados por situação
def percentual_chamados_por_situacao() -> plt:
    global tela_mensagem_zero_chamados
    chamados_str: str = total_chamados_por_situacao()
    num_chamados: List[int] = retirando_espacos(chamados_str)
    if sum(num_chamados) != 0:
        labels = 'Situação não definida', 'Em análise', 'Agendado', 'Encerrado', 'Avaliado'
        sizes = [num_chamados[0], num_chamados[1], num_chamados[2], num_chamados[3], num_chamados[4]]
        fig1, ax1 = plt.subplots()
        colors = ['#52A889', '#F1F584', '#F5706C', '#53ADF5', '#427BA8']
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, shadow=True, startangle=90)
        ax1.axis('equal')
        plt.title(" % de chamados por situação")

        plt.show()
    else:
        tela_mensagem_zero_chamados = Tk()
        tela_mensagem_zero_chamados.title("Error")
        tela_mensagem_zero_chamados.geometry("300x50+500+325")
        tela_mensagem_zero_chamados.iconbitmap("icon_error.ico")
        lb_tmzc = Label(tela_mensagem_zero_chamados, text="\nNão há chamados registrados!\n", font="ComicSansMS 12")
        lb_tmzc.pack()
        tela_mensagem_zero_chamados.mainloop()


# A função "tela_dashboard" apresenta a tela onde usuário pode escolher as métricas dos registros de solicitações
# que deseja visualizar
def tela_dashboard():
    global janela_atual
    fechando_janela_atual()
    fechando_janela_login()

    janela_atual = Tk()
    janela_atual.title("S-GEMAPy")
    janela_atual.iconbitmap("icon.ico")
    janela_atual["bg"] = "white"
    janela_atual.geometry("800x600+250+50")
    janela_atual.resizable(width=False, height=False)

    # Label com a logo do sistema
    logo_temp2 = Image.open("logo.gif")
    logo2 = ImageTk.PhotoImage(logo_temp2)
    lb0_tdb = Label(janela_atual, image=logo2)
    lb0_tdb.place(x=214, y=75)

    # Texto explicativo para direcionar escolha da área
    lb1_tdb = Label(janela_atual, text="Dashboard", background="white", font="ComicSansMS 14 bold")
    lb1_tdb.place(x=350, y=225)

    # Texto explicativo para direcionar escolha da área
    lb2_tdb = Label(janela_atual, text="Clique nos ícones abaixo para visualizar indicadores das suas solicitações",
                    background="white", font="ComicSansMS 12")
    lb2_tdb.place(x=141, y=260)

    # Botão para visualizar o indicador número de chamados x status
    img_bt1_tdb_temp = Image.open("DB1.gif")
    img_bt1_tdb = ImageTk.PhotoImage(img_bt1_tdb_temp)
    bt1_tdb = Button(janela_atual, height=175, width=250, text="\nPercentual de chamados\npor Status",
                     image=img_bt1_tdb, compound=TOP, background="white", font="ComicSansMS 12 bold",
                     command=percentual_chamados_por_situacao)
    bt1_tdb.place(x=94, y=325)

    # Botão para visualizar o indicador % de chamados x status
    img_bt2_tdb_temp = Image.open("DB2.gif")
    img_bt2_tdb = ImageTk.PhotoImage(img_bt2_tdb_temp)
    bt2_tdb = Button(janela_atual, height=175, width=250, text="\nNúmero de chamados\npor status",
                     image=img_bt2_tdb, compound=TOP, background="white", font="ComicSansMS 12 bold",
                     command=numero_chamados_por_situacao)
    bt2_tdb.place(x=446, y=325)

    # Botão para voltar para a área do usuário
    img_bt3_tdb_temp = Image.open("back.gif")
    img_bt3_tdb = ImageTk.PhotoImage(img_bt3_tdb_temp)
    bt3_tdb = Button(janela_atual, height=20, width=75, text="Voltar", image=img_bt3_tdb, compound=LEFT,
                     background="white", font="ComicSansMS 12 bold", command=tela_opcoes_area_usuario)
    bt3_tdb.place(x=675, y=550)

    janela_atual.mainloop()


# A função "destroy_window" fecha a janela de confirmaçao de alteração dos dados aberta na
# função atualizar_dados_minha_conta_usuario
def destroy_window():
    tela_confirmacao_atualizar_dados_usuario.destroy()


# A função "validar_entradas_minha_conta" checa se todas as entradas são válidas
def validar_entradas_minha_conta() -> bool:
    verif_entradas_minha_conta = False
    if validar_entrada_str(ent6_t11.get()) and validar_entrada_str(ent1_t11.get()) and \
            validar_entrada_str(ent2_t11.get()) and validar_entrada_str(ent3_t11.get()) and \
            validar_entrada_numero(ent3_t11.get()) and validar_entrada_str(ent4_t11.get()) and \
            validar_entrada_numero(ent4_t11.get()) and validar_entrada_str(ent5_t11.get()) and \
            validar_entrada_numero(ent5_t11.get()) and validar_entrada_str(clicked_plano.get()) and \
            validar_entrada_str(ent8_t11.get()) and validar_entrada_numero(ent8_t11.get()):
        verif_entradas_minha_conta = True
    return verif_entradas_minha_conta


# A função "atualizar_dados_minha_conta_usuario" registra os dados alterados pelo usuário na função
# "editar_tela_minha_conta_area_usuario"
def atualizar_dados_minha_conta_usuario():
    global email_verif
    global tela_mensagem_erro_minha_conta
    global tela_confirmacao_atualizar_dados_usuario

    if validar_entradas_minha_conta():
        try:
            # O arquivo "users_cadastro.json" armazena um dicionário que tem como chave o email do usuário e
            # como valores associados a chave os dados cadastrais do usuário
            with open('users_cadastro.json', "r") as file:
                dados = json.load(file)
                del dados[email_verif]
            with open('users_cadastro.json', "w") as file:
                new_data = {ent6_t11.get(): [ent1_t11.get(), ent2_t11.get(), ent3_t11.get(), ent4_t11.get(),
                                             ent5_t11.get(), ent6_t11.get(), clicked_plano.get(), ent8_t11.get(),
                                             data_e_hora_formatada()]}
                dados.update(new_data)
                file.seek(0)
                json.dump(dados, file, ensure_ascii=False, indent=4)
        except:
            print("Não foi possível ler o arquivo JSON que armazena os dados dos usuários cadastradas no sistema. "
                  "Esse arquivo precisa estar acessível no mesmo diretório que o programa.")

        email_verif = ent6_t11.get()
        fechando_janelas_secundarias()
        tela_confirmacao_atualizar_dados_usuario = Tk()
        tela_confirmacao_atualizar_dados_usuario["bg"] = "white"
        tela_confirmacao_atualizar_dados_usuario.title("S-GEMAPy")
        tela_confirmacao_atualizar_dados_usuario.geometry("500x125+400+300")
        tela_confirmacao_atualizar_dados_usuario.iconbitmap("icon_log.ico")
        lb1_tcadu = Label(tela_confirmacao_atualizar_dados_usuario,
                          text="\nSeus dados cadastrais foram atualizados com sucesso!\n", background="white",
                          font="ComicSansMS 12")
        lb1_tcadu.pack()

        bt1_tcadu = Button(tela_confirmacao_atualizar_dados_usuario, width=5, text="OK!",
                           background="white", font="ComicSansMS 12", command=destroy_window)
        bt1_tcadu.pack()

        tela_confirmacao_atualizar_dados_usuario.mainloop()
    else:
        fechando_janelas_secundarias()
        tela_mensagem_erro_minha_conta = Tk()
        tela_mensagem_erro_minha_conta.title("Error")
        tela_mensagem_erro_minha_conta.geometry("300x75+500+325")
        tela_mensagem_erro_minha_conta.iconbitmap("icon_error.ico")
        lb2_tmemc = Label(tela_mensagem_erro_minha_conta, text="\nEntradas inválidas:\n"
                                                               "Corrija os dados inseridos!", font="ComicSansMS 12")
        lb2_tmemc.pack()
        tela_mensagem_erro_minha_conta.mainloop()


# A função "editar_tela_minha_conta_area_usuario" apresenta a tela onde o usuário poderá alterar os dados cadastrais
def editar_tela_minha_conta_area_usuario():
    fechando_janelas_secundarias()
    global janela_atual
    fechando_janela_atual()
    global ent1_t11
    global ent2_t11
    global ent3_t11
    global ent4_t11
    global ent5_t11
    global ent6_t11
    global clicked_plano
    global ent8_t11

    dados_user = []

    arquivo_cadastro_users_json = None

    try:
        # O arquivo "users_cadastro.json" armazena um dicionário que tem como chave o email do usuário e como valores
        # associados a chave os dados cadastrais do usuário
        arquivo_cadastro_users_json = open('users_cadastro.json', 'r')
        dados_cadastro_users_json = json.load(arquivo_cadastro_users_json)
        for email_usuario in dados_cadastro_users_json:
            if email_usuario == email_verif:
                dados_user = dados_cadastro_users_json[email_usuario]
    except:
        print("Não foi possível ler o arquivo JSON que armazena os dados dos usuários cadastradas no sistema. "
              "Esse arquivo precisa estar acessível no mesmo diretório que o programa.")
    finally:
        if arquivo_cadastro_users_json:
            arquivo_cadastro_users_json.close()

    janela_atual = Tk()
    janela_atual.title("S-GEMAPy - Área do usuário: Minha Conta")
    janela_atual.iconbitmap("icon.ico")
    janela_atual["bg"] = "white"
    janela_atual.geometry("800x600+250+50")
    janela_atual.resizable(width=False, height=False)

    # Label com texto explicativo ao usuário sobre a alteração de dados
    lb_t11 = Label(janela_atual, text="Faça a alteração dos dados e clique no botão 'Salvar'",
                   background="white", font="ComicSansMS 14")
    lb_t11.place(x=175, y=25)

    # Label com texto explicativo sobre o preenchimento dos dados
    lb0_t11 = Label(janela_atual, text="* Todos os campos devem ser obrigatoriamente preenchidos",
                    background="white", font="ComicSansMS 10")
    lb0_t11.place(x=50, y=75)

    # Label com texto explicativo sobre o preenchimento dos dados
    lb1_t11 = Label(janela_atual, text="* Os campos CEP, Telefone principal e secundário e Senha"
                                       " devem conter apenas dígitos numéricos",
                    background="white", font="ComicSansMS 10")
    lb1_t11.place(x=50, y=100)

    # Label com a indicação do nome do usuario
    lb2_t10 = Label(janela_atual, text="Nome", background="white", font="ComicSansMS 12 bold")
    lb2_t10.place(x=50, y=150)

    # Caixa para edição do nome do usuario
    ent1_t11 = Entry(janela_atual, width=70, font="ComicSansMS 10")
    ent1_t11.insert(0, dados_user[0])
    ent1_t11.place(x=250, y=150)

    # Label com a indicação do endereço do usuario
    lb3_t10 = Label(janela_atual, text="Endereço", background="white", font="ComicSansMS 12 bold")
    lb3_t10.place(x=50, y=200)

    # Caixa para edição do endereço do usuario
    ent2_t11 = Entry(janela_atual, width=70, font="ComicSansMS 10")
    ent2_t11.insert(0, dados_user[1])
    ent2_t11.place(x=250, y=200)

    # Label com a indicação do CEP do usuário
    lb4_t10 = Label(janela_atual, text="CEP", background="white", font="ComicSansMS 12 bold")
    lb4_t10.place(x=50, y=250)

    # Caixa para edição do CEP do usuario
    ent3_t11 = Entry(janela_atual, width=70, font="ComicSansMS 10")
    ent3_t11.insert(0, dados_user[2])
    ent3_t11.place(x=250, y=250)

    # Label com a indicação do telefone para contato do usuário
    lb5_t10 = Label(janela_atual, text="Telefone principal", background="white", font="ComicSansMS 12 bold")
    lb5_t10.place(x=50, y=300)

    # Caixa para edição do telefone do usuario
    ent4_t11 = Entry(janela_atual, width=70, font="ComicSansMS 10")
    ent4_t11.insert(0, dados_user[3])
    ent4_t11.place(x=250, y=300)

    # Label com a indicação do telefone secundário para contato do usuário
    lb6_t10 = Label(janela_atual, text="Telefone secundário", background="white", font="ComicSansMS 12 bold")
    lb6_t10.place(x=50, y=350)

    # Caixa para edição do telefone secundário do usuario
    ent5_t11 = Entry(janela_atual, width=70, font="ComicSansMS 10")
    ent5_t11.insert(0, dados_user[4])
    ent5_t11.place(x=250, y=350)

    # Label com a indicação do email do usuário
    lb7_t10 = Label(janela_atual, text="Email", background="white", font="ComicSansMS 12 bold")
    lb7_t10.place(x=50, y=400)

    # Caixa para edição do email do usuario
    ent6_t11 = Entry(janela_atual, width=70, font="ComicSansMS 10")
    ent6_t11.insert(0, dados_user[5])
    ent6_t11.place(x=250, y=400)

    # Label com a indicação do plano de manutenção
    lb8_t10 = Label(janela_atual, text="Plano de Manutenção", background="white", font="ComicSansMS 12 bold")
    lb8_t10.place(x=50, y=450)

    # Caixa para edição do plano de manutenção
    lista_planos = ["Plano Mensal", "Plano Semestral", "Plano Anual"]
    clicked_plano = StringVar()
    clicked_plano.set(dados_user[6])
    ent7_t11 = OptionMenu(janela_atual, clicked_plano, *lista_planos)
    ent7_t11.place(x=250, y=450)

    # Label com a indicação da senha do usuário
    lb9_t10 = Label(janela_atual, text="Senha", background="white", font="ComicSansMS 12 bold")
    lb9_t10.place(x=50, y=500)

    # Caixa para alteração da senha do usuario
    ent8_t11 = Entry(janela_atual, width=70, font="ComicSansMS 10")
    ent8_t11.insert(0, dados_user[7])
    ent8_t11.place(x=250, y=500)

    # Botão para salvar a edição dos dados cadastrados
    img_bt1_t11_temp = Image.open("edit.gif")
    img_bt1_t11 = ImageTk.PhotoImage(img_bt1_t11_temp)
    bt1_11 = Button(janela_atual, height=20, width=75, text="Salvar", image=img_bt1_t11, compound=LEFT,
                    background="white", font="ComicSansMS 12 bold", command=atualizar_dados_minha_conta_usuario)
    bt1_11.place(x=362, y=550)

    # Botão para voltar para a tela da área do usuário
    img_bt2_t11_temp = Image.open("back.gif")
    img_bt2_t11 = ImageTk.PhotoImage(img_bt2_t11_temp)
    bt2_t11 = Button(janela_atual, height=20, width=75, text="Voltar", image=img_bt2_t11, compound=LEFT,
                     background="white", font="ComicSansMS 12 bold", command=tela_opcoes_area_usuario)
    bt2_t11.place(x=675, y=550)

    janela_atual.mainloop()


# A função "tela_minha_conta_area_usuario" apresenta a tela onde o usuário irá visualizar os dados da própria conta
def tela_minha_conta_area_usuario():
    fechando_janelas_secundarias()
    global janela_atual
    fechando_janela_atual()

    dados_user: list = []

    arquivo_cadastro_users_json = None
    try:
        # O arquivo "users_cadastro.json" armazena um dicionário que tem como chave o email do usuário e como valores
        # associados a chave os dados cadastrais do usuário
        arquivo_cadastro_users_json = open('users_cadastro.json', 'r', encoding='latin-1')
        dados_cadastro_users_json = json.load(arquivo_cadastro_users_json)
        for email_usuario in dados_cadastro_users_json:
            if email_usuario == email_verif:
                dados_user = dados_cadastro_users_json[email_usuario]
    except:
        print("Não foi possível ler o arquivo JSON que armazena os dados dos usuários cadastradas no sistema. "
              "Esse arquivo precisa estar acessível no mesmo diretório que o programa.")
    finally:
        if arquivo_cadastro_users_json:
            arquivo_cadastro_users_json.close()

    janela_atual = Tk()
    janela_atual.title("S-GEMAPy - Área do usuário: Minha Conta")
    janela_atual.iconbitmap("icon.ico")
    janela_atual["bg"] = "white"
    janela_atual.geometry("800x600+250+50")
    janela_atual.resizable(width=False, height=False)

    # Label com texto explicativo ao usuário sobre a alteração de dados
    lb1_t10 = Label(janela_atual, text="Para alterar os seus dados cadastrais, clique no botão Editar",
                    background="white", font="ComicSansMS 14 bold")
    lb1_t10.place(x=115, y=75)

    # Label com a indicação do nome do usuario
    lb2_t10 = Label(janela_atual, text="Nome: " + dados_user[0], background="white", font="ComicSansMS 12")
    lb2_t10.place(x=50, y=150)

    # Label com a indicação do endereço do usuario
    lb3_t10 = Label(janela_atual, text="Endereço: " + dados_user[1], background="white", font="ComicSansMS 12")
    lb3_t10.place(x=50, y=200)

    # Label com a indicação do CEP do usuário
    lb4_t10 = Label(janela_atual, text="CEP: " + dados_user[2], background="white", font="ComicSansMS 12")
    lb4_t10.place(x=50, y=250)

    # Label com a indicação do telefone para contato do usuário
    lb5_t10 = Label(janela_atual, text="Telefone principal: " + dados_user[3], background="white",
                    font="ComicSansMS 12")
    lb5_t10.place(x=50, y=300)

    # Label com a indicação do telefone secundário para contato do usuário
    lb6_t10 = Label(janela_atual, text="Telefone secundário: " + dados_user[4], background="white",
                    font="ComicSansMS 12")
    lb6_t10.place(x=50, y=350)

    # Label com a indicação do email do usuário
    lb7_t10 = Label(janela_atual, text="Email: " + dados_user[5], background="white", font="ComicSansMS 12")
    lb7_t10.place(x=50, y=400)

    # Label com a indicação do plano de manutenção
    lb8_t10 = Label(janela_atual, text="Plano de Manutenção: " + dados_user[6], background="white",
                    font="ComicSansMS 12")
    lb8_t10.place(x=50, y=450)

    # Label com a indicação da senha do usuário
    lb9_t10 = Label(janela_atual, text="Senha: ***********", background="white", font="ComicSansMS 12")
    lb9_t10.place(x=50, y=500)

    # Botão para editar os dados cadastrados
    img_bt1_t10_temp = Image.open("edit.gif")
    img_bt1_t10 = ImageTk.PhotoImage(img_bt1_t10_temp)
    bt1_10 = Button(janela_atual, height=20, width=75, text="Editar", image=img_bt1_t10, compound=LEFT,
                    background="white", font="ComicSansMS 12 bold", command=editar_tela_minha_conta_area_usuario)
    bt1_10.place(x=362, y=550)

    # Botão para voltar para a tela da área do usuário
    img_bt2_t10_temp = Image.open("back.gif")
    img_bt2_t10 = ImageTk.PhotoImage(img_bt2_t10_temp)
    bt2_t10 = Button(janela_atual, height=20, width=75, text="Voltar", image=img_bt2_t10, compound=LEFT,
                     background="white", font="ComicSansMS 12 bold", command=tela_opcoes_area_usuario)
    bt2_t10.place(x=675, y=550)

    janela_atual.mainloop()


# A função "check_login_usuário" checa se o login e a senha do usuário estão corretas
def check_login_usuario():
    global email_verif
    global tela_mensagem_login
    check_email = False
    check_senha = False
    arquivo_users_json = None
    try:
        # O arquivo "users.json" armazena um dicionário que tem como chave os emails dos usuários
        # e como valores a associados a chave a senha de cada usuário
        arquivo_users_json = open('users_cadastro.json', 'r', encoding='latin-1')
        dados_users_json = json.load(arquivo_users_json)
        for email in dados_users_json:
            if email == ent1_t8_coleta_email.get().lower():  # Busca no dicionário se há email igual ao inserido
                check_email = True
                email_verif = email
        if dados_users_json[email_verif][7] == ent2_t8_coleta_senha.get():  # Verifica se a senha inserida corresponde
            # ao email encontrado no dicionário
            check_senha = True
    except:
        print("Não foi possível ler o arquivo JSON que armazena as contas dos usários. "
              "Esse arquivo precisa estar acessível no mesmo diretório que o programa.")
    finally:
        if arquivo_users_json:
            arquivo_users_json.close()

    # Se o email e a senha estiverem corretos, o programa irá abrir a tela de "Minha Conta" e fechar a janela de login
    if check_email and check_senha:
        janela_login.destroy()
        tela_opcoes_area_usuario()

    # Se os dados inseridos estiverem errados, o programa informa sobre o erro
    else:
        fechando_janelas_secundarias()
        tela_mensagem_login = Tk()
        tela_mensagem_login.title("Error")
        tela_mensagem_login.geometry("300x50+500+325")
        tela_mensagem_login.iconbitmap("icon_error.ico")
        lb2_tml = Label(tela_mensagem_login, text="\nEmail ou senha inválidos!\n", font="ComicSansMS 12")
        lb2_tml.pack()
        tela_mensagem_login.mainloop()


def mensagem_fechando_janela_login():
    global contador_login
    if messagebox.askyesno("Sair", "Desejar sair da área de login?"):
        contador_login = 0
        janela_login.destroy()


# A função "tela_login_minha_conta_area_usuario" apresenta a tela onde o usuário irá inserir o email e a senha para
# acessar os dados da sua conta
def tela_login_minha_conta_area_usuario():
    global ent1_t8_coleta_email
    global ent2_t8_coleta_senha
    global janela_login
    global contador_login
    contador_login += 1

    if contador_login <= 1:
        janela_login = Tk()
        janela_login.title("S-GEMAPy - Área do usuário: Login")
        janela_login.iconbitmap("icon.ico")
        janela_login["bg"] = "white"
        janela_login.geometry("400x300+450+200")
        janela_login.resizable(width=False, height=False)
        janela_login.protocol("WM_DELETE_WINDOW", mensagem_fechando_janela_login)

        # Label com a indicação da área de LOGIN
        lb1_t8 = Label(janela_login, text="LOGIN", background="white",
                       font="ComicSansMS 14 bold")
        lb1_t8.place(x=170, y=25)

        # Label com texto explicativo sobre o campo para inserir o email
        lb2_t8 = Label(janela_login, text="Seu email", background="white",
                       font="ComicSansMS 12")
        lb2_t8.place(x=25, y=75)

        # Caixa para usuário inserir o email
        ent1_t8_coleta_email = Entry(janela_login, width=35, font="ComicSansMS 12")
        ent1_t8_coleta_email.place(x=25, y=100)

        # Label com texto explicativo sobre o campo para inserir a senha
        lb3_t8 = Label(janela_login, text="Sua senha", background="white",
                       font="ComicSansMS 12")
        lb3_t8.place(x=25, y=150)

        # Caixa para usuário inserir a senha
        ent2_t8_coleta_senha = Entry(janela_login, width=35, font="ComicSansMS 12", show='*')
        ent2_t8_coleta_senha.place(x=25, y=175)

        # Botão para logar
        bt1 = Button(janela_login, width=10, text="Logar", background="white", font="ComicSansMS 12 bold",
                     command=check_login_usuario)
        bt1.place(x=144, y=235)

        janela_login.mainloop()


# A função "busca_chamados" irá criar uma lista com o número de todos os chamados abertos pelo usuário
def busca_chamados() -> List[str]:
    chamados: List[str] = []
    arquivo_busca_chamados_json: json = None
    try:
        # O arquivo "chamados.json" armazena um dicionário que tem como chave os números dos chamados cadastrados
        # no sistema e como valores a associados a chave as informações associadas aos chamados
        arquivo_busca_chamados_json = open('chamados.json', 'r', encoding='latin-1')
        dados_arquivo_busca_chamado_json = json.load(arquivo_busca_chamados_json)
        for chamado in dados_arquivo_busca_chamado_json:
            if dados_arquivo_busca_chamado_json[chamado][8] == email_verif:
                chamados += [chamado]
    #    except:
    #        print("Não foi possível ler o arquivo JSON que armazena os chamados cadastradas no sistema. "
    #              "Esse arquivo precisa estar acessível no mesmo diretório que o programa.")
    finally:
        if arquivo_busca_chamados_json:
            arquivo_busca_chamados_json.close()
    return chamados


# A função "busca_chamados" irá criar uma lista apnas com o número dos chamados abertos pelo usuário que ainda podem ser
# avaliados, ou seja, caso um chamado já tenha sido avaliado, esta busca não apresentará este chamado novamente
def busca_chamados_av() -> List[str]:
    chamados: List[str] = []
    arquivo_busca_chamados_json: json = None
    try:
        # O arquivo "chamados.json" armazena um dicionário que tem como chave os números dos chamados cadastrados
        # no sistema e como valores a associados a chave as informações associadas aos chamados
        arquivo_busca_chamados_json = open('chamados.json', 'r', encoding='latin-1')
        dados_arquivo_busca_chamado_json = json.load(arquivo_busca_chamados_json)
        for chamado in dados_arquivo_busca_chamado_json:
            if dados_arquivo_busca_chamado_json[chamado][8] == email_verif:
                if (dados_arquivo_busca_chamado_json[chamado][10] == "Solicitação em análise") or (
                        dados_arquivo_busca_chamado_json[chamado][10] == "Solicitação agendada") or (
                        dados_arquivo_busca_chamado_json[chamado][10] == "Não definida"):
                    chamados += [chamado]
    #    except:
    #        print("Não foi possível ler o arquivo JSON que armazena os chamados cadastradas no sistema. "
    #              "Esse arquivo precisa estar acessível no mesmo diretório que o programa.")
    finally:
        if arquivo_busca_chamados_json:
            arquivo_busca_chamados_json.close()
    return chamados


# A função "tela_avaliacao_de_solicitacoes_area_usuario" apresenta a tela da área do usuário onde é
# possível avaliar as solicitações registradas
def tela_escolha_chamado_avaliacao_de_solicitacoes_area_usuario():
    global clicked_chamado_av
    global tela_escolha_chamados_avaliacao
    global tela_mensagem_erro_chamados_avaliacao

    # Menu de opções com os chamados abertos pelo usuário
    lista_chamados_av: List[str] = busca_chamados_av()

    if not lista_chamados_av:
        fechando_janelas_secundarias()
        tela_mensagem_erro_chamados_avaliacao = Tk()
        tela_mensagem_erro_chamados_avaliacao.title("Error")
        tela_mensagem_erro_chamados_avaliacao.geometry("500x75+400+275")
        tela_mensagem_erro_chamados_avaliacao.iconbitmap("icon_error.ico")
        lb1_tmeca = Label(tela_mensagem_erro_chamados_avaliacao, text="\nVocê não possui solicitações "
                                                                      "a serem avaliadas!\n",
                          font="ComicSansMS 12")
        lb1_tmeca.pack()
        tela_mensagem_erro_chamados_avaliacao.mainloop()
    else:
        fechando_janelas_secundarias()
        tela_escolha_chamados_avaliacao = Tk()
        tela_escolha_chamados_avaliacao["bg"] = "white"
        tela_escolha_chamados_avaliacao.title("S-GEMAPy")
        tela_escolha_chamados_avaliacao.geometry("500x125+400+300")
        tela_escolha_chamados_avaliacao.iconbitmap("select.ico")
        lb1_teca = Label(tela_escolha_chamados_avaliacao, text="\nEscolha a solicitação que deseja avaliar "
                                                               "no menu abaixo\n", background="white",
                         font="ComicSansMS 12")
        lb1_teca.pack()

        clicked_chamado_av = StringVar(tela_escolha_chamados_avaliacao)
        clicked_chamado_av.set("Selecione")
        ent1_coleta_chamado_av = OptionMenu(tela_escolha_chamados_avaliacao, clicked_chamado_av, *lista_chamados_av,
                                            command=lambda _: tela_avaliacao_de_solicitacoes_area_usuario())
        ent1_coleta_chamado_av.config(font=("ComicSansMS", 12, "bold"), bg="white", width=10)
        ent1_coleta_chamado_av.pack()

        tela_escolha_chamados_avaliacao.mainloop()


# A função "validar_entradas_minha_conta" checa se todas as entradas são válidas
def validar_entradas_avaliacao_solicitacao() -> bool:
    verif_entradas_avaliacao_solicitacao = False
    if validar_entrada_str_av(clicked_atesto.get()) and validar_entrada_str_av(clicked_qs.get()) and \
            validar_entrada_str_av(clicked_qp.get()) and validar_entrada_str_av(clicked_em.get()):
        verif_entradas_avaliacao_solicitacao = True
    return verif_entradas_avaliacao_solicitacao


# A função "confirmacao_avaliacao_solicitacao" salva o a avaliação do chamado no arquivo "chamados.json"
# e apresenta a tela de confirmação de registro da avaliação
def confirmacao_avaliacao_solicitacao():
    global tela_confirmacao_av
    fechando_janelas_secundarias()

    if validar_entradas_avaliacao_solicitacao():
        novos_dados_av = [clicked_atesto.get(), clicked_qs.get(), clicked_qp.get(), clicked_em.get(),
                          ent5_tac_coleta_obs.get()]

        # Os dados da variável novos_dados_av são registrados no arquivo "chamados.json"
        with open("chamados.json", "r", encoding='latin-1') as file:
            data_av = json.load(file)
            for chamado in data_av:
                if chamado == chamado_avaliado:
                    data_av[chamado].append(novos_dados_av)
                    data_av[chamado][10] = "Avaliado"
            file.seek(0)
        with open("chamados.json", "w", encoding='latin-1') as file:
            json.dump(data_av, file, ensure_ascii=False, indent=4)

        # O programa apresenta uma tela de confirmação da avaliação
        tela_confirmacao_av = Tk()
        tela_confirmacao_av.title("S-GEMAPy")
        tela_confirmacao_av.geometry("500x75+400+275")
        tela_confirmacao_av.iconbitmap("icon_log.ico")
        lb1_tcav = Label(tela_confirmacao_av, text="\nSua opinião é muito importante para nós.\n Obrigada!",
                         font="ComicSansMS 12 bold")
        lb1_tcav.pack()

        tela_confirmacao_av.mainloop()
    else:
        fechando_janelas_secundarias()
        tela_mensagem_erro_confirmacao_avaliacao = Tk()
        tela_mensagem_erro_confirmacao_avaliacao.title("Error")
        tela_mensagem_erro_confirmacao_avaliacao.geometry("450x75+450+325")
        tela_mensagem_erro_confirmacao_avaliacao.iconbitmap("icon_error.ico")
        lb1_tmeca = Label(tela_mensagem_erro_confirmacao_avaliacao, text="\nEntradas inválidas!\n"
                                                                         "Todos os campos devem ser preenchidos!",
                          font="ComicSansMS 12")
        lb1_tmeca.pack()
        tela_mensagem_erro_confirmacao_avaliacao.mainloop()


# A função "tela_avaliacao_de_solicitacoes_area_usuario" apresenta as informações que o usuário irá avaliar em relação
# a solicitação registrada
def tela_avaliacao_de_solicitacoes_area_usuario():
    fechando_janelas_secundarias()
    global janela_atual
    fechando_janela_atual()
    global chamado_avaliado
    global clicked_atesto
    global clicked_qs
    global clicked_qp
    global clicked_em
    global ent5_tac_coleta_obs

    chamado_avaliado = clicked_chamado_av.get()

    janela_atual = Tk()
    janela_atual.title("S-GEMAPy")
    janela_atual.iconbitmap("icon.ico")
    janela_atual["bg"] = "white"
    janela_atual.geometry("800x600+250+50")
    janela_atual.resizable(width=False, height=False)

    # Label com texto explicativo ao usuário sobre a avaliação de chamados
    lb1_tac = Label(janela_atual, text="Para atestar a execução de um serviço, preencha os campos abaixo \n "
                                       "e clique no botão 'Enviar", background="white", font="ComicSansMS 14 bold")
    lb1_tac.place(x=85, y=100)

    # Label com a indicação do número do chamado selecionado
    lb2_tac = Label(janela_atual, text="Número da solicitação: #" + chamado_avaliado, background="white",
                    font="ComicSansMS 12")
    lb2_tac.place(x=75, y=200)

    # Label com a indicação do atesto de execução do serviço
    lb3_tac = Label(janela_atual, text="Você atesta a execução do serviço", background="white", font="ComicSansMS 12")
    lb3_tac.place(x=75, y=250)

    # Menu com opções para atesto do serviço
    lista_atesto = ["Sim", "Não", "Parcialmente"]
    clicked_atesto = StringVar()
    clicked_atesto.set("Selecione")
    ent1_tac_coleta_atesto = OptionMenu(janela_atual, clicked_atesto, *lista_atesto)
    ent1_tac_coleta_atesto.place(x=550, y=250)

    # Label com a indicação da avaliação da qualidade do serviço
    lb4_tac = Label(janela_atual, text="Avalie a qualidade do serviço executado",
                    background="white", font="ComicSansMS 12")
    lb4_tac.place(x=75, y=300)

    # Menu com opções para avaliação da qualidade do serviço
    lista_qualidade = ["1-Péssimo", "2-Ruim", "3-Regular", "4-Bom", "5-Ótimo"]
    clicked_qs = StringVar()
    clicked_qs.set("Selecione")
    ent2_tac_coleta_qs = OptionMenu(janela_atual, clicked_qs, *lista_qualidade)
    ent2_tac_coleta_qs.place(x=550, y=300)

    # Label com a indicação da avaliação do profissional responsável pela execução do serviço
    lb5_tac = Label(janela_atual, text="Avalie o profissional responsável pelo serviço executado", background="white",
                    font="ComicSansMS 12")
    lb5_tac.place(x=75, y=350)

    # Menu com opções para avaliação do profissional responsável pela execução do serviço
    clicked_qp = StringVar()
    clicked_qp.set("Selecione")
    ent3_tac_coleta_qp = OptionMenu(janela_atual, clicked_qp, *lista_qualidade)
    ent3_tac_coleta_qp.place(x=550, y=350)

    # Label com a indicação da avaliação da equipe de manutenção
    lb6_tac = Label(janela_atual, text="Avalie o atendimento prestado pela equipe de manutenção", background="white",
                    font="ComicSansMS 12")
    lb6_tac.place(x=75, y=400)

    # Menu com opções para avaliação da equipe de manutenção
    clicked_em = StringVar()
    clicked_em.set("Selecione")
    ent4_tac_coleta_em = OptionMenu(janela_atual, clicked_em, *lista_qualidade)
    ent4_tac_coleta_em.place(x=550, y=400)

    # Label com a indicação da possibilidade de registro de observações
    lb7_tac = Label(janela_atual, text="Observações (Opcional)", background="white", font="ComicSansMS 12")
    lb7_tac.place(x=75, y=475)

    # Caixa para inserir o observações
    ent5_tac_coleta_obs = Entry(janela_atual, width=40, font="ComicSansMS 12")
    ent5_tac_coleta_obs.place(x=275, y=475)

    # Botão para enviar a avaliação
    img_bt1_t10_temp = Image.open("sent.gif")
    img_bt1_t10 = ImageTk.PhotoImage(img_bt1_t10_temp)
    bt1_10 = Button(janela_atual, height=20, width=75, text="Enviar", image=img_bt1_t10, compound=LEFT,
                    background="white", font="ComicSansMS 12 bold", command=confirmacao_avaliacao_solicitacao)
    bt1_10.place(x=362, y=550)

    # Botão para voltar para a tela inicial
    img_bt1_tavc_temp = Image.open("back.gif")
    img_bt1_tavc = ImageTk.PhotoImage(img_bt1_tavc_temp)
    bt1_tavc = Button(janela_atual, height=20, width=75, text="Voltar", image=img_bt1_tavc, compound=LEFT,
                      background="white", font="ComicSansMS 12 bold", command=tela_opcoes_area_usuario)
    bt1_tavc.place(x=675, y=550)

    janela_atual.mainloop()


# A função "escolha_solicitacoes_acompanhamento_area_usuario" apresenta a tela da área do usuário escolherá a
# solicitação que deseja acompanhar
def escolha_solicitacoes_acompanhamento_area_usuario():
    global clicked_chamado
    global tela_mensagem_erro_chamados
    global tela_escolha_solicitacoes_usuario

    # Menu de opções com os chamados abertos pelo usuário
    lista_chamados = busca_chamados()
    if not lista_chamados:
        fechando_janelas_secundarias()
        tela_mensagem_erro_chamados = Tk()
        tela_mensagem_erro_chamados.title("Error")
        tela_mensagem_erro_chamados.geometry("500x75+400+275")
        tela_mensagem_erro_chamados.iconbitmap("icon_error.ico")
        lb2_tml = Label(tela_mensagem_erro_chamados, text="\nVocê ainda não possui solicitações "
                                                          "registradas no S-GEMAPy!\n",
                        font="ComicSansMS 12")
        lb2_tml.pack()
        tela_mensagem_erro_chamados.mainloop()
    else:
        fechando_janelas_secundarias()
        tela_escolha_solicitacoes_usuario = Tk()
        tela_escolha_solicitacoes_usuario["bg"] = "white"
        tela_escolha_solicitacoes_usuario.title("S-GEMAPy")
        tela_escolha_solicitacoes_usuario.geometry("500x125+400+300")
        tela_escolha_solicitacoes_usuario.iconbitmap("select.ico")
        lb1_tesu = Label(tela_escolha_solicitacoes_usuario,
                         text="\nEscolha a solicitação que deseja acompanhar no menu abaixo\n", background="white",
                         font="ComicSansMS 12")
        lb1_tesu.pack()

        clicked_chamado = StringVar(tela_escolha_solicitacoes_usuario)
        clicked_chamado.set("Selecione")
        ent1_coleta_chamado = OptionMenu(tela_escolha_solicitacoes_usuario, clicked_chamado, *lista_chamados,
                                         command=lambda _: tela_acompanhamento_de_solicitacoes_area_usuario())
        ent1_coleta_chamado.config(font=("ComicSansMS", 12, "bold"), bg="white", width=10)
        ent1_coleta_chamado.pack()

        tela_escolha_solicitacoes_usuario.mainloop()


# A função "tela_acompanhamento_de_solicitacoes_area_usuario" apresenta a tela da área do usuário onde é
# possível acompanhar as solicitações registradas
def tela_acompanhamento_de_solicitacoes_area_usuario():
    fechando_janelas_secundarias()
    global janela_atual
    fechando_janela_atual()
    chamado_escolhido = clicked_chamado.get()

    janela_atual = Tk()
    janela_atual.title("S-GEMAPy - Área do usuário: Acompanhamento de solicitações de manutenção")
    janela_atual.iconbitmap("icon.ico")
    janela_atual["bg"] = "white"
    janela_atual.geometry("800x600+250+50")
    janela_atual.resizable(width=False, height=False)

    dados_chamado = []

    arquivo_chamados_users_json = None
    try:
        # O arquivo "chamados.json.json" armazena um dicionário com todos os chamados registrados pelos usuários
        arquivo_chamados_users_json = open('chamados.json', 'r', encoding='latin-1')
        dados_chamados_users_json = json.load(arquivo_chamados_users_json)
        for chamado in dados_chamados_users_json:
            if chamado == chamado_escolhido:
                dados_chamado = dados_chamados_users_json[chamado]
    #    except:
    #        print("Não foi possível ler o arquivo JSON que armazena os dados dos chamados cadastradas no sistema. "
    #              "Esse arquivo precisa estar acessível no mesmo diretório que o programa.")
    finally:
        if arquivo_chamados_users_json:
            arquivo_chamados_users_json.close()

    # Label com texto explicativo ao usuário sobre a alteração de dados
    lb1_tacc = Label(janela_atual, text="S-GEMAPy: Acompanhamento de solicitações de manutenção",
                     background="white", font="ComicSansMS 14 bold")
    lb1_tacc.place(x=114, y=75)

    # Label com a indicação do número do chamado
    lb2_tacc = Label(janela_atual, text="Número da solicitação: " + chamado_escolhido,
                     background="white", font="ComicSansMS 12")
    lb2_tacc.place(x=50, y=150)

    # Label com a indicação da data de abertura do chamado
    lb3_tacc = Label(janela_atual, text="Data de abertura: " + dados_chamado[9],
                     background="white", font="ComicSansMS 12")
    lb3_tacc.place(x=50, y=200)

    # Label com a indicação da descrição do chamado
    lb4_tacc = Label(janela_atual, text="Descrição: " + dados_chamado[5][:80], background="white",
                     font="ComicSansMS 12")
    lb4_tacc.place(x=50, y=250)

    # Label com a indicação da situação do chamado
    lb5_tacc = Label(janela_atual, text="Situação: " + dados_chamado[10], background="white",
                     font="ComicSansMS 12")
    lb5_tacc.place(x=50, y=300)

    # Label com a indicação do técnico responsável
    lb6_tacc = Label(janela_atual, text="Técnico responsável: " + dados_chamado[11], background="white",
                     font="ComicSansMS 12")
    lb6_tacc.place(x=50, y=350)

    # Label com a indicação da data de agendamento
    lb7_tacc = Label(janela_atual, text="Data prevista para execução do serviço: " + dados_chamado[12],
                     background="white", font="ComicSansMS 12")
    lb7_tacc.place(x=50, y=400)

    # Label com a indicação de observações
    lb8_tacc = Label(janela_atual, text="Observações: " + dados_chamado[13][:80], background="white",
                     font="ComicSansMS 12")
    lb8_tacc.place(x=50, y=450)

    # Label com a indicação da data da última atualização
    lb9_tacc = Label(janela_atual, text="Última atualização: " + dados_chamado[14], background="white",
                     font="ComicSansMS 12")
    lb9_tacc.place(x=50, y=500)

    # Botão para voltar para a tela da área do usuário
    img_bt1_tacc_temp = Image.open("back.gif")
    img_bt1_tacc = ImageTk.PhotoImage(img_bt1_tacc_temp)
    bt1_tacc = Button(janela_atual, height=20, width=75, text="Voltar", image=img_bt1_tacc, compound=LEFT,
                      background="white", font="ComicSansMS 12 bold", command=tela_opcoes_area_usuario)
    bt1_tacc.place(x=675, y=550)

    janela_atual.mainloop()


# A função "busca_edificacoes" transforma as informacoes do arquivo edificacoes.json em uma lista
def busca_edificacoes() -> List[str]:
    edicacoes = []
    arquivo_edificacoes_json = None
    try:
        # O arquivo "edificacoes.json" armazena um dicionário que tem como chave as edificacoes cadastradas no sistema
        # e como valores a associados a chave as unidades de cada edificacao que foram cadastradas
        arquivo_edificacoes_json = open('edificacoes.json', 'r', encoding='latin-1')
        dados_edificacoes_json = json.load(arquivo_edificacoes_json)
        for edificacao in dados_edificacoes_json:
            edicacoes += [edificacao]
    except:
        print("Não foi possível ler o arquivo JSON que armazena as edificações cadastradas no sistema. "
              "Esse arquivo precisa estar acessível no mesmo diretório que o programa.")
    finally:
        if arquivo_edificacoes_json:
            arquivo_edificacoes_json.close()
    return edicacoes


# A função "total_chamados" verifica o total de chamados registrados existente no arquivo "chamados.json"
def total_chamados() -> int:
    arquivo_chamados_users_json = None
    total_chamados_atual = 0
    try:
        # O arquivo "chamados.json" armazena um dicionário que registras todos os chamados dos usuários
        arquivo_chamados_users_json = open('chamados.json', 'r')
        dados_chamados_users_json = json.load(arquivo_chamados_users_json, encoding='utf8')
        total_chamados_atual = len(dados_chamados_users_json)
    except:
        print("Não foi possível ler o arquivo JSON que armazena as solicitações dos usários. "
              "Esse arquivo precisa estar acessível no mesmo diretório que o programa.")
    finally:
        if arquivo_chamados_users_json:
            arquivo_chamados_users_json.close()
    return total_chamados_atual


# A função "validar_registro_nova_solicitacao" checa se todas as entradas são válidas
def validar_registro_nova_solicitacao() -> bool:
    verif_entradas_registro_nova_solicitacao = False
    if validar_entrada_str(ent1_t5_coleta_nome.get()) and validar_entrada_str(clicked_edif.get()) and \
            validar_entrada_str(ent3_t5_coleta_apt.get()) and validar_entrada_str(ent4_t5_coleta_tel.get()) and \
            validar_entrada_str(ent5_t5_coleta_email.get()) and validar_entrada_str(ent6_t5_coleta_chamado.get()) and \
            validar_entrada_str(clicked_turno.get()):
        verif_entradas_registro_nova_solicitacao = True
    return verif_entradas_registro_nova_solicitacao


# A função "confirmacao_registro_nova_solicitacao" salva o chamado aberto pelo usuário no arquivo "chamados.json"
# e apresenta a tela de confirmação de registro do chamado
def confirmacao_registro_nova_solicitacao():
    global tela_confirmacao_chamado
    global tela_mensagem_erro_confirmacao_chamado
    # O número do chamado é determinado pelo tamanho do dicionário guardado no arquivo "chamados.json"
    # que é chamado pela função total_chamados()

    if validar_registro_nova_solicitacao():

        numero_chamado = str(total_chamados() + 1)

        # A variável novos dados armazena os dados preenchidos pelo usuário em "registro_de_solicitacoes_area_usuario"
        # Estrutura novos_dados: {número chamado : [0-nome, 1-edif, 2-apt, 3-tel, 4-email, 5-descrição do chamado,
        # 6-turno, 7-observações do usuário, 8-email login, 9-data_e_hora, 10-situação, 11-técnico responsável,
        # 12-data agendada para execução, 13-observações do gestor, 14-data da última atualização do gestor, [15-atesto,
        # 16-av serviço, 17-av profissional, 18-av equipe manutenção, 19-observações de av]

        novos_dados = {numero_chamado: [ent1_t5_coleta_nome.get(), clicked_edif.get(), ent3_t5_coleta_apt.get(),
                                        ent4_t5_coleta_tel.get(), ent5_t5_coleta_email.get(),
                                        ent6_t5_coleta_chamado.get(), clicked_turno.get(), ent8_t5_coleta_obs.get(),
                                        email_verif, data_e_hora_formatada(), "Não definida", "Não definido",
                                        "Não definida", "Não há observações", "Não há atualizações"]}

        # Os dados da variável novos_dados são registrados no arquivo "chamados.json"
        with open("chamados.json", "r") as file:
            data = json.load(file)  # transforma o JSON em um objeto do Python
            data.update(novos_dados)
            file.seek(0)  # move o ponteiro para o início
        with open("chamados.json", "w") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)  # transforma um objeto do Python (listas, dicionários,
            # tuplas) nos formato JSON

        # O programa apresenta uma tela de confirmação do registro da solicitação
        fechando_janelas_secundarias()
        tela_confirmacao_chamado = Tk()
        tela_confirmacao_chamado.title("S-GEMAPy")
        tela_confirmacao_chamado.geometry("500x150+400+275")
        tela_confirmacao_chamado.iconbitmap("icon_log.ico")
        lb1_tcc = Label(tela_confirmacao_chamado, text="\nSua solicitação foi registrada.\n"
                                                       "\nEm breve a equipe de manutenção entrará em contato!",
                        font="ComicSansMS 12")
        lb1_tcc.pack()

        # O programa apresenta o código da solicitação registrada (número inteiro em ordem crescente)
        lb2_tcc = Label(tela_confirmacao_chamado, text="\nNúmero da solicitação: #" + str(numero_chamado) + "\n",
                        font="ComicSansMS 12 bold")
        lb2_tcc.pack()
        tela_confirmacao_chamado.mainloop()

    else:
        fechando_janelas_secundarias()
        tela_mensagem_erro_confirmacao_chamado = Tk()
        tela_mensagem_erro_confirmacao_chamado.title("Error")
        tela_mensagem_erro_confirmacao_chamado.geometry("450x75+450+325")
        tela_mensagem_erro_confirmacao_chamado.iconbitmap("icon_error.ico")
        lb1_tmecc = Label(tela_mensagem_erro_confirmacao_chamado, text="\nEntradas inválidas!\n"
                                                                       "Todos os campos devem ser preenchidos!",
                          font="ComicSansMS 12")
        lb1_tmecc.pack()
        tela_mensagem_erro_confirmacao_chamado.mainloop()


# A função "tela_registro_de_solicitacoes_area_usuario" apresenta a tela da área do usuário onde é
# possível registrar uma nova solicitação
def tela_registro_de_solicitacoes_area_usuario():
    fechando_janelas_secundarias()
    global janela_atual
    fechando_janela_atual()
    global ent1_t5_coleta_nome
    global ent2_t5_coleta_edif
    global ent3_t5_coleta_apt
    global ent4_t5_coleta_tel
    global ent5_t5_coleta_email
    global ent6_t5_coleta_chamado
    global ent8_t5_coleta_obs
    global clicked_edif
    global clicked_turno

    janela_atual = Tk()
    janela_atual.title("S-GEMAPy - Área do usuário: Registro de nova solicitação de manutenção")
    janela_atual.iconbitmap("icon.ico")
    janela_atual["bg"] = "white"
    janela_atual.geometry("800x600+250+50")
    janela_atual.resizable(width=False, height=False)

    # Label com texto explicativo ao usuário sobre o registro de solicitações
    lb1_t5 = Label(janela_atual, text="Para registrar o seu problema ou dúvida referente à manutenção predial,\n "
                                      "preencha os campos abaixo e clique no botão 'Salvar' para enviar",
                   background="white", font="ComicSansMS 12")
    lb1_t5.place(x=151, y=50)

    # Label informando que o usuário deve inserir o nome
    lb2_t5 = Label(janela_atual, text="Solicitante", background="white", font="ComicSansMS 12 bold")
    lb2_t5.place(x=50, y=150)

    # Caixa para usuário inserir o nome
    ent1_t5_coleta_nome = Entry(janela_atual, width=50, font="ComicSansMS 12")
    ent1_t5_coleta_nome.place(x=275, y=150)

    # Label informando que o usuário deve selecionar a edificação
    lb3_t5 = Label(janela_atual, text="Edificação do solicitante", background="white", font="ComicSansMS 12 bold")
    lb3_t5.place(x=50, y=200)

    # Caixa para selecionar a edificação
    lista_edificacoes = busca_edificacoes()
    clicked_edif = StringVar()
    clicked_edif.set("Selecione")
    ent2_t5_coleta_edif = OptionMenu(janela_atual, clicked_edif, *lista_edificacoes)
    ent2_t5_coleta_edif.place(x=275, y=200)

    # Label informando que o usuário deve informar a unidade
    lb4_t5 = Label(janela_atual, text="Apartamento do solicitante", background="white", font="ComicSansMS 12 bold")
    lb4_t5.place(x=50, y=250)

    # Caixa para selecionar a unidade
    ent3_t5_coleta_apt = Entry(janela_atual, width=50, font="ComicSansMS 12")
    ent3_t5_coleta_apt.place(x=275, y=250)

    # Label informando que o usuário deve inserir o telefone
    lb5_t5 = Label(janela_atual, text="Telefone para contato", background="white", font="ComicSansMS 12 bold")
    lb5_t5.place(x=50, y=300)

    # Caixa para inserir o telefone
    ent4_t5_coleta_tel = Entry(janela_atual, width=50, font="ComicSansMS 12")
    ent4_t5_coleta_tel.place(x=275, y=300)

    # Label informando que o usuário deve inserir o email
    lb6_t5 = Label(janela_atual, text="Email", background="white", font="ComicSansMS 12 bold")
    lb6_t5.place(x=50, y=350)

    # Caixa para inserir o email
    ent5_t5_coleta_email = Entry(janela_atual, width=50, font="ComicSansMS 12")
    ent5_t5_coleta_email.place(x=275, y=350)

    # Label informando que o usuário deve inserir a dúvida e/ou problema
    lb7_t5 = Label(janela_atual, text="Descrição da solicitação", background="white",
                   font="ComicSansMS 12 bold")
    lb7_t5.place(x=50, y=400)

    # Caixa para inserir o problema
    ent6_t5_coleta_chamado = Entry(janela_atual, width=50, font="ComicSansMS 12")
    ent6_t5_coleta_chamado.place(x=275, y=400)

    # Label informando que o usuário pode inserir horário preferencial para atendimento
    lb8_t5 = Label(janela_atual, text="Horário preferencial", background="white", font="ComicSansMS 12 bold")
    lb8_t5.place(x=50, y=450)

    # Caixa para informar o turno preferencial no qual o serviço de manutenção será executado
    lista_turnos = ["Manhã", "Tarde", "Noite", "Todos os turnos"]
    clicked_turno = StringVar()
    clicked_turno.set("Selecione")
    ent7_t5_coleta_turno = OptionMenu(janela_atual, clicked_turno, *lista_turnos)
    ent7_t5_coleta_turno.place(x=275, y=450)

    # Label informando que o usuário pode inserir observações
    lb9_t5 = Label(janela_atual, text="Observações (Opcional)", background="white", font="ComicSansMS 12 bold")
    lb9_t5.place(x=50, y=500)

    # Caixa para inserir observações
    ent8_t5_coleta_obs = Entry(janela_atual, width=50, font="ComicSansMS 12")
    ent8_t5_coleta_obs.place(x=275, y=500)

    # Botão para enviar a solicitação
    img_bt1_t5_temp = Image.open("sent.gif")
    img_bt1_t5 = ImageTk.PhotoImage(img_bt1_t5_temp)
    bt1_t5 = Button(janela_atual, height=20, width=75, text="Salvar", image=img_bt1_t5, compound=LEFT,
                    background="white", font="ComicSansMS 12 bold", command=confirmacao_registro_nova_solicitacao)
    bt1_t5.place(x=362, y=550)

    # Botão para voltar para a tela da área do usuário
    img_bt2_t5_temp = Image.open("back.gif")
    img_bt2_t5 = ImageTk.PhotoImage(img_bt2_t5_temp)
    bt2_t5 = Button(janela_atual, height=20, width=75, text="Voltar", image=img_bt2_t5, compound=LEFT,
                    background="white", font="ComicSansMS 12 bold", command=tela_opcoes_area_usuario)
    bt2_t5.place(x=675, y=550)

    janela_atual.mainloop()


# A função "tela_opcoes_area_usuario" apresenta a primeira tela da área do usuário onde é possível escolher a
# atividade que se deseja realizar
def tela_opcoes_area_usuario():
    global janela_atual
    fechando_janela_atual()
    janela_atual = Tk()
    janela_atual.title("S-GEMAPy - Área do usuário")
    janela_atual.iconbitmap("icon.ico")
    janela_atual["bg"] = "white"
    janela_atual.geometry("800x600+250+50")
    janela_atual.resizable(width=False, height=False)

    # Botão para o usuário acessar os dados da própria conta ("Minha conta")
    img_bt0_t3_temp = Image.open("user_account.gif")
    img_bt0_t3 = ImageTk.PhotoImage(img_bt0_t3_temp)
    bt0_t3 = Button(janela_atual, height=50, width=150, text=" Minha Conta ", image=img_bt0_t3, compound=RIGHT,
                    background="white", font="ComicSansMS 12 bold",
                    command=tela_minha_conta_area_usuario)
    bt0_t3.place(x=225, y=50)

    # Botão para o usuário acessar o Dashboard
    img_bt1_t3_temp = Image.open("dashboard.gif")
    img_bt1_t3 = ImageTk.PhotoImage(img_bt1_t3_temp)
    bt1_t3 = Button(janela_atual, height=50, width=150, text=" Dashboard ", image=img_bt1_t3, compound=RIGHT,
                    background="white", font="ComicSansMS 12 bold",
                    command=tela_dashboard)
    bt1_t3.place(x=425, y=50)

    # Label com a indicação do acesso a área do usuário
    lb1_t3 = Label(janela_atual, text="S-GEMAPy: Área do Usuário", background="white",
                   font="ComicSansMS 16 bold")
    lb1_t3.place(x=259, y=150)

    # Label com texto explicativo sobre as opções disponíveis para área do usuário
    lb2_t3 = Label(janela_atual, text="Escolha a opção que deseja acessar clicando nos ícones abaixo",
                   background="white", font="ComicSansMS 14")
    lb2_t3.place(x=127, y=200)

    # Botão para acessar área para registrar nova solicitação de manutenção
    img_bt2_t3_temp = Image.open("user_registro_solicitação.gif")
    img_bt2_t3 = ImageTk.PhotoImage(img_bt2_t3_temp)
    bt2_t3 = Button(janela_atual, height=200, width=160, text="\nRegistro\nde nova solicitação\nde manutenção\n",
                    image=img_bt2_t3, compound=TOP, background="white", font="ComicSansMS 12 bold",
                    command=tela_registro_de_solicitacoes_area_usuario)
    bt2_t3.place(x=80, y=300)

    # Botão para acessar área para acompanhar solicitações de manutenção
    img_bt3_t3_temp = Image.open("user_acompanhamento_solicitacao.gif")
    img_bt3_t3 = ImageTk.PhotoImage(img_bt3_t3_temp)
    bt3_t3 = Button(janela_atual, height=200, width=160, text="\nAcompanhamento\nde solicitações\nde manutenção\n",
                    image=img_bt3_t3, compound=TOP, background="white", font="ComicSansMS 12 bold",
                    command=escolha_solicitacoes_acompanhamento_area_usuario)
    bt3_t3.place(x=320, y=300)

    # Botão para acessar área para avaliar solicitações de manutenção
    img_bt4_t3_temp = Image.open("user_avaliacao_solicitacao.gif")
    img_bt4_t3 = ImageTk.PhotoImage(img_bt4_t3_temp)
    bt4_t3 = Button(janela_atual, height=200, width=160, text="\nAvaliação\nde solicitações\nde manutenção\n",
                    image=img_bt4_t3, compound=TOP, background="white", font="ComicSansMS 12 bold",
                    command=tela_escolha_chamado_avaliacao_de_solicitacoes_area_usuario)
    bt4_t3.place(x=560, y=300)

    # Botão para voltar para a tela de escolha da área (usuário ou gestor)
    img_bt5_t3_temp = Image.open("back.gif")
    img_bt5_t3 = ImageTk.PhotoImage(img_bt5_t3_temp)
    bt5_t3 = Button(janela_atual, height=20, width=75, text="Voltar", image=img_bt5_t3, compound=LEFT,
                    background="white", font="ComicSansMS 12 bold", command=tela_escolha_area)
    bt5_t3.place(x=675, y=550)

    janela_atual.mainloop()


# S-GEMAPy telas para escolha da área

# segunda tela do S-GEMAPy permite ao usuário escolher qual área ele deseja acessar
def tela_escolha_area():
    global janela_atual
    fechando_janela_atual()
    fechando_janela_login()
    global contador_login

    contador_login = 0

    janela_atual = Tk()
    janela_atual.title("S-GEMAPy")
    janela_atual.iconbitmap("icon.ico")
    janela_atual["bg"] = "white"
    janela_atual.geometry("800x600+250+50")
    janela_atual.resizable(width=False, height=False)

    # Label com a logo do sistema
    logo_temp2 = Image.open("logo.gif")
    logo2 = ImageTk.PhotoImage(logo_temp2)
    lb1_t2 = Label(janela_atual, image=logo2)
    lb1_t2.place(x=214, y=75)

    # Texto explicativo para direcionar escolha da área
    lb2_t2 = Label(janela_atual, text="Escolha a área que deseja acessar clicando nos ícones abaixo",
                   background="white",
                   font="ComicSansMS 14")
    lb2_t2.place(x=135, y=240)

    # Botão para acesso à área do usuário
    img_bt1_t2_temp = Image.open("user.gif")
    img_bt1_t2 = ImageTk.PhotoImage(img_bt1_t2_temp)
    bt1_t2 = Button(janela_atual, height=175, width=250, text="\nÁrea do Usuário", image=img_bt1_t2, compound=TOP,
                    background="white", font="ComicSansMS 12 bold", command=tela_login_minha_conta_area_usuario)
    bt1_t2.place(x=94, y=325)

    # Botão para acesso à área do gestor
    img_bt2_t2_temp = Image.open("gestor.gif")
    img_bt2_t2 = ImageTk.PhotoImage(img_bt2_t2_temp)
    bt2_t2 = Button(janela_atual, height=175, width=250, text="\nÁrea do Gestor", image=img_bt2_t2, compound=TOP,
                    background="white", font="ComicSansMS 12 bold", command=tela_opcoes_area_gestor)
    bt2_t2.place(x=446, y=325)

    # Botão para voltar para a tela inicial
    img_bt3_t2_temp = Image.open("back.gif")
    img_bt3_t2 = ImageTk.PhotoImage(img_bt3_t2_temp)
    bt3_t2 = Button(janela_atual, height=20, width=75, text="Voltar", image=img_bt3_t2, compound=LEFT,
                    background="white", font="ComicSansMS 12 bold", command=tela_inicial)
    bt3_t2.place(x=675, y=550)

    janela_atual.mainloop()


# Tela inicial do S-GEMAPy
def tela_inicial():
    global janela_atual
    fechando_janela_atual()
    fechando_janela_login()

    janela_atual = Tk()
    janela_atual.iconbitmap("icon.ico")
    janela_atual.title("S-GEMAPy")
    janela_atual["bg"] = "white"
    janela_atual.geometry(
        "800x600+250+50")  # "largura x altura + posicionamento" da tela (esquerda do vídeo e topo do vídeo) em pixels
    janela_atual.resizable(width=False, height=False)  # Congela as dimensões da janela

    # Label com o nome do sistema
    lb1 = Label(janela_atual, text="Sistema de Gerenciamento da Manutenção Predial", background="white",
                font="ComicSansMS 16 bold")
    lb1.place(x=146, y=125)

    # Label com a logo do sistema
    logo_temp = Image.open("logo.gif")
    logo = ImageTk.PhotoImage(logo_temp)
    lb2 = Label(janela_atual, image=logo)
    lb2.place(x=214, y=225)

    # Label com a descrição da versão do sistema
    lb3 = Label(janela_atual, text="Versão 1.0", background="white", font="ComicSansMS 12 bold")
    lb3.place(x=360, y=350)

    # Botão para abrir a tela onde o usuário poderá escolher a área que deseja acessar
    bt1 = Button(janela_atual, width=10, text="Entrar", background="white", font="ComicSansMS 12 bold",
                 command=tela_escolha_area)
    bt1.place(x=344, y=450)

    janela_atual.mainloop()


tela_inicial()
