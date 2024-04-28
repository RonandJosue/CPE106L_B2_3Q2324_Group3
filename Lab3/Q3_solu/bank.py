import pickle,random
from savingsaccount import SavingsAccount
account_list = []
class Bank:
    def __init__(self, fileName=None):
        self.accounts = {}
        self.fileName = fileName
        if fileName is not None:
            with open(fileName, 'rb') as fileObj:
                while True:
                    try:
                        account = pickle.load(fileObj)
                        self.add(account)
                    except EOFError:
                        break

    def __str__(self):
        """Returns the string representation of the bank, sorted by account names."""
        account_list = self.get_sorted_accounts()
        return "\n".join(str(account) for account in account_list)

    def makeKey(self, name, pin):
        return name + "/" + pin

    def add(self, account):
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        key = self.makeKey(name, pin)
        return self.accounts.get(key)

    def computeInterest(self):
        total = 0
        for account in self.accounts.values():
            total += account.computeInterest()
        return total

    def get_sorted_accounts(self):
        """Retrieve and return accounts sorted by their names."""
        return sorted(self.accounts.values(), key=lambda account: account.getName())

    def save(self, fileName=None):
        if fileName is not None:
            self.fileName = fileName
        if self.fileName is None:
            return
        with open(self.fileName, 'wb') as fileObj:
            for account in self.accounts.values():
                pickle.dump(account, fileObj)

# Functions for testing
       
def createBank(numAccounts = 1):
    """Returns a new bank with the given number of 
    accounts."""
    names = ("Brandon", "Molly", "Elena", "Mark", "Tricia",
             "Ken", "Jill", "Jack")
    bank = Bank()
    upperPin = numAccounts + 1000
    for pinNumber in range(1000, upperPin):
        name = random.choice(names)
        balance = float(random.randint(100, 1000))
        bank.add(SavingsAccount(name, str(pinNumber), balance))
    return bank

def testAccount():


# Instantiate SavingsAccount objects and add them to the list
    account_list.append(SavingsAccount("Ken", "1000", 500.00))
    account_list.append(SavingsAccount("Alice", "2000", 1000.00))
    account_list.append(SavingsAccount("Bob", "3000", 750.00))
    
    print(account_list[0])
    print(account_list[0].deposit(100))
    print("Expect 600:", account_list[0].getBalance())
    print(account_list[0].deposit(-50))
    print("Expect 600:", account_list[0].getBalance())
    print(account_list[0].withdraw(100))
    print("Expect 500:", account_list[0].getBalance())
    print(account_list[0].withdraw(-50))
    print("Expect 500:", account_list[0].getBalance())
    print(account_list[0].withdraw(100000))
    print("Expect 500:", account_list[0].getBalance())

def main(number = 10, fileName = None):
    """Creates and prints a bank, either from
    the optional file name argument or from the optional
    number."""
    testAccount()
    random.shuffle(account_list)
    sorted_accounts_list = sorted(account_list, key=lambda account: account.getName())
    for account in sorted_accounts_list:
        print(account)
    

if __name__ == "__main__":
    main()
