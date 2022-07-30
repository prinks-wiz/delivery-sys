

class User_inputs:
    size=0
  
    def __init__(self,name,phone_number,email,address): 
        self.name =name
        self.phone_number = phone_number
        self.address = address
        self.email = email

    def check_phone(self):
        if len(self.phone_number)!=10:
            return False  

    def check_email(self):
        a=self.email
        if "@" not in a:
            return False
        else:
            return True


    def display(self):  
        print('Hello',self.name)
        print("Your Phone Number is ", self.phone_number)
        print("Your Email is",self.email)
        print("your Address is",self.address)
     

