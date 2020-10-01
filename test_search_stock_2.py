#test_search_stock_2
# tutorial name: ACESSANDO DADOS DO INVESTING.COM COM PYTHON #2 | Índices e Ações | Python para Investimentos #12
# #link of tutorial: https://www.youtube.com/watch?v=Tv2-BGOLf9E

###########################################################
#libraries
###########################################################
import investpy as inv


###########################################################
#declarations
###########################################################



###########################################################
#execution
###########################################################

# lista = inv.get_indices_list('brazil')
# print(lista)

# lista_2 = inv.get_stocks('brazil')
# print(lista_2)

info = inv.get_stock_information('ELEK4','brazil')
print(info)
