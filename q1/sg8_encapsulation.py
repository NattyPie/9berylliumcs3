class BankAccount:
  #Initia;ize object attributes safely
  def __init__ (self, accountnumber, balance):
    self.set_accountnumber(accountnumber)
    self.set_balance(balance)
    
#Set the private account number
  def set_accountnumber(self, accountnumber):
    self.__accountnumber = accountnumber
    
#Set balance with negative check
  def set_balance(self, balance):
    if balance < 0:
      print("The balance must not be a negative number")
    else:
      self.__balance = balance
      
#Return the private account number
  def get_accountnumber(self):
    return self.__accountnumber
    
#Return the private balance
  def get_balance(self):
    return self.__balance

#Create an account instance 
if __name__ == "__main__":
  print("Objectof class BankAccount")
  a1 = BankAccount(12345, 1000)

#Show initial account details
  print("\nOutput:")
  print("Account 1")
  print(f"Account number: {a1.get_accountnumber()}")
  print(f"Balance: {a1.get_balance(): .2f}")

 #Try setting a negative balance 
  print("\nUpdate balance to -100")
  a1.set_balance(-100)
  print(f"Account number: {a1.get_accountnumber()}")
  print(f"Balance: {a1.get_balance(): .2f}")
