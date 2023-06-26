import tkinter as tk
from tkinter import filedialog

#setup
win=tk.Tk()
win.resizable(0,0)
win.geometry("1000x500") #change the side frame and the main frame sizes if this is changed
win.title("Cryptographic Software")

#constants
sideframe_bgc = 'white'
mainframe_bgc = '#EDEFEF'
button_bg = '#0F9FE2'
button_fg = 'black'
button_bg_e = '#74D3FF' #on enter - gets brighter to indicate mouse position
button_fg_e = 'gray' #on enter

#mode track

EncText = False
EncFile = False
DecText = False
DecFile = False

#encryption info
characters = ['$', '&', 'h', 'J', 'M', 'u', '(', '#', 'L', 'I', 'R', '0', 'z', 'y', 'o', '^', '!', 'N', 'n', 'H', 'P', '4', '*', '=', 's', '~', ')', 'B', '7', 'G', '%', 'E', 'Y', 'c', 'd', 'F', '1', 'p', '"', 'A', 'O', '[', '2', 'V', '{', 'f', 'k', '@', 'j', 't', 'b', '8', '}', 'r', '_', 'K', 'v', '-', 'm', '/', 'D', "',|", '5', 'i', '3', 'C', ';', 'S', '6', ',', 'a', '9', 'x', 'T', 'W', 'Q', 'q', 'U', ':', 'e', 'l', 'X', '<', '>', '?', '+', 'Z', '.', ']', 'w', 'g']
key1 = 71
key2 = 97

et = None
dt = None
ef = None
df = None

def clearWidgets(mainframe):
    for widget in mainframe.winfo_children():
        widget.destroy()


def change_view(m): #this should be the only function that changes the 4 primary boolean values
    global EncText, EncFile, DecText, DecFile
    
    initialLabel.destroy()
    
    if m == 'Encrypt Text' and EncText == False:
        EncFile = False
        DecText = False
        DecFile = False
        
        clearWidgets(mainframe)
        EncText = True
        et = encryptText()
        et.start()
        
    elif m == 'Encrypt File' and EncFile == False:
        EncText = False
        DecText = False
        DecFile = False
        
        clearWidgets(mainframe)
        EncFile = True
        ef = encryptFile()
        ef.start()
        
        
    elif m == 'Decrypt Text' and DecText == False:
        #clear the main frame and start to add onto the decrypt text, lots of resuable code
        EncText = False
        EncFile = False
        DecFile = False
        
        clearWidgets(mainframe)
        DecText = True
        dt = decryptText()
        dt.start()
        
    elif m == 'Decrypt File' and DecFile == False:
        EncText = False
        EncFile = False
        DecText = False
        
        clearWidgets(mainframe)
        DecFile = True
        df = decryptFile()
        df.start()
    

#handling the hover over button feature
def on_enter1(event):
    button1.config(bg=button_bg_e, fg=button_fg_e)
def on_leave1(event):
    button1.config(bg=button_bg, fg=button_fg)
def on_enter2(event):
    button2.config(bg=button_bg_e, fg=button_fg_e)
def on_leave2(event):
    button2.config(bg=button_bg, fg=button_fg)
def on_enter3(event):
    button3.config(bg=button_bg_e, fg=button_fg_e)
def on_leave3(event):
    button3.config(bg=button_bg, fg=button_fg)
    
def on_enter4(event):
    button4.config(bg=button_bg_e, fg=button_fg_e)
def on_leave4(event):
    button4.config(bg=button_bg, fg=button_fg)

def on_enter5(event):
    quitButton.config(bg="#FF9999", fg=button_fg_e)
def on_leave5(event):
    quitButton.config(bg="#FF0000", fg=button_fg)

def closeAPP():
    win.destroy()

#side frame setup
sideframe=tk.Frame(win, bg=sideframe_bgc, width=250, relief=tk.FLAT, highlightthickness=2, highlightbackground="black")
sideframe.pack(side=tk.LEFT, fill=tk.Y)

#sideframe widgets
logo = tk.Label(sideframe, bg=sideframe_bgc, text="Encrypt/Decrypt Tool", font=("Arial", 20))
logo.pack(side=tk.TOP, pady=30)

