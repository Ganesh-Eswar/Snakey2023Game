import sys
from os import path
from tkinter import font as font 
from tkinter import * 
from PIL import Image,ImageTk
import rules_and_regulations as rr
from ctypes import windll 

class SnakeyApp(Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        try:
            windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass
        self.application_width = self.winfo_screenwidth()
        self.application_height = int(self.winfo_screenheight()-(self.winfo_screenheight()*0.07))
        self.setting_assets()
        self.basic_setups()
        
    def setting_assets(self):
        bundle_dir = getattr(sys,"_MEIPASS",path.abspath(path.dirname(__file__)))
        self.path_to_logo = path.join(bundle_dir,"assets","green_snake_logo.png")
        self.path_to_enterbg = path.join(bundle_dir,"assets","snake_front_title.png")
        self.path_to_rulesbg = path.join(bundle_dir,"assets","rules_and_regulations.png")
        self.path_to_gamemainbg = path.join(bundle_dir,"assets","third_main_page.png")
        self.path_to_player1img = path.join(bundle_dir,"assets","snakeee.jpg")
        self.path_to_player2img = path.join(bundle_dir,"assets","player2img.png")
        self.path_to_minus1 = path.join(bundle_dir,"assets","no-1.jpg")
        self.path_to_minus3 = path.join(bundle_dir,"assets","no-3.jpg")
        self.path_to_minus2 = path.join(bundle_dir,"assets","no-2.jpg")
        self.path_to_no0 = path.join(bundle_dir,"assets","no0.jpg")
        self.path_to_no1 = path.join(bundle_dir,"assets","no1.jpg")
        self.path_to_no2 = path.join(bundle_dir,"assets","no2.jpg")
        self.path_to_no3 = path.join(bundle_dir,"assets","no3.jpg")
        self.path_to_p1coin = path.join(bundle_dir,"assets","player1coin.png")
        self.path_to_p2coin = path.join(bundle_dir,"assets","player2coin.png")
        self.path_to_congrats = path.join(bundle_dir,"assets","congrats_player1.png")
        self.path_to_sbite = path.join(bundle_dir,"assets","snake_bite_disp.png")
        self.path_to_ladder = path.join(bundle_dir,"assets","ladder_pick.png")
        self.path_to_lossbg = path.join(bundle_dir,"assets","player1_lose.png")
 
    def basic_setups(self):
        self.title("Snakey2023")
        pil_snake_img = Image.open(self.path_to_logo)
        green_snake_img = ImageTk.PhotoImage(pil_snake_img)
        self.iconphoto(False,green_snake_img)
        self.geometry(f"{self.application_width}x{self.application_height}")
        self.canvas_frame()
    
    def canvas_frame(self):
        self.canvas = Canvas(self,width=self.application_width,
                             height=self.application_height,
                             highlightthickness=0,cursor="spider")
        self.canvas.grid(row=0,column=0)
        self.enter_bg = Image.open(self.path_to_enterbg)
        self.enter_bg = self.enter_bg.resize((self.application_width,self.application_height))
        self.enter_snake = ImageTk.PhotoImage(self.enter_bg)
        self.canvas.create_image(0,0,anchor=NW,image=self.enter_snake)        
        self.adding_buttons()
    
    def adding_buttons(self):
        self.button_font = font.Font(family="Chiller",weight='bold',size=20)
        self.quit_font = font.Font(family="Chiller",weight='normal',size=15)
        self.start_button = Button(self,text="Start",padx=100,pady=5,foreground="white",
                                   bg="#160002",borderwidth=5,
                                   font=self.button_font,cursor='spider',command=self.rules_page)
        start_x_por = (450/self.application_width)
        start_y_por = (400/self.application_height)
        self.start_button.place(x=int(self.application_width*start_x_por),
                                y=int(self.application_height*start_y_por))
        self.quit_button = Button(self,text="Quit",padx=20,pady=5,foreground="white",
                                   bg="#160002",borderwidth=5,
                                   font=self.quit_font,cursor='spider',command=self.delete_all)
        quit_x_por = (630/self.application_width)
        quit_y_por = (500/self.application_height)
        self.quit_button.place(x=int(self.application_width*quit_x_por),
                               y=int(self.application_height*quit_y_por))
        
    def rules_page(self):
        rr.RulesAndRegulations(self,self) 

    def delete_all(self):
        self.destroy()
    
if __name__ == "__main__":
    app = SnakeyApp()
    app.mainloop()