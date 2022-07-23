class User_inputs:
    size=0
  
    def __init__(self,name,phone_number,email,address): 
        self.name =name
        self.phone_number = phone_number
        self.address = address
        self.email = email

    def check_phone(self):
        if len(str(self.phone_number))!=10 and type(self.phone_number)!= int:
            return False  

    def check_email(self):
        a=self.email[-1:-11:-1]
        b=a[::-1]
        if b!="@gmail.com":
            return False   

    def display(self):  
        print('Hello',self.name)
        print("Your Phone Number is ", self.phone_number)
        print("Your Email is",self.email)
        print("your Address is",self.address)
     