modes = ['Encrypt Text', 'Encrypt File', 'Decrypt Text', 'Decrypt File']
eT = modes[0]
eF = modes[1]
dT = modes[2]
dF = modes[3]

button1 = tk.Button(sideframe, text=eT, font=("Arial", 14), bg=button_bg, fg=button_fg, cursor="", width=15, pady=10, command=lambda m=eT: change_view(m))
button1.pack(pady=15)

button2 = tk.Button(sideframe, text=eF, font=("Arial", 14), bg=button_bg, fg=button_fg, cursor="", width=15, pady=10, command=lambda m=eF: change_view(m))
button2.pack(pady=15)

button3 = tk.Button(sideframe, text=dT, font=("Arial", 14), bg=button_bg, fg=button_fg, cursor="", width=15, pady=10, command=lambda m=dT: change_view(m))
button3.pack(pady=15)

button4 = tk.Button(sideframe, text=dF, font=("Arial", 14), bg=button_bg, fg=button_fg, cursor="", width=15, pady=10, command=lambda m=dF: change_view(m))
button4.pack(pady=15)

quitButton = tk.Button(sideframe, text="Quit", font=("Arial", 14), bg="#FF0000", fg=button_fg, cursor="", width=15, pady=10, command=closeAPP)
quitButton.pack(side=tk.BOTTOM, pady=15)

button1.bind("<Enter>", on_enter1)
button1.bind("<Leave>", on_leave1)
button2.bind("<Enter>", on_enter2)
button2.bind("<Leave>", on_leave2)
button3.bind("<Enter>", on_enter3)
button3.bind("<Leave>", on_leave3)
button4.bind("<Enter>", on_enter4)
button4.bind("<Leave>", on_leave4)

quitButton.bind("<Enter>", on_enter5)
quitButton.bind("<Leave>", on_leave5)

#main frame setup
mainframe = tk.Frame(win, bg=mainframe_bgc, width=550, relief=tk.FLAT, highlightthickness=1, highlightbackground="black")
mainframe.pack(expand=True, fill=tk.BOTH, side='right')

#mainframe widgets
initialLabel = tk.Label(mainframe, bg="white", text="Choose an option.", font=("Arial", 18))
initialLabel.pack(expand=True, anchor='center', pady = 10)

def Encrypter(inp, shift): #is the caesar cipher
        
    encoded_input = ''
    for i in inp:
        if i == ' ':
            new_letter = ' '
            
        elif i in characters:
                location = characters.index(i)
                if location + shift > len(characters)-1: #cant index the normal length thus -1
                    new_shift = (location+shift) - len(characters)
                    new_letter = characters[new_shift]
                else:
                    new_letter = characters[location+shift]
                
        else:
            new_letter = i
                
        encoded_input += new_letter

    return encoded_input

def Decrypter(inp, shift): #decodes the caesar cipher
    new_output = ''
    new_letter = ''
    for i in inp:
        if i == ' ':
            new_letter = ' '
        
        elif i in characters:
            location = characters.index(i)
            new_letter = characters[location-shift]
        else:
            new_letter = i
            
        new_output += new_letter
    
    return new_output


