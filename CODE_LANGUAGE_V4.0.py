from tkinter import *


def code_app():

    
    def more():
        more = Tk()
        more.configure(bg='powder blue')
        more.iconbitmap(r'code.ico')
        more.geometry('400x200+300+450')

        Label(more, text='Code Language',bg='powder blue',font=('Arial Black',10,'bold')).pack()

        Label(more, text='By: Hardeep Singh',bg='powder blue',font=('Arial Black',10,'bold')).pack()

        Label(more, text='This code language was created by Hardeep Singh\n  in his junior classes to  communicate with his\n classmates in the class. this is a software version\n of that language.',bg='powder blue',font=('Arial Black',10,'bold')).pack()

        Label(more, text='Contact us at:\n9803588671',bg='powder blue',font=('Arial Black',10,'bold')).pack(side=LEFT)

    def copy():
        entry.clipboard_clear()
        entry.clipboard_append(output)

    def paste():
        deentry.delete(1.0,END)
        deentry.insert(INSERT, entry.clipboard_get())



        

    def decode_func():
        splitted_list = deentry.get(1.0,END).split(',' )
        splitted_list[-1] = splitted_list[-1].split('\n')[0]

        d = []
        for code in splitted_list:
            if code == "2":
              d.append("A")
            elif code == "22":
              d.append("B")
            elif code == "222":
             d.append ("C")
            elif code == "3":
             d.append ("D")
            elif code == "33":
             d.append ("E")    
            elif code == "333":
              d.append("F")    
            elif code == "4":
              d.append("G")     
            elif code == "44":
               d.append("H")    
            elif code == "444":
              d.append("I")     
            elif code == "5":
              d.append("J")     
            elif code == "55":
              d.append("K")    
            elif code == "555":
              d.append("L")      
            elif code == "6":
              d.append("M")
            elif code == "66":
              d.append("N")      
            elif code == "666":
              d.append("O")    
            elif code == "7":
               d.append("P")      
            elif code == "77":
             d.append ("Q")      
            elif code == "777":
              d.append("R")      
            elif code == "7777":
              d.append("S")     
            elif code == "8":
              d.append("T")      
            elif code == "88":
              d.append("U")      
            elif code == "888":
              d.append("V")      
            elif code == "9":
              d.append("W")      
            elif code == "99":
               d.append("X")           
            elif code == "999":
              d.append("Y")
            elif code == "9999":
              d.append("Z")
            elif code == "0":
               d.append(" ")
        ans = ''.join(d)

        deoutput_label.configure(text = ans,font=('Arial Black',10,'bold'))




        



    def code_func():

        value = entry.get(1.0,END)
        list_code = []
        for i in value:
            list_code.append(i.upper())
            

        d = []
        for code in list_code:
            if code == "A":
              d.append("2")
            elif code == "B":
              d.append("22")
            elif code == "C":
             d.append ("222")
            elif code == "D":
             d.append ("3")
            elif code == "E":
             d.append ("33")    
            elif code == "F":
              d.append("333")    
            elif code == "G":
              d.append("4")     
            elif code == "H":
               d.append("44")    
            elif code == "I":
              d.append("444")     
            elif code == "J":
              d.append("5")     
            elif code == "K":
              d.append("55")    
            elif code == "L":
              d.append("555")      
            elif code == "M":
              d.append("6")
            elif code == "N":
              d.append("66")      
            elif code == "O":
              d.append("666")    
            elif code == "P":
               d.append("7")      
            elif code == "Q":
             d.append ("77")      
            elif code == "R":
              d.append("777")      
            elif code == "S":
              d.append("7777")     
            elif code == "T":
              d.append("8")      
            elif code == "U":
              d.append("88")      
            elif code == "V":
              d.append("888")      
            elif code == "W":
              d.append("9")      
            elif code == "X":
               d.append("99")           
            elif code == "Y":
              d.append("999")
            elif code == "Z":
              d.append("9999")
            elif code == " ":
               d.append("0")

        global output
        output = ','.join(d)

          #configure output
        output_label.configure(text=str(output),font=('Arial Black',10,'bold'))

        


    def code():
        code_win = Tk()
        code_win.geometry('300x320+5+100')
        code_win.iconbitmap(r'code.ico')
        code_win.resizable(0,0)
        code_win.title('Code')

        code_label = Label(code_win, text='Code',width=60,height=2, bg='powder blue', font=('Arial Black',15,'bold'))
        code_label.pack()

        Label(code_win, text='').pack()
        
        intro_label = Label(code_win,height=1, text='Enter the Text below to Code', font=('Arial Black',10,'bold'))
        intro_label.pack()


        Label(code_win, text='').pack()

        global entry
        entry = Text(code_win,bd=5,height=1,font=('Arial Black',10,'bold'))
        entry.pack()

        Label(code_win, text='').pack()

        submit_button = Button(code_win, bd=5, text='Convert To Code', font=('Arial Black',10,'bold'), bg='powder blue', command=code_func)
        submit_button.pack()

        Label(code_win, text='').pack()

        global output_label
        output_label = Label(code_win, text='')
        output_label.pack()
        
        Label(code_win, text='').pack()

        copy_button = Button(code_win, bd=5, text='Copy Code', font=('Arial Black',10,'bold'), bg='powder blue', command=copy)
        copy_button.pack()

        
        

        

        
        
        code_win.mainloop()










    def decode():
        decode_win = Tk()
        decode_win.geometry('300x320+595+100')
        decode_win.iconbitmap(r'code.ico')
        decode_win.resizable(0,0)
        decode_win.title('Decode')

        decode_label = Label(decode_win, text='Decode',width=60,height=2, bg='powder blue', font=('Arial Black',15,'bold'))
        decode_label.pack()

        Label(decode_win, text='').pack()
        
        intro_label = Label(decode_win,height=1, text='Enter The Code Below To Decode', font=('Arial Black',10,'bold'))
        intro_label.pack()
        

        Label(decode_win, text='').pack()

        global deentry
        deentry = Text(decode_win,bd=5,height=1,font=('Arial Black',10,'bold'))
        deentry.pack()



        Label(decode_win, text='').pack()

        submit_button = Button(decode_win, bd=5, text='Convert To Text', font=('Arial Black',10,'bold'), bg='powder blue', command=decode_func)
        submit_button.pack()

        Label(decode_win, text='').pack()

        global deoutput_label
        deoutput_label = Label(decode_win, text='')
        deoutput_label.pack()
        
        Label(decode_win, text='').pack()

        paste_button = Button(decode_win, bd=5, text='Paste Code', font=('Arial Black',10,'bold'), bg='powder blue', command=paste)
        paste_button.pack()

        
        

        

        
        
        decode_win.mainloop()











    root = Tk()
    root.geometry('300x300+300+100')
    root.iconbitmap(r'code.ico')
    root.title('CODE LANGUAGE V2.0')
    root.resizable(0,0)



    label_1 = Label(root, text='Code Language',width=60,height=3, bg='powder blue', font=('Arial Black',15,'bold'))
    label_1.pack()

    Label(root, text='').pack()




    code_button = Button(root, text='Code',bd=5, width=20, height=2, bg='powder blue', font=('Arial Black',11,'bold'), command = code)
    code_button.pack()



    decode_button = Button(root, text='Decode',bd=5, width=20, height=2, bg='powder blue', font=('Arial Black',11,'bold'), command = decode)
    decode_button.pack()




    Label(root, text='').pack()

    more = Button(root, text='About us',bg='powder blue',bd=5, font=('Arial Black',9,'bold'), command=more)
    more.pack(side=RIGHT)



    root.mainloop()





code_app()























    
        


    
    


  
          

    
            




        

            
        


