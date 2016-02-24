from collections import defaultdict

flowers = [('rose', 3), ('tulip', 1), ('rose', 7), ('tulip', 5), ('violet', 1)]
flowers_inventory = defaultdict(list)
for k, v in flowers:
    flowers_inventory[k].append(v)

flowers_inventory.items()  #[('rose', [3, 7]), ('violet', [1]), ('tulip', [1, 5])]