class encryptText:
    def __init__(self):
        
        self.initFrame()
        
        self.text_Enc = tk.Text(self.encTextFrame, bg='white', width=100, height=10, font=("Arial", 16), relief=tk.FLAT, highlightthickness=1, highlightbackground="black")
        
        
        self.prompt_text = "Click here to enter text to be encrypted!"
        self.text_Enc.insert("1.0", self.prompt_text)
        self.text_Enc.configure(state="disabled")
        self.text_Enc.configure(foreground='lightgrey')
        
        # Bind the click event to the text area
        self.text_Enc.bind("<Button-1>", self.on_click_EncText)
        
        #hidden textbox
        self.encodedLabel = tk.Text(self.encTextFrame, bg=mainframe_bgc, width=100, height=6, font=("Arial", 18), cursor="arrow", relief=tk.FLAT, highlightthickness=1, highlightbackground=mainframe_bgc)
        
        self.encodedLabel.configure(state="disabled")
        
        
        self.submit_text = tk.Button(self.encTextFrame, text='Submit Text', font=('Arial',14), bg=button_bg, fg=button_fg, width=15, height=2, command=self.encTextController)
        
        self.submit_text.bind("<Enter>", self.on_enterEncText)
        self.submit_text.bind("<Leave>", self.on_leaveEncText)
        
        self.clear_text = tk.Button(self.encTextFrame, text='Clear Input Box', font=('Arial',14), bg=button_bg, fg=button_fg, width=15, height=2, command=self.clearTextCommand)
        self.clear_text.bind("<Enter>", self.on_enterEncTextClear)
        self.clear_text.bind("<Leave>", self.on_leaveEncTextClear)
        
       
        
    def start(self):
        win.title("Encrypt Text")
        
        self.encTextFrame.pack(expand=True, fill=tk.BOTH)
        self.text_Enc.pack(side=tk.TOP, padx=20, pady=20)
        self.encodedLabel.pack(side=tk.BOTTOM, padx=20, pady=20)
        self.submit_text.pack(side=tk.RIGHT, padx=20) #no pady because text_Enc has it
        self.clear_text.pack(side=tk.LEFT, padx=20) #no pady because text_Enc has it

    
    def initFrame(self):
        #destroy mainframe, create the new frame and then pack it
        self.encTextFrame = mainframe
        
        
    def destroyFrame(self):
        self.encTextFrame.destroy()
    
    def on_click_EncText(self, event):
        if self.text_Enc["state"] == "normal":
            return
        self.text_Enc.configure(state="normal")
        self.text_Enc.delete("1.0", "end")
        self.text_Enc.configure(foreground='black')
        
    def on_enterEncText(self, event):
        self.submit_text.config(bg=button_bg_e, fg=button_fg_e)
    def on_leaveEncText(self, event):
        self.submit_text.config(bg=button_bg, fg=button_fg)
        
    def on_enterEncTextClear(self, event):
        self.clear_text.config(bg=button_bg_e, fg=button_fg_e)
    def on_leaveEncTextClear(self, event):
        self.clear_text.config(bg=button_bg, fg=button_fg)
    
    def clearTextCommand(self):
        self.text_Enc.delete("1.0", "end")
    
    def encTextController(self):
        #encodedLabel.destroy()
        text = self.text_Enc.get("1.0", "end")
        shift1 = (len(text)-1)*key1 % len(characters)
        shift2 = (len(text)-1)*key2 % len(characters)
        if shift1+shift2 == 91:
            shift2 += 1 #to prevent a loop encoding problem. 
        encoded_text = Encrypter(Encrypter(text, shift1), shift2)
        self.showEncodedOutput(encoded_text)
        

    def showEncodedOutput(self, etext):
        #encodedLabel = Text(mainframe, bg='white', width=100, height=6, font=("Arial", 18), relief=FLAT, highlightthickness=1, highlightbackground="black")
        #encodedLabel.pack(side=BOTTOM, padx=20, pady=20)
        self.encodedLabel.configure(state="normal")
        self.encodedLabel.delete("1.0", "end")
        self.encodedLabel.insert("1.0", etext)
        self.encodedLabel.configure(state="disabled")
        self.encodedLabel.configure(bg='white')
        self.encodedLabel.configure(highlightbackground='black')
        self.encodedLabel.configure(cursor="ibeam")
        self.encodedLabel.bind("<1>", lambda event: self.encodedLabel.focus_set())
    

