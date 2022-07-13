# My coding skills got you climbing hills
from tkinter import *
import customtkinter
import os
import random
import pyperclip as pc
from tkinter import messagebox as mb
from bs4 import BeautifulSoup
import requests
customtkinter.set_appearance_mode("Light")
window=customtkinter.CTk()
# Making all the widgets for thte password saver
window.title("Password saver for me")
window.geometry("1800x500")
# Logic (The hard part)
#----------------------------------------------------
global logic
def main_func():
    def dollar_logic():
        for i in window.winfo_children():
            i.destroy()
        main_func()
        amount_entry=customtkinter.CTkEntry(window,placeholder_text="Amount"
        ,width=200,border=0
        ,placeholder_text_color="Silver"
        ,bg="#aeaeb0")
        amount_entry.place(x=74,y=152)
        from_currency_entry=customtkinter.CTkEntry(window,
        width=200
        ,placeholder_text="From",placeholder_text_color="Silver"
        ,border=0)
        from_currency_entry.place(x=370,y=152)
        to_currecny_entry=customtkinter.CTkEntry(window,placeholder_text="To",placeholder_text_color="Silver",
        width=200,border=0,
        bg="#aeaeb0")
        to_currecny_entry.place(x=665,y=152)
        def turn_upper_case():
                global new_dollar_label
                global currency_rate_label
                choose_currency_upper=from_currency_entry.get()
                to_currecny_entry_upper=to_currecny_entry.get()
                choose_currency_upper=choose_currency_upper.upper()
                to_currecny_entry_upper=to_currecny_entry_upper.upper()
                google ='https://www.xe.com/currencyconverter/convert/?Amount=1&From='+choose_currency_upper+'&To='+to_currecny_entry_upper
                source = requests.get(google).text
                soup = BeautifulSoup(source,'lxml')
                dollar = soup.find("p",class_="result__BigRate-sc-1bsijpp-1 iGrAod")
                dollar__to__float=dollar.text.split(" ")
                new__dollar=dollar__to__float[0]
                new__dollar = str(new__dollar)
                new__dollar = float(new__dollar)
                new__dollar=round(new__dollar,2)    
                currency_rate = "1 "+str(choose_currency_upper)+" = "+str(new__dollar)+" "+str(to_currecny_entry_upper)
                currency_rate_label=customtkinter.CTkLabel(window,text=currency_rate)
                currency_rate_label.place(x=500,y=230)
                #^^^^^^^^^^ New__dollar means the dollar's rate (not have to be the dollar's rate it could be also the euro rate it depends)
                amount=amount_entry.get()
                sum=new__dollar*float(amount)
                new_dollar_label=customtkinter.CTkLabel(window,text=str(sum)+' '+to_currecny_entry_upper)
                new_dollar_label.place(x=500,y=200)
        def delete():
            clear=customtkinter.CTkLabel(window,width=450,text="").place(x=500,y=200)
            clean=customtkinter.CTkLabel(window,width=2100,text="").place(x=500,y=230)
            dollar_logic()
        clear_button=customtkinter.CTkButton(window,text="clear",
        fg_color="red",hover_color="white",command=delete)
        clear_button.place(x=966,y=180)
        def swap():
            from_ = from_currency_entry.get()
            to = to_currecny_entry.get()

            for i in range(0,3):
                from_currency_entry.delete(i)
                to_currecny_entry.delete(i)
            to_currecny_entry.insert(0,from_)
            from_currency_entry.insert(0,to)
            to_currecny_entry.delete(3)
            from_currency_entry.delete(3)
            
        swap_button=customtkinter.CTkButton(window,text="Swap",fg_color="red",hover_color="white",width=10,
                                                            command=swap)
        swap_button.place(x=592,y=152)
        choose_currency_button=customtkinter.CTkButton(window,text="Send",fg_color="red",hover_color="white"
        ,command=turn_upper_case,border=0.3
        ,bg="#2b64fb",padx=10)
        choose_currency_button.place(x=960,y=150)
    def add():
        for i in window.winfo_children():
            i.destroy()
        password=customtkinter.CTkEntry(window,
                                    width=230
                                        ,border_width=0.5
                                            ,placeholder_text="Password"
                                                ,placeholder_text_color="Silver")
        user=customtkinter.CTkEntry(window,
                                        width=230,
                                            border_width=0.5
                                                ,placeholder_text="User"
                                                    ,placeholder_text_color="Silver")
        platform_=customtkinter.CTkEntry(window,
                                        width=490,
                                            border_width=0.5
                                                ,placeholder_text="Platform"
                                                    ,placeholder_text_color="Silver")
        password.place(x=450,y=35) #I wasn't able to calculate this by myself
        user.place(x=192,y=35)
        platform_.place(x=192,y=70)
        main_func()
        def logic():
            #for i in window.winfo_children():
               # i.destroy()
            
            #Opens the file and writes the user information inside it
            #Guardian
            if platform_.get() == "" or user.get() == "" or password.get() == "":
                mb.showerror("WRONG INPUT","Please Make sure to enter all the fields \nIf you don't have a username/password Enter \'None\'")
                return
            else:
                file = open("pass.txt","a")
                write_platform_=file.write("Platform: "+platform_.get()+" | ")
                write_email=file.write("Username/Email: "+user.get()+" | ")
                write_password=file.write("Password: "+password.get()+"\n")
                file.close()
                #Clear Fields
            
        def clear_field():
            for i in window.winfo_children():
                i.destroy()
            add()
        def generate_password():
            for i in range(12):
                a = random.choice("Q!w!E!r!T!y!U!i!O!p!A!s!D!fGhJkLzXcVbNm1234567890")
                password.insert(i,a)
            pc.copy(password.get())
        save=customtkinter.CTkButton(window,text="Save",
                                    command=logic
                                        ,fg_color='red',
                                                hover_color="white"
                                                        ,width=490).place(x=192,y=105)
        first_generate_button=customtkinter.CTkButton(window
                                                        ,width=490
                                                            ,text="Generate Random Password"
                                                                ,fg_color="red"
                                                                    ,hover_color="white"
                                                                        ,command=generate_password).place(x=192,y=105+35)
        clear_fields=customtkinter.CTkButton(window
                                                ,width=490
                                                    ,text="Clear Fields"
                                                        ,fg_color="Red"
                                                            ,hover_color="white"
                                                                ,command=clear_field).place(x=192,y=105+70)
    #--------------------------------------------------------------------------------

    def generate():
            for i in window.winfo_children():
                i.destroy()
            main_func()
            password_label2=customtkinter.CTkLabel(window,
                                                        text="New Password")
            password_label2.place(x=191,y=65)  
            rand_password=customtkinter.CTkEntry(window,
                                                    border_width=0.5)
            rand_password.place(x=192,y=150-65)
            for i in range(12):
                a = random.choice("QwErTyUiOpAsDfGhJkLzXcVbNm1234567890")
                rand_password.insert(i,a)
                pc.copy(rand_password.get())

    #---------------------------------------------------------------

    #----------------------------------------------------------------
    def saved():

        file1 = open("pass.txt","r")
        new_window=customtkinter.CTk()
        saved_passwords=customtkinter.CTkLabel(new_window,text=file1.read())
        saved_passwords.pack()
        new_window.mainloop()
        return
    #----------------------------------------------------------------------
    #Not finished Need to add encryption
    def add_passport():

        for i in window.winfo_children():
            i.destroy()
        name=customtkinter.CTkEntry(window
                                    ,placeholder_text="Enter Surname"
                                        ,placeholder_text_color="Silver")
        passport_no=customtkinter.CTkEntry(window
                                        ,placeholder_text="Enter Given name",
                                            placeholder_text_color="Silver")
        nation=customtkinter.CTkEntry(window
                                    ,placeholder_text="Nationality"
                                        ,placeholder_text_color="Silver")
        date_of_birth=customtkinter.CTkEntry(window
                                            ,placeholder_text="Date of birth"
                                                ,placeholder_text_color="Silver")
        date_of_issue=customtkinter.CTkEntry(window
                                            ,placeholder_text="Date of issue"
                                                ,placeholder_text_color="Silver")
        authority=customtkinter.CTkEntry(window
                                        ,placeholder_text="Authority"
                                                ,placeholder_text_color="Silver")
                #Clear Fields
        save=customtkinter.CTkButton(window,text="Save",
                                    command=logic
                                        ,fg_color='red',
                                                hover_color="white"
                                                        ,width=490).place(x=192,y=105)
        name.place(x=200,y=35)
        passport_no.place(x=370,y=35)
        nation.place(x=540,y=35)
        date_of_birth.place(x=200,y=70)
        date_of_issue.place(x=370,y=70)
        authority.place(x=540,y=70)
        # The space between x + 170 and y supposed to be + 35
        main_func()
        # platform_: Iphone | Username/Email: Nitay | Password: pro
    #All the Buttons
    #Saved button
    saved=customtkinter.CTkButton(window,command=saved
                                ,fg_color="red"
                                    ,hover_color="white"
                                        ,text="Saved Passwords").place(x=1,y=0)
    # Generate password button
    #------------------------------------------------------------------------
    generate_button=customtkinter.CTkButton(window,text="Generate Password",
                                            command=generate,height=28,
                                                fg_color="red",
                                                    hover_color="white").place(x=1,y=35)
    #------------------------------------------------------------------------
    #Save button
    #-------------------------------------------------
    add_password=customtkinter.CTkButton(window
                                        ,text="Add Password"
                                            ,fg_color="red"
                                                ,hover_color="white"
                                                    ,command=add).place(x=1,y=70)
    #-------------------------------------------------
    #Currency Converter button
    convert=customtkinter.CTkButton(window
    ,text="Convert Currency"
    ,fg_color="red"
    ,hover_color="white"
    ,command=dollar_logic).place(x=1,y=105)
    #Main Loop
main_func()
window.mainloop()
