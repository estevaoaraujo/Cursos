from itertools import combinations, permutations, product

times = [
		'cruzeiro','Atletico','America','Pouso Alegre'
]


camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
]

def print_iter(iterator):
	print(*list(iterator),sep='\n')
	print()


print_iter(combinations(times,2))	
print_iter(product(*camisetas))