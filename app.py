from tkinter import *
import random

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width = 1280,height = 700)
        self.root.minsize(width = 1280,height = 700)
        self.root.title("Billing Software")
        
        #====================Variables========================#
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        #For Generating Random Bill Numbers
        x = random.randint(1000,9999)
        self.c_bill_no = StringVar()
        #Seting Value to variable
        self.c_bill_no.set(str(x))

        self.bathing_soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.hair_spray = IntVar()
        self.body_lotion = IntVar()
        self.rice = IntVar()
        self.Dal = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.maaza = IntVar()
        self.coke = IntVar()
        self.Mountain_dew = IntVar()
        self.Red_bull = IntVar()
        self.biscuits = IntVar()
        self.total_cosmetics = StringVar()
        self.total_grocery = StringVar()
        self.total_other = StringVar()
        self.tax_cos = StringVar()
        self.tax_groc = StringVar()
        self.tax_other = StringVar()


        #===================================
        bg_color = "Green"
        fg_color = "white"
        lbl_color = 'pink'
        btn_color = 'red'
        #Title of App
        title = Label(self.root,text = "Billing Software",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)

        #==========Customers Frame==========#
        F1 = LabelFrame(text = "Customer Details",font = ("time new roman",12,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
        F1.place(x = 0,y = 80,relwidth = 1)

        #===============Customer Name===========#
        cname_lbl = Label(F1,text="Customer Name",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
        cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.cus_name)
        cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

        #=================Customer Phone==============#
        cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
        cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_phone)
        cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)

        #====================Customer Bill No==================#
        cbill_lbl = Label(F1,text = "Bill No.",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold"))
        cbill_lbl.grid(row = 0,column = 4,padx = 20)
        cbill_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_bill_no)
        cbill_en.grid(row = 0,column = 5,ipadx = 30,ipady = 4,pady = 5)
        
        #====================Bill Search Button===============#
        bill_btn = Button(F1,text = "Enter",bd = 7,relief = GROOVE,font = ("times new roman",12,"bold"),bg = btn_color,fg = fg_color)
        bill_btn.grid(row = 0,column = 6,ipady = 5,padx = 60,ipadx = 19,pady = 5)

        #==================Cosmetics Frame=====================#
        F2 = LabelFrame(self.root,text = 'Cosmetics',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 5,y = 180,width = 325,height = 380)

        #===========Frame Content===============================#
        bath_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Bath Soap")
        bath_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        bath_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.bathing_soap)
        bath_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======Face Cream
        face_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Face Cream")
        face_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.face_cream)
        face_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #========Face Wash
        wash_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Face Wash")
        wash_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        wash_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.face_wash)
        wash_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========Hair Spray
        hair_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Hair Spray")
        hair_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        hair_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.hair_spray)
        hair_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============Body Lotion
        lot_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Body Lotion")
        lot_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        lot_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.body_lotion)
        lot_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================Grocery Frame=====================#
        F2 = LabelFrame(self.root,text = 'Grocery',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 330,y = 180,width = 325,height = 380)

        #===========Frame Content=============================#
        rice_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Rice")
        rice_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        rice_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.rice)
        rice_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======Food oil
        oil_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Food Oil")
        oil_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        oil_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.food_oil)
        oil_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======Dal
        Dal_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Dal")
        Dal_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        Dal_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Dal)
        Dal_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========Wheat
        wheat_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Wheat")
        wheat_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        wheat_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.wheat)
        wheat_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============Sugar
        sugar_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Sugar")
        sugar_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        sugar_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.sugar)
        sugar_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================Other Stuff=====================#

        F2 = LabelFrame(self.root,text = 'Others',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 655,y = 180,width = 325,height = 380)

        #===========Frame Content
        maaza_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Maaza")
        maaza_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        maaza_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.maaza)
        maaza_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======Coke
        cock_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Coke")
        cock_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        cock_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.coke)
        cock_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======Mountain dew
        Mountain_dew_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Mountain dew")
        Mountain_dew_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        Mountain_dew_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Mountain_dew)
        Mountain_dew_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========Red bull
        cold_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Red bull")
        cold_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        cold_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Red_bull)
        cold_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============Biscuits
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Biscuits")
        bis_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        bis_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.biscuits)
        bis_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #===================Bill Aera================#
        F3 = Label(self.root,bd = 5,relief = GROOVE)
        F3.place(x = 960,y = 180,width = 325,height = 380)
        #===========
        bill_title = Label(F3,text = "Bill Area",font = ("Lucida",13,"bold"),bd= 7,relief = GROOVE)
        bill_title.pack(fill = X)

        #============
        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)

        #===========Buttons Frame=============#
        F4 = LabelFrame(self.root,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F4.place(x = 0,y = 560,relwidth = 1,height = 145)

        #===================
        cosm_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Cosmetics")
        cosm_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
        cosm_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_cosmetics)
        cosm_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)

        #===================
        gro_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Grocery")
        gro_lbl.grid(row = 1,column = 0,padx = 10,pady = 5)
        gro_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_grocery)
        gro_en.grid(row = 1,column = 1,ipady = 2,ipadx = 5)

        #================
        oth_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Others Total")
        oth_lbl.grid(row = 2,column = 0,padx = 10,pady = 5)
        oth_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_other)
        oth_en.grid(row = 2,column = 1,ipady = 2,ipadx = 5)

        #================
        cosmt_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Cosmetics Tax")
        cosmt_lbl.grid(row = 0,column = 2,padx = 30,pady = 0)
        cosmt_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_cos)
        cosmt_en.grid(row = 0,column = 3,ipady = 2,ipadx = 5)

        #=================
        grot_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Grocery Tax")
        grot_lbl.grid(row = 1,column = 2,padx = 30,pady = 5)
        grot_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_groc)
        grot_en.grid(row = 1,column = 3,ipady = 2,ipadx = 5)

        #==================
        otht_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Others Tax")
        otht_lbl.grid(row = 2,column = 2,padx = 10,pady = 5)
        otht_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_other)
        otht_en.grid(row = 2,column = 3,ipady = 2,ipadx = 5)

        #====================
        total_btn = Button(F4,text = "Total",bg = btn_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.total)
        total_btn.grid(row = 1,column = 4,ipadx = 20,padx = 30)

        #========================
        genbill_btn = Button(F4,text = "Generate Bill",bg = btn_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.bill_area)
        genbill_btn.grid(row = 1,column = 5,ipadx = 20)

        #====================
        clear_btn = Button(F4,text = "Clear",bg = btn_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.clear)
        clear_btn.grid(row = 1,column = 6,ipadx = 20,padx = 30)

        #======================
        exit_btn = Button(F4,text = "Exit",bg = btn_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.exit)
        exit_btn.grid(row = 1,column = 7,ipadx = 20)

