import tkinter as tk
from tkinter import messagebox,simpledialog

class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Simulation")
        self.root.geometry("800x500")
        root.configure(bg='black')


        label = tk.Label(root, text="Welcome to your bank account Ms.ABC", font="arial,30", fg='white', bg='black')
        label.place(x=10, y=10)


        self.btn_logout = tk.Button(root, text="Logout and Exit",fg='white', bg='black', command=self.logout_exit)
        self.btn_logout.pack(pady=10)

        self.btn_view= tk.Button(root, text="View account balance",fg='white', bg='black', command=self.view_balance)
        self.btn_view.pack(pady=5)

        self.btn_withdraw = tk.Button(root, text="Withdraw Cash",fg='white', bg='black', command=self.withdraw_cash)
        self.btn_withdraw.pack(pady=5)

        self.btn_deposit = tk.Button(root, text="Deposit Cash", fg='white', bg='black',command=self.deposit_cash)
        self.btn_deposit.pack(pady=5)

        self.btn_change_pin = tk.Button(root, text="Change PIN",fg='white', bg='black',command=self.change_pin)
        self.btn_change_pin.pack(pady=5)

        self.btn_return_card = tk.Button(root, text="Return card",fg='white', bg='black',command=self.return_card)
        self.btn_return_card.pack(pady=5)






    def logout_exit(self):
        messagebox.showinfo("logout","Exiting....You have been logged out. Thank you!")

    def view_balance(self):
        withdrawal_amount = simpledialog.askinteger("view balance", "Enter your 4 digit PIN")
        messagebox.showinfo("view balance", "Account authorized")
        messagebox.showinfo("view balance","Loading Account balance.....", "Your current balance is Rs.9743.2")

    def withdraw_cash(self):
        withdrawal_amount = simpledialog.askinteger("Withdraw", "Please enter your 4 digit PIN")
        messagebox.showinfo("withdrawal","Account authorized")
        messagebox.showinfo("withdrawal","opening cash withdrawal")
        withdrawal_amount1 = simpledialog.askinteger("Withdraw", "Enter the amount you wish to withdraw")
        messagebox.showinfo("withdrawal","Cant withdraw Rs.100000.0")
        messagebox.showinfo("withdrawal","please enter a lower amount")
        withdrawal_amount1 = simpledialog.askinteger("Withdraw", "Enter the amount you wish to withdraw")
        messagebox.showinfo("withdrawal","Withdrawing Rs.10000.0")
        withdrawal_amount1 = simpledialog.askstring("Withdraw", "Confirm Y/N")
        messagebox.showinfo("withdrawal","Amount withdrawn Rs.10000.0")
        messagebox.showinfo("withdrawal","Remaining balance Rs.87432.5")


    def deposit_cash(self):
        deposit_amount = simpledialog.askinteger("Deposit", "Please Enter your 4 digit PIN")
        messagebox.showinfo("Deposit", "Account authorized!")
        messagebox.showinfo("Deposit", "Loading Cash Deposit....")

    def change_pin(self):
        deposit_amount = simpledialog.askinteger("Deposit", "Please Enter your 4 digit PIN")
        messagebox.showinfo("change pin", "Account authorized!")
        messagebox.showinfo("change pin", "Loading PIN change....")
        deposit_amount = simpledialog.askinteger("pinchange", "Enter your new PIN")
        messagebox.showinfo("change pin", "Changing PIN to 2912....")
        withdrawal_amount1 = simpledialog.askstring("Withdraw", "Confirm Y/N")
        messagebox.showinfo("change pin", "PIN changed successfully!")

    def return_card(self):
        messagebox.showinfo("change pin", "Transaction compleated")
        messagebox.showinfo("change pin", "Return your card")
        

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
