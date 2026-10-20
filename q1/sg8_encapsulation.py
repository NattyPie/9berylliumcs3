class BankAccount: #defines class
  def __init__ (self, accountnumber, balance): #defines the attributes
    self.set_accountnumber(accountnumber) #account number variable
    self.set_balance(balance) #balance variable
    
  def set_accountnumber(self, accountnumber): #sets account number
    self.__accountnumber = accountnumber
    
  def set_balance(self, balance): #sets balance
    if balance < 0: #checks if the balance is a negative number
      print("The balance must not be a negative number") #if the balance is a negative number this will be printed
    else:
      self.__balance = balance #if the balance is positive
      
  def get_accountnumber(self): #gets the account number
    return self.__accountnumber
    
  def get_balance(self): #gets balance
    return self.__balance

if __name__ == "__main__": #checks if everything is being done correctly
  print("Objectof class BankAccount")
  a1 = BankAccount(12345, 1000)

  print("\nOutput:")
  print("Account 1") #prints the labes, haha sanaol
  print(f"Account number: {a1.get_accountnumber()}") #prints the retrieved account number
  print(f"Balance: {a1.get_balance(): .2f}") #prints the retrieved balance

  print("\nUpdate balance to -100") #prints a message that says that the balance will be updating
  a1.set_balance(-100) #tries to set the balance to negative, it should warn the user that it is not possible for it to be negative
  print(f"Account number: {a1.get_accountnumber()}") #prints the account number
  print(f"Balance: {a1.get_balance(): .2f}") #prints the balance