class decryptText:
    def __init__(self):

        self.initFrame()
        
        self.text_Dec = tk.Text(self.decTextFrame, bg='white', width=100, height=10, font=("Arial", 16), relief=tk.FLAT, highlightthickness=1, highlightbackground="black")
        
        
        self.prompt_text = "Click here to enter text to be decrypted!"
        self.text_Dec.insert("1.0", self.prompt_text)
        self.text_Dec.configure(state="disabled")
        self.text_Dec.configure(foreground='lightgrey')
        
        # Bind the click event to the text area
        self.text_Dec.bind("<Button-1>", self.on_click_EncText)
        
        #hidden textbox
        self.decodedLabel = tk.Text(self.decTextFrame, bg=mainframe_bgc, width=100, height=6, font=("Arial", 18), cursor="arrow", relief=tk.FLAT, highlightthickness=1, highlightbackground=mainframe_bgc)
        
        self.decodedLabel.configure(state="disabled")
        
        
        self.submit_text = tk.Button(self.decTextFrame, text='Submit Text', font=('Arial',14), bg=button_bg, fg=button_fg, width=15, height=2, command=self.encTextController)
        
        self.submit_text.bind("<Enter>", self.on_enterEncText)
        self.submit_text.bind("<Leave>", self.on_leaveEncText)
        
        self.clear_text = tk.Button(self.decTextFrame, text='Clear Input Box', font=('Arial',14), bg=button_bg, fg=button_fg, width=15, height=2, command=self.clearTextCommand)
        self.clear_text.bind("<Enter>", self.on_enterEncTextClear)
        self.clear_text.bind("<Leave>", self.on_leaveEncTextClear)

    def start(self):
        win.title("Decrypt Text")
       
        self.decTextFrame.pack(expand=True, fill=tk.BOTH)
        self.text_Dec.pack(side=tk.TOP, padx=20, pady=20)
        self.decodedLabel.pack(side=tk.BOTTOM, padx=20, pady=20)
        self.submit_text.pack(side=tk.RIGHT, padx=20) #no pady because text_Enc has it
        self.clear_text.pack(side=tk.LEFT, padx=20) #no pady because text_Enc has it

    
    def initFrame(self):
        #destroy mainframe, create the new frame and then pack it
        self.decTextFrame = mainframe
        
    def destroyFrame(self):
        self.decTextFrame.destroy()
    
    def on_click_EncText(self, event):
        if self.text_Dec["state"] == "normal":
            return
        self.text_Dec.configure(state="normal")
        self.text_Dec.delete("1.0", "end")
        self.text_Dec.configure(foreground='black')
        
    def on_enterEncText(self, event):
        self.submit_text.config(bg=button_bg_e, fg=button_fg_e)
    def on_leaveEncText(self, event):
        self.submit_text.config(bg=button_bg, fg=button_fg)
        
    def on_enterEncTextClear(self, event):
        self.clear_text.config(bg=button_bg_e, fg=button_fg_e)
    def on_leaveEncTextClear(self, event):
        self.clear_text.config(bg=button_bg, fg=button_fg)
    
    def clearTextCommand(self):
        self.text_Dec.delete("1.0", "end")
    
    def encTextController(self):
        #encodedLabel.destroy()
        text = self.text_Dec.get("1.0", "end")
        shift1 = (len(text)-1)*key1 % len(characters)
        shift2 = (len(text)-1)*key2 % len(characters)
        if shift1+shift2 == 91:
            shift2 += 1 #to prevent a loop encoding problem. 
        encoded_text = Decrypter(Decrypter(text, shift2), shift1)
        self.showDecodedOutput(encoded_text)
        

    def showDecodedOutput(self, etext):
        self.decodedLabel.configure(state="normal")
        self.decodedLabel.delete("1.0", "end")
        self.decodedLabel.insert("1.0", etext)
        self.decodedLabel.configure(state="disabled")
        self.decodedLabel.configure(bg='white')
        self.decodedLabel.configure(highlightbackground='black')
        self.decodedLabel.configure(cursor="ibeam")
        self.decodedLabel.bind("<1>", lambda event: self.decodedLabel.focus_set())


def txtFileController(file_path, new_path, EorD):
    label = ''
    code
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            
            shift1 = (len(content)-1)*key1 % len(characters)
            shift2 = (len(content)-1)*key2 % len(characters)
            if shift1+shift2 == 91:
                shift2 += 1 #to prevent a loop encoding problem.
            
            if EorD == 'E': #means encryption
                text = Encrypter(Encrypter(content, shift1), shift2)
                code = 'encrypted'
            else: #decrypt
                text = Decrypter(Decrypter(content, shift2), shift1)
                code = 'decrypted'
            
        with open(new_path, 'w') as file:
            file.write(text)
        
        label= f"File Created Successfully. Your data is {code}"
    except:
        label = "Processing Error, please check input file type and/or try again."
    return label
    

