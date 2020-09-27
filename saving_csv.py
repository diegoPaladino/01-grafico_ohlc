#saving_csv

# libraries
import csv
# declarations
# execution
with open("arquivos/saida.csv",'w', newline='') as saida:
    escrever = csv.writer(saida)

    for i in range (1,21):
        print(i)
        escrever.writerow([i])