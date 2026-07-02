inventory = {'screws': 150, 'bolts': 8, 'washers': 0, 'nuts': 45}
inventory_check={key: 'reorder' if value <=10  else 'In stock' for (key,value) in inventory.items()}
print(inventory_check)