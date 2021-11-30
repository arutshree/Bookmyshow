
from modules import*

print('Welcome to Book_your_Movie.com')
rows = input('please enter the number of rows in the desired theatre\n')
columns = input('please enter the number of columns in the desired theatre\n')

def showoptions():
    print('select From the following options')
    print('1.show the seats\n2.Buy a ticket\n3.statistics\n4.show booked tickets user info\n0.Exit\n')
    n = input()
    return int(n)
n = showoptions()
m = seats.Theatre(int(rows),int(columns))
q = 0
customers = []
while n!= 0:
    q = 0
    if n == 1:
        print('1.show the seats')
        seats.show_seats(m)
    elif n== 2:
        print(' Buy a ticket')
        r = int(input('Enter the row number of your seats\n'))
        c = int(input('Enter the columns number of your seats\n'))
        for j in customers:
            if j.seat == (r,c):
                print('sorry, Those seats are occupied!!')
                print('*********')
                n = showoptions()
                q = 1
        if q ==1:
            continue
        Ticketprice = stats.Ticket_price(int(row),int(columns),r)
        print('Your Ticket price is ',Ticketprice,'$')
        inp = input('press "y" to proceed to booking\npress "n" to return main menu\n')
        if inp =='y':
            Name = input('Enter your name\n')
            Age = input('Enter your name Age\n')
            Gender = input('Enter your name Gender\n')
            phn = input('Enter your name phone number\n')
            print('*********')
            i = details.Audience(Name,Gender,Age,phn,(r,c))
            customers.append(i)
            m = Buy_a_ticket.Book_Ticket(m,r,c)
        elif inp == 'n':
            pass
        else:
            print('please enter the valid response\nReturning to main menu\n.............\n')
        elif n== 3:
            print('statistics')
            stats.show_stats(m)
        elif n ==4:
            print('Book ticket user info')
            for i in customers:
                i.printDetails()
        else:
            print('please select from the given option only')
        n = showoptions()
        
        
print('Thank you')


            
                
                
        

