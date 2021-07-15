from re import search
from tkinter import*
#from PIL import Image,ImageTk
from tkinter import ttk
import tkinter
import mysql.connector
from tkinter import messagebox
from tkcalendar import DateEntry

class PharmacyManagementSystem:
        def __init__(self, root):
                self.root = root
                self.root.title("Pharmacy Management System")
                self.root.geometry("1850x850+0+0")
                self.root.resizable(0, 0)
                #===========AddMed Variables============

                self.addMed_var = StringVar()
                self.refMed_var = StringVar()

                #===============Main Variables============
                self.ref_var = IntVar()
                self.cmpName_var = StringVar()
                self.typeMed_var = StringVar()
                self.medName_var = StringVar()
                self.lot_var = StringVar()
                self.issuedate_var = StringVar()
                self.expdate_var = StringVar()
                self.uses_var = StringVar()
                self.sideEffect_var = StringVar()
                self.warning_var = StringVar()
                self.dosage_var = StringVar()
                self.price_var = DoubleVar()
                self.product_var = IntVar()

                #==============Search Variables===========

                self.search_var = StringVar()
                self.searchTxt_var = StringVar()        


                lbltitle = Label(self.root, text = "PHARAMACY MANAGEMENT SYSTEM", bd = 15, relief = RIDGE, bg = 'yellow', fg = "red", font = ("times in roman", 50, "bold"), padx = 2, pady = 4)
                lbltitle.pack(side = TOP, fill = X)
                #img1 = Image.open("")



                #============================DataFrame========================
                DataFrame = Frame(self.root, bd = 15, relief = RIDGE, padx = 20)
                DataFrame.place(x = 0, y = 120, width = 1830, height = 400)

                DataFrameLeft = LabelFrame(DataFrame, bd = 10, relief = RIDGE, padx = 20, text = "Medicine Information", fg = "darkgreen", font = ("arial", 12, "bold"))
                DataFrameLeft.place(x = 0, y = 5, width = 1100, height = 350)

                DataFramerRight = LabelFrame(DataFrame, bd = 10, relief = RIDGE, padx = 20, text = "User Management", fg = "darkgreen", font = ("arial", 12, "bold"))
                DataFramerRight.place(x = 1050, y = 5, width = 700, height = 350)


                #=========================ButtonsFrame===========================
                ButtonFrame = Frame(self.root, bd = 15, relief = RIDGE, padx = 20)
                ButtonFrame.place(x = 0, y = 520, width = 1830, height = 65)

                #=========================Main Button=============================
                btnAddData = Button(ButtonFrame, text = "Medicine Add", font = ("arial", 13, "bold"), bg = "darkgreen", fg = "white", command=self.add_data)
                btnAddData.grid(row = 0, column = 0)

                btnAddData = Button(ButtonFrame, text = "UPDATE", font = ("arial", 13, "bold"), bg = "darkgreen", fg = "white", command = self.Update)
                btnAddData.grid(row = 0, column = 1)

                btnAddData = Button(ButtonFrame, text = "DELETE", font = ("arial", 13, "bold"), bg = "red", fg = "white", command = self.delete)
                btnAddData.grid(row = 0, column = 2)

                btnAddData = Button(ButtonFrame, text = "RESET", font = ("arial", 13, "bold"), bg = "darkgreen", fg = "white", command = self.reset)
                btnAddData.grid(row = 0, column = 3)

                btnAddData = Button(ButtonFrame, text = "EXIT", font = ("arial", 13, "bold"), bg = "darkgreen", fg = "white", command = self.exitC)
                btnAddData.grid(row = 0, column = 4)


                #==================Search By=====================

                lblSearch = Label(ButtonFrame, font = ("arial", 17, "bold"), width = 25, text = "Search By", padx = 2, bg = "red", fg = "white")
                lblSearch.grid(row = 0, column = 5, sticky = W)

                #==================variable======================
                

                search_combo = ttk.Combobox(ButtonFrame, textvariable = self.search_var, width = 20, font = ("arial", 17, "bold"), state = "readonly")
                search_combo.grid(row = 0, column = 6)
                search_combo["values"] = ("ref_no", "Medname", "Lotno")
                search_combo.grid(row = 0, column = 6)
                search_combo.current(0)

                txtSearch = Entry(ButtonFrame, textvariable = self.searchTxt_var, bd = 3, relief = RIDGE, width = 20, font = ("arial", 17, "bold"))
                txtSearch.grid(row = 0, column = 7)

                searchBtn = Button(ButtonFrame, command = self.search_data, text = "SEARCH", font = ("arial", 15, "bold"), width = 15, bg = "darkgreen", fg = "white")
                searchBtn.grid(row = 0, column = 8)

                searchBtn = Button(ButtonFrame, command = self.fetch_data, text = "SHOW ALL", font = ("arial", 15, "bold"), width = 15, bg = "darkgreen", fg = "white")
                searchBtn.grid(row = 0, column = 9)

                #====================label and entry============================

                Framedetails = Frame(self.root, bd = 15, relief = RIDGE)
                Framedetails.place(x = 0, y = 590, width = 1830, height = 250)

                lblrefno = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Reference No", padx = 2)
                lblrefno.grid(row = 0, column = 0, sticky = W)
                ref_combo = Entry(DataFrameLeft, textvariable = self.ref_var, font = ("arial", 17, "bold"), bg = "white", bd = 2, relief = RIDGE, width = 25)
                ref_combo.grid(row = 0, column = 1)

                lblCompanyName = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Company Name:", padx = 2, pady = 6)
                lblCompanyName.grid(row = 1, column = 0, sticky = W)
                txtCompanyName = Entry(DataFrameLeft, textvariable = self.cmpName_var, font = ("arial", 17, "bold"), bg = "white", bd = 2, relief = RIDGE, width = 25)
                txtCompanyName.grid(row = 1, column = 1)


                lblTypeofMedicine = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Type of Medicine ", padx = 2, pady = 6)
                lblTypeofMedicine .grid(row = 2, column = 0, sticky = W)
                txtTypeofMedicine = Entry(DataFrameLeft, textvariable = self.typeMed_var, font = ("arial", 17, "bold"), bg = "white", bd = 2, relief = RIDGE, width = 25)
                txtTypeofMedicine.grid(row = 2, column = 1)

                
                lblMedicineName = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Medicine Name", padx = 2, pady = 6)
                lblMedicineName.grid(row = 3, column = 0, sticky = W)
                txtMedicineName = Entry(DataFrameLeft, textvariable = self.medName_var, font = ("arial", 17, "bold"), bg = "white", bd = 2, relief = RIDGE, width = 25)
                txtMedicineName.grid(row = 3, column = 1)


                lblLotNo = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Lot No:", padx = 2, pady = 6)
                lblLotNo.grid(row = 4, column = 0, sticky = W)
                txtLotNo = Entry(DataFrameLeft, textvariable = self.lot_var, font = ("arial", 17, "bold"), bg = "white", bd = 2, relief = RIDGE, width = 25)
                txtLotNo.grid(row = 4, column = 1)

                        
                lblIssueDate = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Issue Date:", padx = 2, pady = 6)
                lblIssueDate.grid(row = 5, column = 0, sticky = W)
                lblIssueDate = DateEntry(DataFrameLeft, textvariable = self.issuedate_var, font = ("arial", 17, "bold"), bg = "white", bd = 2, relief = RIDGE, width = 25, date_pattern = 'yyyy/mm/dd')
                lblIssueDate.grid(row =  5, column = 1) 

                lblExpDate = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Exp Date:", padx = 2, pady = 6)
                lblExpDate.grid(row = 6, column = 0, sticky = W)
                lblExpDate = DateEntry(DataFrameLeft, textvariable = self.expdate_var, font = ("arial",17,"bold"), bg = "white", bd = 2, relief = RIDGE, width = 25, date_pattern = 'yyyy/mm/dd')
                lblExpDate.grid(row = 6, column = 1) 


                lblUses = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Uses:", padx = 2, pady = 6)
                lblUses.grid(row = 7, column = 0, sticky = W)
                lblUses = Entry(DataFrameLeft, textvariable = self.uses_var, font = ("arial", 17, "bold"), bg = "white", bd = 2, relief = RIDGE, width = 25)
                lblUses.grid(row = 7, column = 1) 


                lblSideEffect = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Side Effect:", padx = 2, pady = 6)
                lblSideEffect.grid(row = 8, column = 0, sticky = W)
                lblSideEffect = Entry(DataFrameLeft, textvariable = self.sideEffect_var, font = ("arial", 17, "bold"), bg = "white", bd = 2, relief = RIDGE, width = 25)
                lblSideEffect.grid(row = 8, column = 1) 


                lblProcwarning = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Proc&warning:", padx = 2, pady = 6)
                lblProcwarning.grid(row = 0, column = 2, sticky = W)
                lblProcwarning = Entry(DataFrameLeft, textvariable = self.warning_var, font = ("arial", 17, "bold"), bg = "white", bd = 2, relief = RIDGE, width = 25)
                lblProcwarning.grid(row = 0, column = 3) 


                lblDossage = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Dossage :", padx = 2, pady = 6)
                lblDossage.grid(row = 1, column = 2, sticky = W)
                lblDossage = Entry(DataFrameLeft, textvariable = self.dosage_var, font = ("arial", 17, "bold"), bg = "white", bd = 2, relief = RIDGE, width = 25)
                lblDossage.grid(row = 1, column = 3) 


                lblPrice = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Tablets Price:", padx = 2, pady = 6)
                lblPrice.grid(row = 2, column = 2, sticky = W)
                lblPrice = Entry(DataFrameLeft, textvariable = self.price_var, font = ("arial", 17, "bold"), bg = "white", bd = 2, relief = RIDGE, width = 25)
                lblPrice.grid(row = 2, column = 3) 


                lblProduct = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Product QTY:", padx = 2, pady = 6)
                lblProduct.grid(row = 3, column = 2, sticky = W)
                lblProduct = Entry(DataFrameLeft, textvariable = self.product_var, font = ("arial", 17, "bold"), bg = "white", bd = 2, relief = RIDGE, width = 25)
                lblProduct.grid(row = 3, column = 3) 



                #============================UserAdd Dataframe=====================================
                lblrefno = Label(DataFramerRight, font = ("arial", 12, "bold"), text = "UserName", padx = 2, pady = 6)
                lblrefno.place(x = 0, y = 80)
                lblrefno = Entry(DataFramerRight, textvariable = self.refMed_var, font = ("arial", 15, "bold"), bg = "white", bd = 2, relief = RIDGE, width = 25)
                lblrefno.place(x = 135, y = 80)
                
                lblmedName = Label(DataFramerRight, font = ("arial", 12, "bold"), text = "Password", padx = 2, pady = 6)
                lblmedName.place(x = 0, y = 110)
                lblmedName = Entry(DataFramerRight, textvariable = self.addMed_var, font = ("arial", 15, "bold"), bg = "white", bd = 2, relief = RIDGE, width = 25)
                lblmedName.place(x = 135, y = 110)




                #============================Side Frame=====================================
                side_frame = Frame(DataFramerRight, bd = 4, relief = RIDGE, bg = "white")
                side_frame.place(x = 0, y = 150, width = 350, height = 160)

                sc_x = ttk.Scrollbar(side_frame, orient = HORIZONTAL)
                sc_x.pack(side = BOTTOM, fill = X)
                sc_y = ttk.Scrollbar(side_frame, orient = VERTICAL)
                sc_y.pack(side = RIGHT, fill = Y)

                self.medicine_table = ttk.Treeview(side_frame, column = ("ref", "medname"), xscrollcommand = sc_x.set, yscrollcommand = sc_y.set)

                sc_x.config(command = self.medicine_table.xview)
                sc_y.config(command = self.medicine_table.yview)


                self.medicine_table.heading("ref", text = "Username")
                self.medicine_table.heading("medname", text = "Password")

                self.medicine_table["show"] = "headings"
                self.medicine_table.pack(fill = BOTH, expand = 1)

                self.medicine_table.column("ref", width = 30)
                self.medicine_table.column("medname", width = 100) 

                self.fetch_dataMed()  

                self.medicine_table.bind("<ButtonRelease-1>", self.Medget_cursor)

                #=================Medicine Add Button======================
                down_frame = Frame(DataFramerRight, bd = 4, relief = RIDGE, bg = "darkgreen")
                down_frame.place(x = 360, y = 150, width = 135, height = 160)
                
                btnAddmed = Button(down_frame, text = "Add", font = ("arial", 13, "bold"), width = 12, bg = "green", fg = "white", pady = 4, command = self.AddMed)
                btnAddmed.grid(row = 0, column = 0)

                btnUpdatemed = Button(down_frame, text = "UPDATE", font = ("arial", 13, "bold"), width = 12, bg = "purple", fg = "white", pady = 4, command = self.UpdateMed)
                btnUpdatemed.grid(row = 1, column = 0)

                btnDeletemed = Button(down_frame, text = "DELETE", font = ("arial", 13, "bold"), width = 12, bg = "red", fg = "white", pady = 4, command = self.DeleteMed)
                btnDeletemed.grid(row = 2, column = 0)

                btnClearmed = Button(down_frame, text = "CLEAR", font = ("arial", 13, "bold"), width = 12, bg = "orange", fg = "white", pady = 4, command = self.ClearMed)
                btnClearmed.grid(row = 3, column = 0)


                #================frame Details=========================

                        
                        



                #==================main table and scrollbar============
                Table_frame = Frame(self.root, bd = 15, relief = RIDGE)
                Table_frame.place(x = 15, y = 605, width = 1800, height = 220)
                    
                scroll_x = ttk.Scrollbar(Table_frame, orient = HORIZONTAL)
                scroll_x.pack(side = BOTTOM, fill = X)
                scroll_y = ttk.Scrollbar(Table_frame, orient = VERTICAL)
                scroll_y.pack(side = BOTTOM, fill = Y)
                    
                self.pharmacy_table = ttk.Treeview(Table_frame, column = ("ref", "companyname", "type", "tabletname", "lotno", "issuedate", "expdate", "uses", "sideeffect", "warning", "dosage", "price", "productqt"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
                        
                scroll_x.pack(side = BOTTOM, fill = X)
                scroll_y.pack(side = RIGHT, fill = Y)

                scroll_x.config(command = self.pharmacy_table.xview)
                scroll_y.config(command = self.pharmacy_table.yview)

                self.pharmacy_table["show"] = "headings"

                self.pharmacy_table.heading("ref", text = "Reference No")
                self.pharmacy_table.heading("companyname", text = "Company Name")
                self.pharmacy_table.heading("type", text = "Type of Medicine")
                self.pharmacy_table.heading("tabletname", text = "Tablet Name")
                self.pharmacy_table.heading("lotno", text = "Lot No")
                self.pharmacy_table.heading("issuedate", text = "Issue Date")
                self.pharmacy_table.heading("expdate", text = "Exp Date")
                self.pharmacy_table.heading("uses", text = "Uses")
                self.pharmacy_table.heading("sideeffect", text = "Side Effect")
                self.pharmacy_table.heading("warning", text = "Proc&Warning")
                self.pharmacy_table.heading("dosage", text = "Dosage")
                self.pharmacy_table.heading("price", text = "Price")
                self.pharmacy_table.heading("productqt", text = "Product Qts")
                self.pharmacy_table.pack(fill = BOTH, expand = 1)



                self.fetch_dataMed()    
                self.fetch_data()
                self.pharmacy_table.bind("<ButtonRelease-1>", self.get_cursor)

                root.mainloop()
                    
            
        #========================Add Medicine Functionality Declaration============

                    
        def AddMed(self):
                try :
                        user = self.refMed_var.get()
                        passw = self.addMed_var.get()
                        if user == "" or passw == "" :
                                messagebox.showwarning("Warning","Username and Password cannot be empty")
                        elif user[0].isdigit() :
                                messagebox.showwarning("Warning","Username cannot start with digit")
                        else :
                                conn = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "mydata")
                                my_cursor = conn.cursor()
                                my_cursor.execute('insert into login(uid,pass) values(%s,%s)', (self.refMed_var.get(), self.addMed_var.get(), ))
                                conn.commit()
                                self.fetch_dataMed()
                                conn.close()
                                messagebox.showinfo("Success", "User Added")
                except mysql.connector.errors.IntegrityError :
                        messagebox.showerror("Invalid Username","Username Already Exists")
                                                                                                    
        def fetch_dataMed(self):
                conn = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "mydata")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from login")
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.medicine_table.delete(*self.medicine_table.get_children())
                    for i in rows:
                        self.medicine_table.insert("", END, values = i)
                    conn.commit()
                conn.close()

        # =========Medgetcursor=======================

        def Medget_cursor(self, event = ""):
                try :
                        cursor_rows= self.medicine_table.focus()
                        content = self.medicine_table.item(cursor_rows)
                        row = content["values"]
                        self.refMed_var.set(row[0])
                        self.addMed_var.set(row[1])
                except IndexError:
                        messagebox.showwarning("Warning","Please Select Proper data")

        def UpdateMed(self):
                if self.refMed_var.get() == "" or self.addMed_var.get() == "":
                    messagebox.showerror("Error","All fields are Required")
                else:
                    conn = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "mydata")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update login set pass=%s where uid=%s", (self.addMed_var.get(), self.refMed_var.get(), ))                                        
                    conn.commit()
                    self.fetch_dataMed()
                    conn.close()
                    messagebox.showinfo("Success", "Password has been Updated")


        def DeleteMed(self):
                user = self.refMed_var.get()
                if user == "admin" :
                        messagebox.showerror("Invalid","Cannot Delete Admin")
                else :
                        conn = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "mydata")
                        my_cursor=conn.cursor()
                        sq1 = "delete from login where uid=%s"
                        val = (self.refMed_var.get(), )
                        my_cursor.execute(sq1, val)
                        conn.commit()
                        self.fetch_dataMed()
                        conn.close()

        def ClearMed(self):
                self.refMed_var.set("")
                self.addMed_var.set("")


        #=================Main Table==========================

        def add_data(self):
                try:
                        conn = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "mydata")
                        my_cursor = conn.cursor()
                        my_cursor.execute("insert into pharmacy(ref_no,CmpName,TypeMed,Medname,Lotno,Issue_Date,ExpDate,uses,sideeffect,warning,dosage,price,quantity) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.ref_var.get(), self.cmpName_var.get(), self.typeMed_var.get(), self.medName_var.get(), self.lot_var.get(), self.issuedate_var.get(), self.expdate_var.get(), self.uses_var.get(), self.sideEffect_var.get(), self.warning_var.get(), self.dosage_var.get(), self.price_var.get(), self.product_var.get()))       
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success", "MedicineData has been inserted")
                except tkinter.TclError :
                        messagebox.showwarning("Data Error","Please check the entered Data for ReferenceId, Price and Quantity \n Reference Id Should be integer")
                except mysql.connector.errors.IntegrityError :
                        messagebox.showerror("Error","Reference ID Already Exists")  

        def fetch_data(self):
                conn = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "mydata")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from pharmacy ")
                row=my_cursor.fetchall()
                if len(row) != 0:
                    self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                    for i in row:
                        self.pharmacy_table.insert("", END, values = i)
                    conn.commit()
                conn.close()


        def get_cursor(self, ev = ""):
                try :
                        cursor_rows= self.pharmacy_table.focus()
                        content = self.pharmacy_table.item(cursor_rows)
                        row = content["values"]
                        self.ref_var.set(row[0])
                        self.cmpName_var.set(row[1])
                        self.typeMed_var.set(row[2])
                        self.medName_var.set(row[3])
                        self.lot_var.set(row[4])
                        self.issuedate_var.set(row[5])
                        self.expdate_var.set(row[6])
                        self.uses_var.set(row[7])
                        self.sideEffect_var.set(row[8])
                        self.warning_var.set(row[9])
                        self.dosage_var.set(row[10])
                        self.price_var.set(row[11])
                        self.product_var.set(row[12])
                except IndexError:
                        messagebox.showwarning("Warning","Please Select Proper data")
                    

        def Update(self):
                if self.ref_var.get() == "" or self.lot_var.get() == "":
                    messagebox.showerror("Error", "All fields are Required")
                else:
                        try:
                                conn = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "mydata")
                                my_cursor=conn.cursor()
                                my_cursor.execute("update pharmacy set CmpName=%s, TypeMed=%s, MedName=%s, Lotno=%s, Issue_Date=%s, ExpDate=%s, uses=%s, sideeffect=%s, warning=%s, dosage=%s, price=%s, quantity=%s where ref_no=%s", (self.cmpName_var.get(), self.typeMed_var.get(), self.medName_var.get(), self.lot_var.get(), self.issuedate_var.get(), self.expdate_var.get(), self.uses_var.get(), self.sideEffect_var.get(), self.warning_var.get(), self.dosage_var.get(), self.price_var.get(), self.product_var.get(), self.ref_var.get(), ))                
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("UPDATE", "Record has been Updated Successfully")
                        except tkinter.TclError :
                                messagebox.showwarning("Data Error","Please check the entered Data for ReferenceId, Price and Quantity")

        def delete(self):
                conn = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "mydata")
                my_cursor = conn.cursor()
                my_cursor.execute("delete from pharmacy where ref_no=%s", (self.ref_var.get(), ))              
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "info deleted successfully")

        def reset(self):

                self.ref_var.set(""),
                self.cmpName_var.set(""),
                self.typeMed_var.set(""),
                self.medName_var.set(""),
                self.lot_var.set(""),
                #self.issuedate_var.set(""),
                #self.expdate_var.set(""),
                self.uses_var.set(""),
                self.sideEffect_var.set(""),
                self.warning_var.set(""),
                self.dosage_var.set(""),
                self.price_var.set(""),
                self.product_var.set("")


        def search_data(self):
                conn = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "mydata")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from pharmacy where "+str(self.search_var.get())+" LIKE '%"+str(self.searchTxt_var.get())+"%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                        for i in rows:
                                self.pharmacy_table.insert("", END, values = i)
                        conn.commit()
                conn.close()
        
        def exitC(self):
                exit()


# if __name__ == "__main__":
#         root = Tk()
#         obj = PharmacyManagementSystem(root)
#         root.mainloop()                                                                                                                                                                                                                                     
