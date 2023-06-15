from tkinter import *
from tkinter import ttk
import mysql.connector
import random
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import time



class Loan:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1295x600+230+220")
        self.root.title("Loan")

        # -----Variables------
        self.var_Loan_Id = StringVar()
        x = random.randint(980020, 980999)
        self.var_Loan_Id.set(str(x))




        self.var_Dependents = StringVar()
        self.var_IdProof = StringVar()
        self.var_IdNumber = StringVar()
        self.var_Loan_Type = StringVar()
        self.var_LoanAmount = StringVar()
        self.var_ROI = StringVar()
        self.actualname = StringVar()
        self.var_Gender = StringVar()
        self.var_Married = StringVar()
        self.var_Name = StringVar()
        self.var_ApplicantIncome = StringVar()
        self.var_Self_Employed = StringVar()
        self.var_CoapplicantIncome = StringVar()
        self.var_LoanAmount_Term = StringVar()
        self.var_Credit_History = StringVar()
        self.var_Property_Area = StringVar()
        self.var_Loan_Status = StringVar()
        self.var_Education = StringVar()


        #-----title----------
        lbl_title = Label(self.root, text="LOAN ISSUING", font=("times new roman", 18, "bold"),
                          bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=70)

        # ---------Logo--------------------
        img2 = Image.open('E:\\python project\\images\\kc.jpg')
        img2 = img2.resize((150, 70), Image.ANTIALIAS)
        self.bg1 = ImageTk.PhotoImage(img2)
        label = Label(self.root, image=self.bg1, bd=4, relief=RIDGE)
        label.place(x=0, y=0, width=150, height=70)

        # ---------Label Frame----------
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details",
                                    font=("times new roman", 9, "bold"), padx=3)
        labelframeleft.place(x=5, y=70, width=370, height=525)

        # -------Labels and Entry-----------
        # LoanId
        lbl_Loan_Id = Label(labelframeleft, text="Loan Id", font=("arial", 7, "bold"), padx=2, pady=6)
        lbl_Loan_Id.grid(row=0, column=0, sticky=W)

        enty_Loan_Id = ttk.Entry(labelframeleft,textvariable=self.var_Loan_Id, width=20, font=("arial", 9, "bold"),
                            state="readonly")
        enty_Loan_Id.grid(row=0, column=1,sticky=W)
        # Name
        lbl_name = Label(labelframeleft, text="Name :", font=("arial", 7, "bold"), padx=2, pady=6)
        lbl_name.grid(row=1, column=0, sticky=W)

        enty_name = ttk.Entry(labelframeleft, width=29,textvariable=self.var_Name,font=("arial", 9, "bold"))
        enty_name.grid(row=1, column=1,sticky=W)

        # gender
        lbl_gender = Label(labelframeleft, text="Gender :", font=("arial", 7, "bold"), padx=2, pady=6)
        lbl_gender.grid(row=2,column=0, sticky=W)

        combos_gender = ttk.Combobox(labelframeleft, textvariable=self.var_Gender, font=("arial", 9, "bold"),
                                      width=27, state="readonly")
        combos_gender["value"] = ("Male", "Female", "Others")
        combos_gender.current(1)
        combos_gender.grid(row=2, column=1)

        # Married
        lbl_married = Label(labelframeleft, text="Married :", font=("arial", 7, "bold"), padx=2, pady=6)
        lbl_married.grid(row=3, column=0, sticky=W)

        combos_gender = ttk.Combobox(labelframeleft, textvariable=self.var_Married, font=("arial", 9, "bold"),
                                     width=27, state="readonly")
        combos_gender["value"] = ("Yes", "No")
        combos_gender.current(1)
        combos_gender.grid(row=3, column=1)

        # Dependents
        lbls_Dependents = Label(labelframeleft, text="Dependents :", font=("arial", 7, "bold"), padx=2, pady=6)
        lbls_Dependents.grid(row=4, column=0, sticky=W)

        combos_Dependents = ttk.Combobox(labelframeleft,textvariable=self.var_Dependents, font=("arial", 9, "bold"), width=27,
                                     state="readonly")
        combos_Dependents["value"] = ("0", "1", "2","3+")
        combos_Dependents.current(0)
        combos_Dependents.grid(row=4, column=1)

        # Education
        lbls_Education = Label(labelframeleft, text="Education :", font=("arial", 7, "bold"), padx=2, pady=6)
        lbls_Education.grid(row=5, column=0, sticky=W)

        combos_Education = ttk.Combobox(labelframeleft, textvariable=self.var_Education, font=("arial", 9, "bold"),
                                        width=27,
                                        state="readonly")
        combos_Education["value"] = ("Graduate","Not Graduate")
        combos_Education.current(0)
        combos_Education.grid(row=5, column=1)

        # Self_Employed
        lbls_Self_Employed = Label(labelframeleft, text="Self Employed :", font=("arial", 7, "bold"), padx=2, pady=6)
        lbls_Self_Employed.grid(row=6, column=0, sticky=W)

        combos_Self_Employed = ttk.Combobox(labelframeleft, textvariable=self.var_Self_Employed, font=("arial", 9, "bold"),
                                        width=27,
                                        state="readonly")
        combos_Self_Employed["value"] = ("Yes", "No")
        combos_Self_Employed.current(0)
        combos_Self_Employed.grid(row=6, column=1)

        # ApplicantIncome
        lbl_ApplicantIncome = Label(labelframeleft, text="Applicant Income :", font=("arial", 7, "bold"), padx=2, pady=6)
        lbl_ApplicantIncome.grid(row=7, column=0, sticky=W)

        txt_ApplicantIncome = ttk.Entry(labelframeleft, width=29, textvariable=self.var_ApplicantIncome, font=("arial", 9, "bold"))
        txt_ApplicantIncome.grid(row=7, column=1)

        # CoapplicantIncome
        lbl_CoapplicantIncome = Label(labelframeleft, text="Coapplicant Income :", font=("arial", 7, "bold"), padx=2,
                                    pady=6)
        lbl_CoapplicantIncome.grid(row=8, column=0, sticky=W)

        txt_CoapplicantIncome = ttk.Entry(labelframeleft, width=29, textvariable=self.var_CoapplicantIncome,
                                        font=("arial", 9, "bold"))
        txt_CoapplicantIncome.grid(row=8, column=1)

        # Loan Amount
        lbl_LoanAmount = Label(labelframeleft, text="Loan Amount :", font=("arial", 7, "bold"), padx=2, pady=6)
        lbl_LoanAmount.grid(row=9, column=0, sticky=W)

        txt_LoanAmount = ttk.Entry(labelframeleft, textvariable=self.var_LoanAmount, width=29,
                                    font=("arial", 9, "bold"))
        txt_LoanAmount.grid(row=9, column=1)

        # LoanAmount_Term
        lbl_LoanAmount_Term = Label(labelframeleft, text="Loan Amount Term :", font=("arial", 7, "bold"), padx=2, pady=6)
        lbl_LoanAmount_Term.grid(row=10, column=0, sticky=W)

        txt_LoanAmount_Term = ttk.Entry(labelframeleft, width=29, textvariable=self.var_LoanAmount_Term, font=("arial", 9, "bold"))
        txt_LoanAmount_Term.grid(row=10, column=1)

        # Credit_History
        lbls_Credit_History = Label(labelframeleft, text="Credit History :", font=("arial", 7, "bold"), padx=2, pady=6)
        lbls_Credit_History.grid(row=11, column=0, sticky=W)

        combos_Credit_History = ttk.Combobox(labelframeleft, textvariable=self.var_Credit_History,
                                            font=("arial", 9, "bold"),
                                            width=27,
                                            state="readonly")
        combos_Credit_History["value"] = ("1", "0")
        combos_Credit_History.current(0)
        combos_Credit_History.grid(row=11, column=1)

        # Property_Area
        lbls_Property_Area = Label(labelframeleft, text="Property Area :", font=("arial", 7, "bold"), padx=2, pady=6)
        lbls_Property_Area.grid(row=12, column=0, sticky=W)

        combos_Property_Area = ttk.Combobox(labelframeleft, textvariable=self.var_Property_Area,
                                             font=("arial", 9, "bold"),
                                             width=27,
                                             state="readonly")
        combos_Property_Area["value"] = ("Urban", "Semiurban","Rural")
        combos_Property_Area.current(0)
        combos_Property_Area.grid(row=12, column=1)

        # Loan_Status
        lbls_Loan_Status = Label(labelframeleft, text="Loan Status :", font=("arial", 7, "bold"), padx=2, pady=6)
        lbls_Loan_Status.grid(row=13, column=0, sticky=W)

        combos_Loan_Status = ttk.Combobox(labelframeleft, textvariable=self.var_Loan_Status,
                                            font=("arial", 9, "bold"),
                                            width=27,
                                            state="readonly")
        combos_Loan_Status["value"] = ("Y", "N")
        combos_Loan_Status.current(0)
        combos_Loan_Status.grid(row=13, column=1)


        # id proof
        lbl_IdProof = Label(labelframeleft, text="Id Proof Type :", font=("arial", 7, "bold"), padx=2, pady=6)
        lbl_IdProof.grid(row=14, column=0, sticky=W)

        combos_IdProof = ttk.Combobox(labelframeleft,textvariable=self.var_IdProof, font=("arial",9, "bold"),
                                     width=27, state="readonly")
        combos_IdProof["value"] = ("Aadhar Card", "Pan Card", "Driving Licence", "Passport", "Ration Card", "Voter Id")
        combos_IdProof.current(1)
        combos_IdProof.grid(row=14, column=1)

        # id number
        lbl_IdNumber = Label(labelframeleft, text="Id Number :", font=("arial", 7, "bold"), padx=2, pady=6)
        lbl_IdNumber.grid(row=15, column=0, sticky=W)

        txt_IdNumber = ttk.Entry(labelframeleft,textvariable=self.var_IdNumber, width=29, font=("arial", 9, "bold"))
        txt_IdNumber.grid(row=15, column=1)

        # LoanType
        lbl_LoanType = Label(labelframeleft, text="Loan Type :", font=("arial", 7, "bold"), padx=2, pady=6)
        lbl_LoanType.grid(row=16, column=0, sticky=W)

        combos_LoanType = ttk.Combobox(labelframeleft,textvariable=self.var_Loan_Type, font=("arial", 9, "bold"), width=27,
                                       state="readonly")
        combos_LoanType["value"] = (
        "Personal Loan", "Car Loan", "Educational Loan", "Business Loan", "Gold Loan", "Home Loan")
        combos_LoanType.current(2)
        combos_LoanType.grid(row=16, column=1)

        # Interest
        lbl_ROI = Label(labelframeleft, text="Rate Of Interest  :", font=("arial", 7, "bold"), padx=2,
                                      pady=6)
        lbl_ROI.grid(row=17, column=0, sticky=W)

        txt_ROI = ttk.Entry(labelframeleft, width=20,textvariable=self.var_ROI, font=("arial", 9, "bold"),state="readonly")
        txt_ROI.grid(row=17, column=1,sticky=W)


        #------Fetch Data Button-----
        # Fetch
        btnFetch = Button(labelframeleft, text="Fetch", font=("arial", 9, "bold"), bg="black",
                         fg="gold", width=6)
        btnFetch.place(x=300,y=3)

        # ------ROI Button-----
        # ROI
        btnROI = Button(labelframeleft, text="Calculate", command=self.ROIs,font=("arial", 9, "bold"), bg="black",
                          fg="gold", width=7)
        btnROI.place(x=290, y=450)

        # ---------Button---------
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=480, width=412, height=30)

        # Save
        btnSave = Button(btn_frame, text="Save",font=("arial", 9, "bold"),command=self.save_data, bg="black",
                         fg="gold", width=8)
        btnSave.grid(row=0, column=0, padx=1)

        # update
        btnUpdate = Button(btn_frame, text="Update",font=("arial", 9, "bold"),command=self.update, bg="black",
                           fg="gold", width=6)
        btnUpdate.grid(row=0, column=1, padx=1)

        # Delete
        btnDelete = Button(btn_frame, text="Delete",font=("arial", 9, "bold"),command=self.mDelete, bg="black",
                           fg="gold", width=6)
        btnDelete.grid(row=0, column=2, padx=1)

        # reset
        btnReset = Button(btn_frame, text="Reset",font=("arial", 9, "bold"),command=self.reset, bg="black",
                          fg="gold", width=6)
        btnReset.grid(row=0, column=3, padx=1)


        # -----------Right Side Image------------------
        img3 = Image.open('E:\\python project\\images\\loan.jpg')
        img3 = img3.resize((500,270))
        self.bg2 = ImageTk.PhotoImage(img3)
        label = Label(self.root, image=self.bg2, bd=4, relief=RIDGE)
        label.place(x=760, y=70, width=500, height=270)

        # -----------Right Side Image------------------
        img4 = Image.open('E:\\python project\\images\\loan.jpg')
        img4 = img4.resize((150, 150))
        self.bg3 = ImageTk.PhotoImage(img4)
        label = Label(self.root, image=self.bg3, bd=4, relief=RIDGE)
        label.place(x=460, y=70, width=150, height=150)

        # -------tabel frame----------

        Table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System",
                                 font=("times new roman", 12, "bold"), padx=3)
        Table_frame.place(x=420, y=250, width=860, height=290)

        lblSearchBy = Label(Table_frame, text="Search By :", font=("arial", 7, "bold"), bg="red", fg="white", padx=2,
                            pady=6)
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=3)

        self.search_var = StringVar()

        combo_Search = ttk.Combobox(Table_frame, textvariable=self.search_var, font=("arial", 9, "bold"), width=27,
                                    state="readonly")
        combo_Search["value"] = ("Loan_Id", "Loan_Status", "IdNumber","Loan_Type")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=3)

        self.txt_search = StringVar()

        txtSearch = ttk.Entry(Table_frame, textvariable=self.txt_search, width=24, font=("arial", 9, "bold"))
        txtSearch.grid(row=0, column=2, padx=3)

        btnSearch = Button(Table_frame, text="Search",command=self.search, font=("arial", 10, "bold"), bg="black",
                           fg="gold", width=9)
        btnSearch.grid(row=0, column=3, padx=3)

        btnShowAll = Button(Table_frame, text="Show All",command=self.fetch_data, font=("arial", 10, "bold"),
                            bg="black", fg="gold", width=9)
        btnShowAll.grid(row=0, column=4, padx=3)

        # -----SHOW DATA--------
        details_table = Frame(Table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=60, width=860, height=210)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.cust_Details_Table = ttk.Treeview(details_table, columns=("Loan_Id", "Name", "Gender", "Married","Dependents",
                                                                       "Education", "Self_Employed", "ApplicantIncome",
                                                                       "CoapplicantIncome","LoanAmount","LoanAmount_Term",
                                                                       "Credit_History","Property_Area","Loan_Status",
                                                                       "IdProof","IdNumber","Loan_Type","ROI")
                                               , xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.cust_Details_Table.xview)
        scroll_y.config(command=self.cust_Details_Table.yview)

        self.cust_Details_Table.heading("Loan_Id", text="Loan ID")
        self.cust_Details_Table.heading("Name", text="Name")
        self.cust_Details_Table.heading("Gender", text="Gender")
        self.cust_Details_Table.heading("Married", text="Married")
        self.cust_Details_Table.heading("Dependents", text="Dependents")
        self.cust_Details_Table.heading("Education", text="Education")
        self.cust_Details_Table.heading("Self_Employed", text="Self Employed")
        self.cust_Details_Table.heading("ApplicantIncome", text="Applicant Income")
        self.cust_Details_Table.heading("CoapplicantIncome", text="Co Applicant Income")
        self.cust_Details_Table.heading("LoanAmount", text="Loan Amount")
        self.cust_Details_Table.heading("LoanAmount_Term", text="Loan Amount Term")
        self.cust_Details_Table.heading("Credit_History", text="Credit History")
        self.cust_Details_Table.heading("Property_Area", text="Property Area")
        self.cust_Details_Table.heading("Loan_Status", text="Loan Status")
        self.cust_Details_Table.heading("IdProof", text="Id Proof")
        self.cust_Details_Table.heading("IdNumber", text="Id Number")
        self.cust_Details_Table.heading("Loan_Type", text="Loan Type")
        self.cust_Details_Table.heading("ROI", text="Rate Of Interest")

        self.cust_Details_Table["show"] = "headings"

        self.cust_Details_Table.column("Loan_Id", width=100)
        self.cust_Details_Table.column("Name",width=100)
        self.cust_Details_Table.column("Gender",width=100)
        self.cust_Details_Table.column("Married", width=100)
        self.cust_Details_Table.column("Dependents", width=100)
        self.cust_Details_Table.column("Education",width=100)
        self.cust_Details_Table.column("Self_Employed", width=100)
        self.cust_Details_Table.column("ApplicantIncome", width=100)
        self.cust_Details_Table.column("CoapplicantIncome", width=100)
        self.cust_Details_Table.column("LoanAmount", width=100)
        self.cust_Details_Table.column("LoanAmount_Term", width=100)
        self.cust_Details_Table.column("Credit_History", width=100)
        self.cust_Details_Table.column("Property_Area",width=100)
        self.cust_Details_Table.column("Loan_Status", width=100)
        self.cust_Details_Table.column("IdProof", width=100)
        self.cust_Details_Table.column("IdNumber", width=100)
        self.cust_Details_Table.column("Loan_Type", width=100)
        self.cust_Details_Table.column("ROI", width=100)

        self.cust_Details_Table.pack(fill=BOTH, expand=1)
        self.cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    def save_data(self):
        if self.var_Loan_Type.get()=="" or self.var_LoanAmount.get()==""or self.var_ApplicantIncome.get()==""or self.var_IdNumber.get()==""or self.var_LoanAmount_Term.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="HardikJain@090104",database="ml")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into loan values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_Loan_Id.get(),self.var_Name.get(),self.var_Gender.get(),self.var_Married.get(),
                    self.var_Dependents.get(),self.var_Education.get(),self.var_Self_Employed.get(),self.var_ApplicantIncome.get(),
                    self.var_CoapplicantIncome.get(),self.var_LoanAmount.get(),self.var_LoanAmount_Term.get(),
                    self.var_Credit_History.get(), self.var_Property_Area.get(),self.var_Loan_Status.get(),
                    self.var_IdProof.get(),self.var_IdNumber.get(),self.var_Loan_Type.get(),self.var_ROI.get()


                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Account Successfully Created","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some Thing went wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="HardikJain@090104",
                                       database="ml")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from loan")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())
            for i in rows:
                self.cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.cust_Details_Table.focus()
        content=self.cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_Loan_Id.set(row[0])
        self.var_Name.set(row[1])
        self.var_Gender.set(row[2])
        self.var_Married.set(row[3])
        self.var_Dependents.set(row[4])
        self.var_Education.set(row[5])
        self.var_Self_Employed.set(row[6])
        self.var_ApplicantIncome.set(row[7])
        self.var_CoapplicantIncome.set(row[8])
        self.var_LoanAmount.set(row[9])
        self.var_LoanAmount_Term.set(row[10])
        self.var_Credit_History.set(row[11])
        self.var_Property_Area.set(row[12])
        self.var_Loan_Status.set(row[13])
        self.var_IdProof.set(row[14])
        self.var_IdNumber.set(row[15])
        self.var_Loan_Type.set(row[16])
        self.var_ROI.set(row[17])

    def update(self):
        if self.var_IdNumber.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="HardikJain@090104",
                                               database="ml")
                my_cursor = conn.cursor()
                my_cursor.execute("update loan set Name=%s,Gender=%s,Married=%s,Dependents=%s,Education=%s,Self_Employed=%s,ApplicantIncome=%s,"
                                  "CoapplicantIncome=%s,LoanAmount=%s,LoanAmount_Term=%s,Credit_History=%s,Property_Area=%s,"
                                  "Loan_Status=%s,IdProof=%s,IdNumber=%s,Loan_Type=%s,ROI=%s where Loan_Id=%s",(
                    self.var_Name.get(), self.var_Gender.get(), self.var_Married.get(),
                    self.var_Dependents.get(), self.var_Education.get(), self.var_Self_Employed.get(), self.var_ApplicantIncome.get(),
                    self.var_IdProof.get(), self.var_IdNumber.get(), self.var_Loan_Type.get(), self.var_LoanAmount.get(),
                    self.var_LoanAmount_Term.get(), self.var_CoapplicantIncome.get(), self. var_Credit_History.get(),
                    self.var_Property_Area.get(), self.var_ROI.get(),self.var_Loan_Id.get()
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update","Customer Details has been Updated Sucessfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Some Thing went wrong:{str(es)}", parent=self.root)


    def mDelete(self):
        mDelete=messagebox.askyesno("Deletetion","Do You Want to Delete This Customer",parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="HardikJain@090104",
                                           database="ml")
            my_cursor = conn.cursor()
            query="delete from loan where Loan_Id=%s"
            value=(self.var_Loan_Id.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
        self.var_Loan_Id.set(""),
        self.var_Name.set(""),
        self.var_Gender.set(""),
        self.var_Married.set(""),
        self.var_Dependents.set(""),
        self.var_Education.set(""),
        self.var_Self_Employed.set(""),
        self.var_ApplicantIncome.set(""),
        self.var_CoapplicantIncome.set(""),
        self.var_LoanAmount.set(""),
        self.var_LoanAmount_Term.set(""),
        self.var_Credit_History.set(""),
        self.var_Property_Area.set(""),
        self.var_Loan_Status.set(""),
        self.var_IdProof.set(""),
        self.var_IdNumber.set(""),
        self.var_Loan_Type.set(""),
        self.var_ROI.set("")



        x = random.randint(980020, 980999)
        self.var_Loan_Id.set(str(x))



    def search(self):
        if self.txt_search.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="HardikJain@090104",
                                               database="ml")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from loan where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
                rows=my_cursor.fetchall()
                if len (rows)!=0:
                    self.cust_Details_Table.delete(*self.cust_Details_Table.get_children())
                    for i in rows:
                        self.cust_Details_Table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showwarning("Warning", f"Some Thing went wrong:{str(es)}", parent=self.root)



    def ROIs(self):
        if (self.var_Loan_Type.get()=="Business Loan"):
            q1="10%"
            self.var_ROI.set(str(q1))


        elif(self.var_Loan_Type.get()=="Gold Loan"):
            q1 = "6%"
            self.var_ROI.set(str(q1))

        elif (self.var_Loan_Type.get() == "Veichle Loan"):
            q1 = "12%"
            self.var_ROI.set(str(q1))

        elif (self.var_Loan_Type.get() == "Personal Loan"):
            q1 = "13%"
            self.var_ROI.set(str(q1))

        elif (self.var_Loan_Type.get() == "Educational Loan"):
            q1 = "9%"
            self.var_ROI.set(str(q1))

        elif (self.var_Loan_Type.get() == "Home Loan"):
            q1 = "14%"
            self.var_ROI.set(str(q1))









if __name__ == '__main__':
    root=Tk()
    obj=Loan(root)
    root.mainloop()
