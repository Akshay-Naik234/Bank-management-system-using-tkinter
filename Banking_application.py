from tkinter import*
import tkinter.messagebox

import random
import sqlite3
class Bank:
    def __init__(self,root):
        cName = ['aks', 'IasonJordan', 'DavidMorgan', 'BrainJohn', 'JackSwift']
        cAccount=['666666666666','222222222222','333333333333','444444444444','555555555555']
        cPin = ['2348','2575', '7275', '2312', '5049']
        cBalances = [10000, 20000, 30000, 40000, 50000]
        d = Database()
        d.conn()
        self.root=root
        self.root.title('Banking system')
        self.root.geometry("830x500")
        credit2=StringVar()
        debit2=StringVar()
        def Login():
            global screen1
            global Name,Account,PIN
            global txtName,txtAccount,txtPin
            screen1= Toplevel(self.root)
            screen1.title("Login Page")
            screen1.geometry("800x400")
            Name=StringVar()
            Account=StringVar()
            PIN=StringVar()
            Title = Label(screen1,font=('arial',30,'bold'),text="WELCOME TO LOGIN PORTAL"
                                    ,bg='white',fg='red').grid(row=0,column=1)
            lblName=Label(screen1,text="Name",font=('arial',16,'bold')
                              ,bd=20).grid(row=2,column=0)
            txtName=Entry(screen1,font=('arial',16,'bold'),textvariable= Name,
                                  width=22).grid(row=2,column=1,sticky=W)
            lblAccount=Label(screen1,text="Account no",font=('arial',16,'bold'),
                             bd=20).grid(row=3,column=0)
            txtAccount=Entry(screen1,font=('arial',16,'bold'),textvariable= Account,
                                  width=22).grid(row=3,column=1,sticky=W)
            lblPin=Label(screen1,text="PIN",font=('arial',16,'bold'),
                             bd=20).grid(row=4,column=0)
            txtPin=Entry(screen1,font=('arial',16,'bold'),textvariable= PIN,
                                  width=22).grid(row=4,column=1,sticky=W)
            buttonSubmit=Button(screen1,text="SUBMIT",font=('arial',16,'bold'),height=1,
                                       width='14',bd=6,command=SUBMIT).grid(row=5,column=0)
            buttonHome=Button(screen1,text="HOME",font=('arial',16,'bold'),height=1,
                                       width='14',bd=6,command=lambda:Home(screen1)).grid(row=5,column=1)
            print(cName)
        def create():
            global name,credit1,pin
            global screen2
            screen2= Toplevel(self.root)
            screen2.title("Create Account Page")
            name=StringVar()
            credit1=StringVar()
            pin=StringVar()
            Title = Label(screen2,font=('arial',30,'bold'),text="    WELCOME TO Create Account Page   "
                                    ,bg='white',fg='red').grid(row=0,column=1)
            lblName=Label(screen2,text="Enter Name",font=('arial',16,'bold')
                              ,bd=20).grid(row=2,column=0)
            txtName=Entry(screen2,font=('arial',16,'bold'),textvariable= name,
                                  width=22).grid(row=2,column=1,sticky=W)
            lblcredit=Label(screen2,text="Enter initial credit",font=('arial',16,'bold'),
                             bd=20).grid(row=3,column=0)
            txtcredit=Entry(screen2,font=('arial',16,'bold'),textvariable= credit1,
                                  width=22).grid(row=3,column=1,sticky=W)
            lblPin=Label(screen2,text="Enter PIN",font=('arial',16,'bold'),
                             bd=20).grid(row=4,column=0)
            txtPin=Entry(screen2,font=('arial',16,'bold'),textvariable= pin,
                                  width=22).grid(row=4,column=1,sticky=W)
            buttonSubmit=Button(screen2,text="SUMBIT",font=('arial',16,'bold'),height=1,
                                       width='14',bd=6,command=submit).grid(row=5,column=0)

        def close():
            close = tkinter.messagebox.askyesno("Banking system","Really .... Do you want to exit")
            if close>0:
                self.root.destroy()
                return

        def Home(master):
            master.destroy()
            Bank(root)

        def SUBMIT():
            global Account_info
            Name_info=Name.get()
            Account_info=Account.get()
            PIN_info=PIN.get()
            global i
            k=0
            while k<=len(cName)-1:
                if Name_info == cName[k]:
                    if Account_info == cAccount[k]:
                        if PIN_info == cPin[k]:
                            tkinter.messagebox.showinfo("screen1","Login successfully")
                            i=k
                            Log()
                            break
                k=k+1
            if k>=len(cName):
                tkinter.messagebox.showerror("screen1","login fails")
            
        def Log():
            global screen3
            screen3= Toplevel(screen1)
            screen3.title("Bank System")
            screen3.geometry("1100x600")
            Title = Label(screen3,font=('arial',30,'bold'),text=" SIMPLE BANKING SYSTEM",width=40
                                    ,bg='white',fg='red').place(x=100,y=15)
            buttoncredit=Button(screen3,text="Credit Amount in your Account",font=('arial',16,'bold'),height=1,
                                       width='25',bd=6,command=credit).place(x=200,y=150)
            buttondebit=Button(screen3,text="Debit Amount From Account",font=('arial',16,'bold'),height=1,
                                       width='25',bd=6,command=debit).place(x=600,y=150)
            buttonbalance=Button(screen3,text="Balance Amount",font=('arial',16,'bold'),height=1,
                                       width='25',bd=6,command=balance).place(x=200,y=250)
            buttonLoan=Button(screen3,text="Loan",font=('arial',16,'bold'),height=1,
                                       width='25',bd=6,command=Loan).place(x=600,y=250)
            buttonLogout=Button(screen3,text="Logout",font=('arial',16,'bold'),height=1,
                      width='25',bd=6,command=lambda:Logout(screen3,screen1)).place(x=200,y=350)
            buttonSaveData=Button(screen3,text="Save",font=('arial',16,'bold'),height=1,
                                       width='25',bd=6,command=insert).place(x=600,y=350)
            buttonSaveData=Button(screen3,text="Update",font=('arial',16,'bold'),height=1,
                                       width='25',bd=6,command=Update).place(x=400,y=450)
            
            
        def submit():
            name_info=name.get()
            pin_info=pin.get()
            credit_info=credit1.get()
            if name_info == " " or  pin_info == "" or credit_info=="":
                tkinter.messagebox.showerror("screen2","All the fields are required")
            elif len(pin_info)!=4:
                tkinter.messagebox.showerror("screen2","pin must be 4 digits")
            elif int(credit_info)<= 100:
                tkinter.messagebox.showerror("screen2","Minimum credit is 100Rs")
            else:
                acc_no = random.randint(111111111111,999999999999)
                tkinter.messagebox.showinfo("screen2","Your Account Number is:"+str(acc_no))
            cName.append(name_info)
            cPin.append(pin_info)
            cBalances.append(int(credit_info))
            cAccount.append(str(acc_no))
            print(cName)
            print(cAccount)
            
        def credit():
            global txtcredit
            global screen4
            screen4= Toplevel(screen3)
            screen4.title("Bank System")
            screen4.geometry("1000x300")
            Title = Label(screen4,font=('arial',30,'bold'),text="    WELCOME TO Credit Page   "
                                    ,bg='white',fg='red').grid(row=0,column=1)
            lblcredit=Label(screen4,text="Enter the amount to be credited ",font=('arial',16,'bold')
                              ,bd=20).grid(row=2,column=0)
            txtcredit=Entry(screen4,font=('arial',16,'bold'),textvariable= credit2,
                                  width=22).grid(row=2,column=1,sticky=W)
            buttoncredit=Button(screen4,text="SUBMIT",font=('arial',16,'bold'),height=1,
                                       width='14',bd=6,command=csubmit).grid(row=4,column=0)

        def debit():
            global txtdebit
            global screen5
            screen5= Toplevel(screen3)
            screen5.title("Bank System")
            screen5.geometry("1000x300")
            Title = Label(screen5,font=('arial',30,'bold'),text="    WELCOME TO Debit Page   "
                                    ,bg='white',fg='red').grid(row=0,column=1)
            lbldebit=Label(screen5,text="Enter the amount to be debited ",font=('arial',16,'bold')
                              ,bd=20).grid(row=2,column=0)
            txtdebit=Entry(screen5,font=('arial',16,'bold'),textvariable= debit2,
                                  width=22).grid(row=2,column=1,sticky=W)
            buttondebit=Button(screen5,text="SUMIT",font=('arial',16,'bold'),height=1,
                                       width='14',bd=6,command=dsubmit).grid(row=4,column=0)
        def insert():
            if(len(Account.get())==12):
                d.insert(Account.get(),PIN.get(),Name.get(),credit2.get(),debit2.get(),cBalances[i])
                tkinter.messagebox.showinfo("screen5","All the details are saved successfully")

        def csubmit():
            global credit_info
            credit_info=credit2.get()
            cBalances[i]=cBalances[i]+int(credit_info)
            if credit_info == " ":
                tkinter.messagebox.showerror("screen4","credit amount cannot be empty ")
            else:
                tkinter.messagebox.showinfo("screen4","The credit amount is:"+str(credit_info) + "\nthe balance is" + str(cBalances[i]))
            screen4.destroy()

        def dsubmit():
            global debit_info
            debit_info=debit2.get()
            if int(debit_info)>cBalances[i]-500:
                tkinter.messagebox.showerror("screen5","Insufficient Balance ")
            elif debit_info == " ":
                tkinter.messagebox.showerror("screen5","debit amount cannot be empty ")
            else:
                cBalances[i]=cBalances[i]-int(debit_info)
                tkinter.messagebox.showinfo("screen4","The debit amount is:"+str(debit_info) + "\nthe balance is" + str(cBalances[i]))
                screen5.destroy()

        def balance():
             tkinter.messagebox.showinfo("screen4","the balance is" + str(cBalances[i]))

        def Loan():
            global screen6
            screen6= Toplevel(screen3)
            screen6.geometry("1100x600")
            cTitle = Label(screen6,font=('arial',30,'bold'),text=" Available Loan's are",width=40
                                        ,bg='white',fg='red').place(x=100,y=15)
            buttonVehicle=Button(screen6,text="Vehicle Loan",font=('arial',16,'bold'),height=1,
                                           width='25',bd=6,command=Vehicle).place(x=200,y=150)
            buttonGold=Button(screen6,text="Gold Loan",font=('arial',16,'bold'),height=1,
                                       width='25',bd=6,command=Gold).place(x=600,y=150)
            buttonHouse=Button(screen6,text="House Loan",font=('arial',16,'bold'),height=1,
                                       width='25',bd=6,command=House).place(x=200,y=350)
            buttonEducation=Button(screen6,text="Education Loan",font=('arial',16,'bold'),height=1,
                                       width='25',bd=6,command=Education).place(x=600,y=350)
           
        def Vehicle():
            tkinter.messagebox.showinfo("screen6","The max Loan on Vehicle is 50000Rs\n Rate of Interest is 5%")
        def Gold():    
            tkinter.messagebox.showinfo("screen6","The max Loan on Gold is 200000Rs\n Rate of Interest is 10%")
        def House():
            tkinter.messagebox.showinfo("screen6","The max Loan on House is 500000Rs\n Rate of Interest is 12%")
        def Education():
            tkinter.messagebox.showinfo("screen6","The max Loan on Education is 200000Rs\n Rate of Interest is 6%")

        def Logout(master,leader):
            tkinter.messagebox.showinfo("Logged Out","You Have Been Successfully Logged Out!!")
            master.destroy()
            leader.destroy()
            Bank(root)

        def Update():
            global screen7
            global Acc,PIn,NAme,CRdit,DEbit,BAlance
            global txtAccount,txtPin,txtName,txtcredit,txtdebit,txtbalance
            screen7= Toplevel(screen3)
            screen7.title("update Page")
            screen7.geometry("1000x600")
            Acc=StringVar()
            PIn=StringVar()
            NAme=StringVar()
            CRdit=StringVar()
            DEbit=StringVar()
            BAlance=StringVar()
            lblAccount=Label(screen7,text="Account no",font=('arial',16,'bold')
                              ,bd=20).grid(row=1,column=0)
            txtAccount=Entry(screen7,font=('arial',16,'bold'),textvariable=Acc,
                                  width=22).grid(row=1,column=1,sticky=W)
            lblPin=Label(screen7,text="PIN NO",font=('arial',16,'bold')
                              ,bd=20).grid(row=2,column=0)
            txtPin=Entry(screen7,font=('arial',16,'bold'),textvariable=PIn,
                                  width=22).grid(row=2,column=1,sticky=W)
            lblName=Label(screen7,text="Name",font=('arial',16,'bold')
                              ,bd=20).grid(row=3,column=0)
            txtName=Entry(screen7,font=('arial',16,'bold'),textvariable=NAme,
                                  width=22).grid(row=3,column=1,sticky=W)
            lblcredit=Label(screen7,text="credit amount ",font=('arial',16,'bold')
                              ,bd=20).grid(row=4,column=0)
            txtcredit=Entry(screen7,font=('arial',16,'bold'),textvariable=CRdit,
                                  width=22).grid(row=4,column=1,sticky=W)
            lbldebit=Label(screen7,text="debit Amount ",font=('arial',16,'bold')
                              ,bd=20).grid(row=5,column=0)
            txtdebit=Entry(screen7,font=('arial',16,'bold'),textvariable=DEbit,
                                  width=22).grid(row=5,column=1,sticky=W)
            lblbalance=Label(screen7,text="Balance ",font=('arial',16,'bold')
                              ,bd=20).grid(row=6,column=0)
            txtbalance=Entry(screen7,font=('arial',16,'bold'),textvariable=BAlance,
                                  width=22).grid(row=6,column=1,sticky=W)
            buttonSAVE=Button(screen7,text="SAVE",font=('arial',16,'bold'),height=1,
                                       width='25',bd=6,command=SAVE).grid(row=7,column=0,sticky=W)
           
            con = sqlite3.connect("Python_project.db")
            cur = con.cursor()
            cur.execute("SELECT *FROM Bank WHERE Accountno= " +Account_info)
            records = cur.fetchall()
            print(records)
            for record in records:
                Acc.set(record[0])
                PIn.set(record[1])
                NAme.set(record[2])
                CRdit.set(record[3])
                DEbit.set(record[4])
                BAlance.set(record[5])
            con.commit()
            con.close()

        def SAVE():
            con = sqlite3.connect("Python_project.db")
            cur = con.cursor()
            Account = Account_info
            cur.execute("""UPDATE Bank SET
                        pin= :pin,
                        Name=:name,
                        Credit=:credit,
                        Debit=:debit,
                        Balance=:balance

                        WHERE Accountno = :account""",
                        {
                            'pin':PIn.get(),
                            'name':NAme.get(),
                            'credit':CRdit.get(),
                            'debit':DEbit.get(),
                            'balance':BAlance.get(),
                            'account':Acc.get()
                            })
            con.commit()
            con.close()
            tkinter.messagebox.showinfo("screen7","Update successfully")
            PIn.set("")
            NAme.set("")
            CRdit.set("")
            DEbit.set("")
            BAlance.set("")
            Acc.set("")
        Title = Label(self.root,font=('arial',30,'bold'),text="    WELCOME TO Banking System   "
                                    ,bg='white',fg='red').place(x=100,y=15)
        buttonlogin=Button(self.root,text="Login",font=('arial',16,'bold'),height=1,
                                       width='25',bd=6,command=Login).place(x=200,y=150)
        buttoncreate=Button(self.root,text="Create Account",font=('arial',16,'bold'),height=1,
                                       width='25',bd=6,command=create).place(x=200,y=250)
        buttonexit=Button(self.root,text="Exit",font=('arial',16,'bold'),height=1,
                                       width='25',bd=6,command=close).place(x=200,y=350)
           
          
        
class Database:
    def conn(self):
        con = sqlite3.connect("Python_project.db")
        cur = con.cursor()
        query="create table if not exists Bank(Accountno integer primary key,pin integer,Name text,\
                                Credit integer,Debit integer,Balance integer)"
        cur.execute(query)
        con.commit()
        con.close()

    def insert(self,Accountno,pin,Name,Credit="",Debit="",Balance=""):
        con = sqlite3.connect("Python_project.db")
        cur = con.cursor()
        query="insert into Bank values(?,?,?,?,?,?)"
        cur.execute(query,(Accountno,pin,Name,Credit,Debit,Balance))
        con.commit()
        con.close()
        
if __name__ =='__main__':
    root=Tk()
    application=Bank(root)            
