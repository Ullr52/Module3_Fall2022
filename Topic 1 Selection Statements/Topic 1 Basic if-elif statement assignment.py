print('Please make a selection to find out more about our great Programmers Toolkit Monthly Subscription Box!\n'
      '1. Platinum\n2. Gold\n3. Silver\n4. Bron\n5. Free Trial\n\nPlease select 1-5: ')
choice = int(input())

if(choice == 1):
      print('Platinum selection includes 6 free comics!\nAnd a 12" statue of your choice! for only $60!')
elif(choice == 2):
      print('Gold selection includes 5 free comics!\nAnd a 6" figure of your choice! for only $50!')
elif(choice == 3):
     print('Silver selection includes 4 free comics!\nAnd a 3.75" figure of your choice! for only $40!')
elif(choice == 4):
      print('Bronze selection includes 3 free comics!\nAnd a random enamel pin for only $30!')
elif(choice == 5):
      print('Free Trial selection includes 1 free comic!\nAnd one of our great catalogs! This option is free and can only '
            'be used once per household.')
else:
      print('Please enter a valid selection')




