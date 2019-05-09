inventory={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

def displayInventory(inventory):
    print("Inventory:")
    item_total=0
    for k,v in inventory.items():
        print (str(v)+' '+k)
        item_total+=int(v)
    print('The total number of items are :{}'.format(item_total))

displayInventory(inventory)
