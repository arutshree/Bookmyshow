
import numpy as np

def Ticket_price(rows,columns,r):
    if rows*columns <= 60:
        Ticketprice = 10
    else :
        if r < (rows/2):
            Ticketprice = 10
        else:
            Ticketprice = 8
        return Ticketprice
    
    
def Total_Income(m):
    r,c = np.shape(m)
    if r*c <=60:
        TotalIncome =r*c*10
    else:
        TotalIncome =((r/2)*10)*c + ((r-(r//2))*8)*c
    return TotalIncome


def show_stats(m):
    B = np.array([])
    r,c = np.shape(m)
    for i in range(r):
        for j in range(c):
            if m[i][j] == 'B':
                B = np.append(B,i)
    p = np.array([])
    for i in B:
        U = Ticket_price(r,c,i)
        p = np.append(p,u)
        
        
    print('Number of purchased Tickets:', np.shape(B)[0])
    print('percentage :', (np.shape(B)[0]/(r*c))*100,'%')
    print('current income: $', np.sum(p))
    print('Total income: $', Total_income(m))
    print('***********')

