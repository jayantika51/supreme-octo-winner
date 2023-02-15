from tkinter import*
root=Tk()
root.title("dictionary")
root.geometry("400x400")

label_of_zebu = Label(root)
label_of_tearaway = Label(root)
label_of_abashed = Label(root)


dictionary = {"zebu":"a breed of domesticated ox with a humped back",
              "tearaway":"a person who behaves in a wild or reckless way",
              "abashed":"embarassed or ashamed"}


def zebu():
    label_of_zebu["text"] = dictionary['zebu']
    
    
def tearaway():
    label_of_tearaway["text"] = dictionary['tearaway']
    

def abashed():
    label_of_abashed["text"] = dictionary['abashed']
    
    
    button_zebu= Button(root , text = "Meaning of Zebu", command = zebu)
    button_zebu.place(relx = 0.5, rely = 0.2, anchor = CENTER)
    
    label_of_zebu.place(relx = 0.5, rely = 0.3, anchor = CENTER)
    
    
     
    button_tearaway= Button(root , text = "Meaning of Tearaway", command = zebu)
    button_tearaway.place(relx = 0.5, rely = 0.4, anchor = CENTER)
    
    label_of_tearaway.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    
    
     
    button_abashed= Button(root , text = "Meaning of Abashed", command = zebu)
    button_abashed.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    
    label_of_abashed.place(relx = 0.5, rely = 0.7, anchor = CENTER)
    
    
    root.mainloop()