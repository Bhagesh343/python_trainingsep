sweets = input("enter few sweets(space seperated):").split()
sweets_set = set(sweets)
sweets_fset = frozenset(sweets)
sweets_dict = {name:len(name) for name in sweets_fset}

print(f'Original List: {sweets}')
print(f'set of sweets (No duplicate):{sweets}')
print(f'Frozen set: {sweets_fset}')
print(f'Dictionary of sweets: {sweets_dict}')