class encryptFile:
    def __init__(self):
        self.savebuttoncreated = False
        self.label=''
        self.finished=False
        
        self.frame = mainframe
        
        win.title("Encrypt File")
        
        self.filePath = ''
        self.savePath = ''
        
        self.chooseFileButton = tk.Button(self.frame, text='Choose .txt File', font=('Arial',14), bg=button_bg, fg=button_fg, width=15, height=2, command=self.chooseFile)
        
        
        self.chooseFileButton.bind("<Enter>", self.on_enterFile)
        self.chooseFileButton.bind("<Leave>", self.on_leaveFile)
        
        self.fileDirectory = tk.Text(self.frame, bg=mainframe_bgc, width=100, height=1, cursor='arrow', font=("Arial", 18), relief=tk.FLAT, highlightthickness=1, highlightbackground=mainframe_bgc)
        self.fileDirectory.configure(state='disabled')

        

        self.saveDirectory = tk.Text(self.frame, bg=mainframe_bgc, width=100, height=1, cursor='arrow', font=("Arial", 18), relief=tk.FLAT, highlightthickness=1, highlightbackground=mainframe_bgc)
        self.saveDirectory.configure(state='disabled')
        
        
        #add a text entry that contains the file path
        #add a text entry to contain the file name it will save
    def start(self):
        self.chooseFileButton.pack(anchor='nw', padx=20, pady=20)
        self.fileDirectory.pack(anchor='nw', padx=20)
    
    def createSaveButton(self):
        if self.savebuttoncreated == False:
            
            self.saveAsButton = tk.Button(self.frame, text='Save encrypted file (.txt)', font=('Arial',14), bg=button_bg, fg=button_fg, width=19, height=2, command=self.saveNewFile)
            self.saveAsButton.pack(anchor='nw', padx=20, pady=20)
            
            self.saveDirectory.pack(anchor='nw', padx=20)
            
            self.saveAsButton.bind("<Enter>", self.on_enterSave)
            self.saveAsButton.bind("<Leave>", self.on_leaveSave)
            
            self.savebuttoncreated = True
        
    def on_enterSave(self, event):
        self.saveAsButton.config(bg=button_bg_e, fg=button_fg_e)
    def on_leaveSave(self, event):
        self.saveAsButton.config(bg=button_bg, fg=button_fg)   
        
    def on_enterFile(self, event):
        self.chooseFileButton.config(bg=button_bg_e, fg=button_fg_e)
    def on_leaveFile(self, event):
        self.chooseFileButton.config(bg=button_bg, fg=button_fg)
    
    
    def chooseFile(self):
        file_path = filedialog.askopenfilename()
        self.filePath = file_path
        self.showDirectory()
        #self.submit_text.destroy
    
    def saveNewFile(self):
        save_path = filedialog.asksaveasfilename(defaultextension='.txt')
        self.savePath = save_path
        self.showNewFile()
        self.label = txtFileController(self.filePath, self.savePath, 'E')
        if self.finished == False:
            self.showLabel = tk.Label(self.frame, text=self.label, font=("Arial", 18))
            self.showLabel.pack(padx=20, pady=40)
            self.finished = True
        else:
            self.showLabel.configure(text=self.label)
        
        #make new label and pack it
     
    def showNewFile(self):
        self.saveDirectory.configure(state='normal')
        self.saveDirectory.delete("1.0", "end")
        self.saveDirectory.insert("1.0", self.savePath)
        self.saveDirectory.configure(bg='white')
        self.saveDirectory.configure(highlightbackground='black')
        self.saveDirectory.configure(cursor="ibeam")
        self.saveDirectory.configure(state='disabled')
        self.saveDirectory.bind("<1>", lambda event: self.fileDirectory.focus_set()) 
        
    def showDirectory(self):
        self.fileDirectory.configure(state='normal')
        self.fileDirectory.delete("1.0", "end")
        self.fileDirectory.insert("1.0", self.filePath)
        self.fileDirectory.configure(bg='white')
        self.fileDirectory.configure(highlightbackground='black')
        self.fileDirectory.configure(cursor="ibeam")
        self.fileDirectory.configure(state='disabled')
        self.fileDirectory.bind("<1>", lambda event: self.fileDirectory.focus_set())
        
        #show the save button
        self.createSaveButton()
        
