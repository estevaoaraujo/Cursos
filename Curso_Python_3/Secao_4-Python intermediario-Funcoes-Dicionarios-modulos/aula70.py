matrix = ['-', '-', '-',
          '-', '-', '-',
          '-', '-', '-']

for i, cell in enumerate(matrix):
    # Print the cell value without a newline
    print(cell, end=" ")
    
    # After every 3rd element (indices 2, 5, 8), print a newline
    if (i + 1) % 3 == 0:
        print()
        

matrix = ['-','-','-',
          '-','-','-',
          '-','-','-']

# Percorre a lista com um contador (i)
for i, item in enumerate(matrix):
    # Imprime o item sem pular linha
    print(item, end=' ')
    
    # Se o contador (i) for 2 ou 5, pula uma linha para formar a grade
    if i == 2 or i == 5:
        print()        