#Function to get total prices
    def total(self):
        #=================Total Cosmetics Prices
        self.total_cosmetics_prices = (
            (self.bathing_soap.get() * 40)+
            (self.face_cream.get() * 200)+
            (self.face_wash.get() * 150)+
            (self.hair_spray.get() * 340)+
            (self.body_lotion.get() * 260)
        )
        self.total_cosmetics.set("Rs. "+str(self.total_cosmetics_prices))
        self.tax_cos.set("Rs. "+str(round(self.total_cosmetics_prices*0.05)))
        #====================Total Grocery Prices
        self.total_grocery_prices = (
            (self.wheat.get()*100)+
            (self.food_oil.get() * 180)+
            (self.Dal.get() * 80)+
            (self.rice.get() *120)+
            (self.sugar.get() * 170)

        )
        self.total_grocery.set("Rs. "+str(self.total_grocery_prices))
        self.tax_groc.set("Rs. "+str(round(self.total_grocery_prices*0.05)))
        #======================Total Other Prices
        self.total_other_prices = (
            (self.maaza.get() * 10)+
            (self.Mountain_dew.get() * 30)+
            (self.coke.get() * 30)+
            (self.Red_bull.get() * 110)+
            (self.biscuits.get() * 20)
        )
        self.total_other.set("Rs. "+str(self.total_other_prices))
        self.tax_other.set("Rs. "+str(round(self.total_other_prices*0.05)))


#Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0',END)
        self.txt.insert(END,"     Welcome To Manish's Supermart  \n")
        self.txt.insert(END,f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END,f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END,f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END,"\n==========================")
        self.txt.insert(END,"\nProduct     Qty     Price")
        self.txt.insert(END,"\n==========================")

#Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0',END)

#Add Product name , qty and price to bill area
    def bill_area(self):
        self.welcome_soft()
        if self.bathing_soap.get() != 0:
            self.txt.insert(END,f"\nBath Soap     {self.bathing_soap.get()}     {self.bathing_soap.get() * 40}")
        if self.face_cream.get() != 0:
            self.txt.insert(END,f"\nFace Cream    {self.face_cream.get()}     {self.face_cream.get() * 140}")
        if self.face_wash.get() != 0:
            self.txt.insert(END,f"\nFace Wash     {self.face_wash.get()}     {self.face_wash.get() * 240}")
        if self.hair_spray.get() != 0:
            self.txt.insert(END,f"\nHair Spray    {self.hair_spray.get()}     {self.hair_spray.get() * 340}")
        if self.body_lotion.get() != 0 :
            self.txt.insert(END,f"\nBody Lotion   {self.body_lotion.get()}     {self.body_lotion.get() * 260}")
        if self.wheat.get() != 0:
            self.txt.insert(END,f"\nWheat         {self.wheat.get()}     {self.wheat.get() * 100}")
        if self.food_oil.get() != 0:
            self.txt.insert(END,f"\nFood Oil      {self.food_oil.get()}     {self.food_oil.get() * 180}")
        if self.Dal.get() != 0:
            self.txt.insert(END,f"\nDal           {self.Dal.get()}     {self.Dal.get() * 80}")
        if self.rice.get() != 0:
            self.txt.insert(END,f"\nRice          {self.rice.get()}     {self.rice.get() * 80}")
        if self.sugar.get() != 0:
            self.txt.insert(END,f"\nSugar         {self.sugar.get()}     {self.sugar.get() * 170}")
        if self.maaza.get() != 0:
            self.txt.insert(END,f"\nMaaza         {self.maaza.get()}     {self.maaza.get() * 20}")
        if self.Mountain_dew.get() != 0:
            self.txt.insert(END,f"\nMountain dew  {self.Mountain_dew.get()}     {self.Mountain_dew.get() * 50}")
        if self.coke.get() != 0:
            self.txt.insert(END,f"\nCoke          {self.coke.get()}     {self.coke.get() * 60}")
        if self.Red_bull.get() != 0:
            self.txt.insert(END,f"\nRed bull      {self.Red_bull.get()}     {self.Red_bull.get() * 20}")
        if self.biscuits.get() != 0:
            self.txt.insert(END,f"\nBiscuits      {self.biscuits.get()}     {self.biscuits.get() * 20}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,f"\n                      Total : {self.total_cosmetics_prices+self.total_grocery_prices+self.total_other_prices+self.total_cosmetics_prices * 0.05+self.total_grocery_prices * 0.05+self.total_other_prices * 0.05}")


    #Function to exit
    def exit(self):
        self.root.destroy()

    #Function To Clear All Fields


        


root = Tk()
object = Bill_App(root)
root.mainloop()
