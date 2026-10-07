#python mini project-cafe management
#step1:greetings the user
#step2:showing menu{'pizza':60,'salad':50,'burger':100,'pop corn':70}
#step3:note the item
#step4:check the item in our menu
#                  if yes:add the cost
#                    ask user for anything else
#                       if yes:note the seecond item
#                         check the item in our menu
#                                  calculate total cost &display
#                                if no:end order&display cost
#         if no:display erroe message

menu={'pizza':60,'salad':50,'burger':100,'pop corn':70,'chicken':150}
print("welcome to our cafe")
print('pizza:60 \nsalad:50\n burger:100\n pop corn:70\n chicken:150')
order_item=input("enter your item:")

order_total=0

if order_item in menu:
    order_total+=menu[order_item]
    order=input('Do you want anything else(yes/no):')
    if order =='yes':
        order_item2=input('enter your second item:')
        if order_item2 in menu:
            order_total+=menu[order_item2]
            print(f'your order value:{order_total}')
    else:
        print(f'your order value:{order_total}')        
else:
    print('you entered a wrong item')