class decryptFile:
    def __init__(self):
        self.savebuttoncreated = False
        self.label=''
        self.finished=False
        
        self.frame = mainframe
        
        win.title("Decrypt File")
        
        self.filePath = ''
        self.savePath = ''
        
        self.chooseFileButton = tk.Button(self.frame, text='Choose .txt File', font=('Arial',14), bg=button_bg, fg=button_fg, width=15, height=2, command=self.chooseFile)
        
        
        self.chooseFileButton.bind("<Enter>", self.on_enterFile)
        self.chooseFileButton.bind("<Leave>", self.on_leaveFile)
        
        self.fileDirectory = tk.Text(self.frame, bg=mainframe_bgc, width=100, height=1, cursor='arrow', font=("Arial", 18), relief=tk.FLAT, highlightthickness=1, highlightbackground=mainframe_bgc)
        self.fileDirectory.configure(state='disabled')

        

        self.saveDirectory = tk.Text(self.frame, bg=mainframe_bgc, width=100, height=1, cursor='arrow', font=("Arial", 18), relief=tk.FLAT, highlightthickness=1, highlightbackground=mainframe_bgc)
        self.saveDirectory.configure(state='disabled')
        
        
        #add a text entry that contains the file path
        #add a text entry to contain the file name it will save
    def start(self):
        self.chooseFileButton.pack(anchor='nw', padx=20, pady=20)
        self.fileDirectory.pack(anchor='nw', padx=20)
    
    def createSaveButton(self):
        if self.savebuttoncreated == False:
            
            self.saveAsButton = tk.Button(self.frame, text='Save encrypted file (.txt)', font=('Arial',14), bg=button_bg, fg=button_fg, width=19, height=2, command=self.saveNewFile)
            self.saveAsButton.pack(anchor='nw', padx=20, pady=20)
            
            self.saveDirectory.pack(anchor='nw', padx=20)
            
            self.saveAsButton.bind("<Enter>", self.on_enterSave)
            self.saveAsButton.bind("<Leave>", self.on_leaveSave)
            
            self.savebuttoncreated = True
        
    def on_enterSave(self, event):
        self.saveAsButton.config(bg=button_bg_e, fg=button_fg_e)
    def on_leaveSave(self, event):
        self.saveAsButton.config(bg=button_bg, fg=button_fg)   
        
    def on_enterFile(self, event):
        self.chooseFileButton.config(bg=button_bg_e, fg=button_fg_e)
    def on_leaveFile(self, event):
        self.chooseFileButton.config(bg=button_bg, fg=button_fg)
    
    
    def chooseFile(self):
        file_path = filedialog.askopenfilename()
        self.filePath = file_path
        self.showDirectory()
        #self.submit_text.destroy
    
    def saveNewFile(self):
        save_path = filedialog.asksaveasfilename(defaultextension='.txt')
        self.savePath = save_path
        self.showNewFile()
        self.label = txtFileController(self.filePath, self.savePath, 'D')
        if self.finished == False:
            self.showLabel = tk.Label(self.frame, text=self.label, font=("Arial", 18))
            self.showLabel.pack(padx=20, pady=40)
            self.finished = True
        else:
            self.showLabel.configure(text=self.label)
        
        #make new label and pack it
     
    def showNewFile(self):
        self.saveDirectory.configure(state='normal')
        self.saveDirectory.delete("1.0", "end")
        self.saveDirectory.insert("1.0", self.savePath)
        self.saveDirectory.configure(bg='white')
        self.saveDirectory.configure(highlightbackground='black')
        self.saveDirectory.configure(cursor="ibeam")
        self.saveDirectory.configure(state='disabled')
        self.saveDirectory.bind("<1>", lambda event: self.fileDirectory.focus_set()) 
        
    def showDirectory(self):
        self.fileDirectory.configure(state='normal')
        self.fileDirectory.delete("1.0", "end")
        self.fileDirectory.insert("1.0", self.filePath)
        self.fileDirectory.configure(bg='white')
        self.fileDirectory.configure(highlightbackground='black')
        self.fileDirectory.configure(cursor="ibeam")
        self.fileDirectory.configure(state='disabled')
        self.fileDirectory.bind("<1>", lambda event: self.fileDirectory.focus_set())
        
        #show the save button
        self.createSaveButton()
        
    
        
    


win.mainloop()



