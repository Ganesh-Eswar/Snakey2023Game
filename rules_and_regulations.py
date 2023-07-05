from tkinter import font as font 
from tkinter import * 
from PIL import Image,ImageTk
import snakey2023 as snk

class RulesAndRegulations():
    def __init__(self,parent,controller) -> None:
        self.root = parent 
        self.control = controller 
        self.swidth = self.control.application_width
        self.sheight = self.control.application_height
        self.canvas2 = Canvas(self.root,width=self.swidth,
                             height=self.sheight,
                             highlightthickness=0,cursor="spider",
                             background="red")
        self.canvas2.grid(row=0,column=0) 
        rules_bg = Image.open(self.control.path_to_rulesbg)
        rules_bg = rules_bg.resize((self.control.application_width,self.control.application_height))
        self.rule_image = ImageTk.PhotoImage(rules_bg)
        self.canvas2.create_image(0,0,anchor=NW,image=self.rule_image)     
        self.adding_buttons()
    
    def adding_buttons(self):
        self.ready_button_font = font.Font(family="Chiller",weight="bold",size=20)
        self.ready_button = Button(self.root,text="Ready...",font=self.ready_button_font,
                                   padx=50,pady=5,cursor='spider',activebackground="#5a75c9",
                                   relief='sunken',command=self.game_start)
        ready_x_por = (1375/self.swidth)
        ready_y_por = (739/self.sheight)
        self.ready_button.place(x=int(self.swidth*ready_x_por)
                                ,y=int(self.sheight*ready_y_por))
        self.canvas2.tag_raise(self)
    
    def game_start(self):
        snk.GameMainPage(self.root,self.control)