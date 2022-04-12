item_number = int(input('Please input the number of items:'))
total_price = 0.0
while item_number < 0:
    print('Invalid number of items!')
    item_number = int(input('Please input the number of items:'))
for i in range(item_number):
    item_price = float(input('Price of item:'))
    while item_price < 0:
        print('Invalid price of items!')
        item_price = float(input('Price of item:'))
    total_price += item_price
if total_price > 100:
    total_price = total_price * 90/100

print('Total price for', item_number, 'items is', total_price,)
