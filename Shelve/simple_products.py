base = [{'name': 'Apple', 'price': 10, 'quantity': 1}]  # example one element base
# base = []  # it can be also just empty list at the beginning

def entry():
    global base
    name = raw_input('Name of the product: ')
    quantity = raw_input('Quantity: ')
    price = raw_input('Price per unit: ')

    is_new_entry = True
    print name
    print quantity
    print price
    # entry is element of base list
    for entry in base:
        if name.lower() == entry['name'].lower():  # checking if name already exist in base list
            is_new_entry = False

    if is_new_entry:  # adding new list element
        base += [{
            'name': name, 
            'quantity': int(quantity),
            'price': float(price)
        }]
        print 'Saved.'  # confirmation message
    else:
        print 'Element with the name {} already exist!'.format(name)  # error message


def articles():
    global base
    print 'List of articles in magazine'.center(50)
    print '-'*50
    print '|'+'Name'.center(15)+'|'+'Quantity'.center(15)+'|'+'Price'.center(15)+'|'
    print '-'*50
    for entry in base:
        print "|%14s |" % entry['name'],'%13s' % entry['quantity'],'|' '%14s' % entry['price'],'|'
    print '-'*50


entry()
articles()
entry()
articles()