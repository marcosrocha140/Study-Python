names = []
size = int(input("Enter Size for list.\n"))

#.insert(x) insere o valor a lista na posicao indicada (x)
for i in range(0, size):
    value = str(input("Enter name for list.\n"))
    names.insert(i, value)

#.sort organiza a lista na ordem crescente
names.sort()
for i in range(0, size):
    print(f"Name: ", names[i])
    


