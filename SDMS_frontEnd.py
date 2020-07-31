#Fronted
from tkinter import*
import tkinter.messagebox
import stddata_backEnd

class Student:

    def __init__(self,root):
        self.root=root
        self.root.title(" Student Database Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")
        StdID=StringVar()
        Firstname=StringVar()
        Surname=StringVar()
        DOB=StringVar()
        Age=StringVar()
        Gender=StringVar()
        Address=StringVar()
        Mobile=StringVar()
        #================================functions==================

        def iexit():
            iexit=tkinter.messagebox.askyesno('Student Database Management System','Confirm if you want to exit')
            if iexit >0:
                root.destroy()
                return

        def clearData():
            self.txtStdID.delete(0,END)
            self.txtfna.delete(0,END)
            self.txtSna.delete(0,END)
            self.txtDob.delete(0,END)
            self.txtAge.delete(0,END)
            self.txtgnd.delete(0,END)
            self.txtadd.delete(0,END)
            self.txtmob.delete(0,END)

        def addData():
            if(len(StdID.get())!=0):
                stddata_backEnd.addStdRec(StdID.get(),Firstname.get(),Surname.get(),DOB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(),Firstname.get(),Surname.get(),DOB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get()))

        def Display():
            studentlist.delete(0,END)
            for row in stddata_backEnd.viewData():
                studentlist.insert(END,row,str(""))

        def StudentRec(event):
            global sd
            searchStd=studentlist.curselection()[0]
            sd= studentlist.get(searchStd)

            self.txtStdID.delete(0,END)
            self.txtStdID.insert(END,sd[1])
            self.txtfna.delete(0,END)
            self.txtfna.insert(END,sd[2])
            self.txtSna.delete(0,END)
            self.txtSna.insert(END,sd[3])
            self.txtDob.delete(0,END)
            self.txtDob.insert(END,sd[4])
            self.txtAge.delete(0,END)
            self.txtAge.insert(END,sd[5])
            self.txtgnd.delete(0,END)
            self.txtgnd.insert(END,sd[6])
            self.txtadd.delete(0,END)
            self.txtadd.insert(END,sd[7])
            self.txtmob.delete(0,END)
            self.txtmob.insert(END,sd[8])
            

        def DeleteData():
            if(len(StdID.get())!=0):
                stddata_backEnd.deleteRec(sd[0])
                clearData()
                DisplayData()

        def searchDatabase():
            studentlist.delete(0,END)
            for row in stddata_backEnd.searchData(StdID.get(),Firstname.get(),Surname.get(),DOB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get()):
                studentlist.insert(END,row,str(""))

        def update():
            if(len(StdID.get())!=0):
                stddata_backEnd.deleteRec(sd[0])
            if(len(StdID.get())!=0):
                stddata_backEnd.searchData(StdID.get(),Firstname.get(),Surname.get(),DOB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(),Firstname.get(),Surname.get(),DOB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get()))
                

                

                
                    
                
            
            


        #===============================Frames==============
        MainFrame=Frame(self.root,bg='cadet blue')
        MainFrame.grid()
        TitFrame=Frame(MainFrame,bd=2,padx=54,pady=8,bg='Ghost White',relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit=Label(TitFrame,font=('arial',47,'bold'),text='Student Management System')
        self.lblTit.grid()

        ButtonFrame=Frame(MainFrame,bd=2,width=1350,height=70,padx=18,pady=10,bg='Ghost White',relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,bd=1,width=1300,height=400,padx=20,pady=20,bg='Ghost White',relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft=LabelFrame(DataFrame,bd=1,width=1000,height=600,padx=20,bg='Ghost White',font=('arial',47,'bold'),text='Student Information\n',relief=RIDGE)
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight=LabelFrame(DataFrame,bd=1,width=450,height=300,padx=31,pady=3,bg='Ghost White',font=('arial',20,'bold'),text='Student Details\n',relief=RIDGE)
        DataFrameRight.pack(side=RIGHT)    
        #===============================Labels and Widget==============
        self.lblStdID=Label(DataFrameLeft,font=('arial',20,'bold'),text='Student ID  :',padx=2,pady=2)
        self.lblStdID.grid(row=0,column=0,sticky=W)
        self.txtStdID=Entry(DataFrameLeft,font=('arial',20,'bold'),textvariable=StdID,width=39)
        self.txtStdID.grid(row=0,column=1)

        self.lblfna=Label(DataFrameLeft,font=('arial',20,'bold'),text='First Name :',padx=2,pady=2)
        self.lblfna.grid(row=1,column=0,sticky=W)
        self.txtfna=Entry(DataFrameLeft,font=('arial',20,'bold'),textvariable=Firstname,width=39)
        self.txtfna.grid(row=1,column=1)

        self.lblSna=Label(DataFrameLeft,font=('arial',20,'bold'),text='Surname    :',padx=2,pady=2)
        self.lblSna.grid(row=2,column=0,sticky=W)
        self.txtSna=Entry(DataFrameLeft,font=('arial',20,'bold'),textvariable=Surname,width=39)
        self.txtSna.grid(row=2,column=1)

        self.lblDob=Label(DataFrameLeft,font=('arial',20,'bold'),text='DateOfBirth:',padx=2,pady=2)
        self.lblDob.grid(row=3,column=0,sticky=W)
        self.txtDob=Entry(DataFrameLeft,font=('arial',20,'bold'),textvariable=DOB,width=39)
        self.txtDob.grid(row=3,column=1)

        self.lblAge=Label(DataFrameLeft,font=('arial',20,'bold'),text='Age             :',padx=2,pady=2)
        self.lblAge.grid(row=4,column=0,sticky=W)
        self.txtAge=Entry(DataFrameLeft,font=('arial',20,'bold'),textvariable=Age,width=39)
        self.txtAge.grid(row=4,column=1)

        self.lblgnd=Label(DataFrameLeft,font=('arial',20,'bold'),text='Gender       :',padx=2,pady=2)
        self.lblgnd.grid(row=5,column=0,sticky=W)
        self.txtgnd=Entry(DataFrameLeft,font=('arial',20,'bold'),textvariable=Gender,width=39)
        self.txtgnd.grid(row=5,column=1)

        self.lbladd=Label(DataFrameLeft,font=('arial',20,'bold'),text='Address     :',padx=2,pady=2)
        self.lbladd.grid(row=6,column=0,sticky=W)
        self.txtadd=Entry(DataFrameLeft,font=('arial',20,'bold'),textvariable=Address,width=39)
        self.txtadd.grid(row=6,column=1)

        self.lblmob=Label(DataFrameLeft,font=('arial',20,'bold'),text='Mobile        :',padx=2,pady=2)
        self.lblmob.grid(row=7,column=0,sticky=W)
        self.txtmob=Entry(DataFrameLeft,font=('arial',20,'bold'),textvariable=Mobile,width=39)
        self.txtmob.grid(row=7,column=1)

        #===============================ListBox and Scrollbar================
        scrollbar=Scrollbar(DataFrameRight)
        scrollbar.grid(row=0,column=1,sticky='ns')

        studentlist=Listbox(DataFrameRight,width=41,height=16,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>',StudentRec)
        studentlist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=studentlist.yview)
        #===========================button=======================

        self.btnAddData=Button(ButtonFrame,text='Add New',font=('arial',20,'bold'),height=1,width=10,bd=3,command=addData)
        self.btnAddData.grid(row=0,column=0)

        self.btnDisplayData=Button(ButtonFrame,text='Display',font=('arial',20,'bold'),height=1,width=10,bd=3,command=Display)
        self.btnDisplayData.grid(row=0,column=1)

        self.btnClearData=Button(ButtonFrame,text='Clear',font=('arial',20,'bold'),height=1,width=10,bd=3,command=clearData)
        self.btnClearData.grid(row=0,column=2)

        self.btnDeleteData=Button(ButtonFrame,text='Delete',font=('arial',20,'bold'),height=1,width=10,bd=3,command=DeleteData)
        self.btnDeleteData.grid(row=0,column=3)

        self.btnSearchData=Button(ButtonFrame,text='Search',font=('arial',20,'bold'),height=1,width=10,bd=3,command=searchDatabase)
        self.btnSearchData.grid(row=0,column=4)

        self.btnUpdateData=Button(ButtonFrame,text='Update',font=('arial',20,'bold'),height=1,width=10,bd=3,command=update)
        self.btnUpdateData.grid(row=0,column=5)

        self.btnExitData=Button(ButtonFrame,text='Exit',font=('arial',20,'bold'),height=1,width=6,bd=3,command=iexit)
        self.btnExitData.grid(row=0,column=6)
            
        
if __name__=='__main__':
    root=Tk()
    application=Student(root)
    root.mainloop()
    
