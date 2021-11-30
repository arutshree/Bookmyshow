
class Audience:
    
    def __init__(self,Name,Gender,Age,phn,seat):
        self.Name = Name
        self.Gender = Gender
        self.Age = Age
        self.ph = phn
        self.seat = seat
        
    def printDetails(self):
        print('Name :', self.Name)
        print('Gender :', self.Gender)
        print('Age : ', self.Age)
        print('ph no :', self.ph)
        print('seat No :', self.seat)
        print('***********')
        

