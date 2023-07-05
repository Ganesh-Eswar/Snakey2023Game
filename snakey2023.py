from tkinter import font as font 
from tkinter import * 
from PIL import Image,ImageTk
import random
import time

class GameMainPage():
    def __init__(self,parent,controller):
        self.root2 = parent  
        self.ctrl = controller
        self.player1_position = 0
        self.player2_position = 0 
        self.swidth = self.ctrl.application_width
        self.sheight = self.ctrl.application_height
        self.canvas3 = Canvas(self.root2,width=self.swidth,
                             height=self.sheight,
                             highlightthickness=0,cursor="spider")
        self.canvas3.grid(row=0,column=0) 
        game_bg = Image.open(self.ctrl.path_to_gamemainbg)
        game_bg = game_bg.resize((self.swidth,self.sheight))
        self.game_image = ImageTk.PhotoImage(game_bg)
        self.canvas3.create_image(0,0,anchor=NW,image=self.game_image) 
        self.player1_coords()
        self.player2_coords()    
        self.set_up_dice_images()
        self.coins_set_up()
        self.adding_buttons()

    def adding_buttons(self):
        self.player_button_font = font.Font(family="Chiller",weight='bold',size=20)
        self.player1_name = StringVar(value="Player 1")
        self.player1_button = Button(self.root2,textvariable=self.player1_name,
                                     font=self.player_button_font,
                                     padx=20,command=self.change_dice_img,
                                     activebackground="yellow")
        p1_x_por = (160/self.swidth)
        p1_y_por = (520/self.sheight)
        self.player1_button.place(x=int(self.swidth*p1_x_por),
                                  y=int(self.sheight*p1_y_por))
        self.resize_x_por = (150/self.swidth)
        self.resize_y_por = (150/self.sheight)
        player1_img = Image.open(self.ctrl.path_to_player1img).resize((
            int(self.swidth*self.resize_x_por),int(self.sheight*self.resize_y_por)))
        player1_tkimg = ImageTk.PhotoImage(player1_img)
        self.player1_image = Button(image=player1_tkimg)
        image_x_por = 145/self.swidth
        image_y_por = 320/self.sheight
        self.player1_image.place(x=int(self.swidth*image_x_por),y=int(self.sheight*image_y_por))
        self.player2_name = StringVar(value="Computer")
        self.player2_button = Button(self.root2,textvariable=self.player2_name,
                                     font=self.player_button_font,
                                     padx=20)
        p2_x_por = 1300/self.swidth
        p2_y_por = 520/self.sheight
        self.player2_button.place(x=int(self.swidth*p2_x_por),
                                  y=int(self.sheight*p2_y_por))
        
        player2_img = Image.open(self.ctrl.path_to_player2img).resize((
            int(self.swidth*self.resize_x_por),int(self.sheight*self.resize_y_por)
        ))
        player2_tkimg = ImageTk.PhotoImage(player2_img)
        self.player2_image = Button(image=player2_tkimg)
        i2_xp = 1285/self.swidth
        i2_yp = 320/self.sheight
        self.player2_image.place(x=int(self.swidth*i2_xp),
                                 y=int(self.sheight*i2_yp))
        self.canvas3.tag_raise()
        
    def set_up_dice_images(self):
        dice_normal_imgs = [self.ctrl.path_to_minus3,
                            self.ctrl.path_to_minus2,
                            self.ctrl.path_to_minus1,
                            self.ctrl.path_to_no0,
                            self.ctrl.path_to_no1,
                            self.ctrl.path_to_no2,
                            self.ctrl.path_to_no3]
        self.dice_images_dict = {}
        iindex = 0
        self.resize_x_por = (150/self.swidth)
        self.resize_y_por = (150/self.sheight)
        for index in range(-3,len(dice_normal_imgs)-3,1):
            open_img = Image.open(dice_normal_imgs[iindex]).resize((
                int(self.swidth*self.resize_x_por),int(self.sheight*self.resize_y_por)
            ))
            tk_img = ImageTk.PhotoImage(image=open_img)
            self.dice_images_dict[index] = tk_img
            iindex += 1
    
    def coins_set_up(self):
        resize_coin_xp = 30/self.swidth
        resize_coin_yp = 30/self.sheight 
        player1coin = Image.open(self.ctrl.path_to_p1coin).resize((
            int(self.swidth*resize_coin_xp),int(self.sheight*resize_coin_yp)))
        player2coin = Image.open(self.ctrl.path_to_p2coin).resize((
            int(self.swidth*resize_coin_xp),int(self.sheight*resize_coin_yp)
        ))
        tk_p1coin = ImageTk.PhotoImage(image=player1coin)
        tk_p2coin = ImageTk.PhotoImage(image=player2coin)
        self.player1_coin = Label(self.root2,image=tk_p1coin)
        self.player2_coin = Label(self.root2,image=tk_p2coin)
        self.p1_coin = tk_p1coin
        self.p2_coin = tk_p2coin
        p2_x_por = 780/self.swidth
        p2_y_por = 395/self.sheight
        self.player2_coin.place(x=int(self.swidth*p2_x_por),
                                y=int(self.sheight*p2_y_por))
        p1_x_por = 748/self.swidth
        p1_y_por = 395/self.sheight
        self.player1_coin.place(x=int(self.swidth*p1_x_por),
                                y=int(self.sheight*p1_y_por))
        
    def change_dice_img(self):
        self.number = random.randint(-3,3)
        self.dice_label = Label(self.root2,
                                image=self.dice_images_dict[self.number])
        dxp = 70/self.swidth
        dyp = 640/self.sheight
        self.dice_label.place(x=int(self.swidth*dxp),
                              y=int(self.sheight*dyp))
        GameEngine(self.root2,self,self.ctrl)
   
    def player1_coords(self):  
        player1_init_coord = []
        self.player1_coord_dict = {}
        xvp = 350/self.swidth
        x_value = int(xvp*self.swidth)
        x_increment = int((100/self.swidth)*self.swidth)
        r1 = int((703/self.sheight)*self.sheight)
        r2 = int((638/self.sheight)*self.sheight)
        r3 = int((578/self.sheight)*self.sheight)
        r4 = int((515/self.sheight)*self.sheight)
        r5 = int((453/self.sheight)*self.sheight)
        r6 = int((391/self.sheight)*self.sheight)
        r7 = int((330/self.sheight)*self.sheight)
        r8 = int((270/self.sheight)*self.sheight)
        r9 = int((207/self.sheight)*self.sheight)
        r10 = int((148/self.sheight)*self.sheight)
        r11 = int((87/self.sheight)*self.sheight)
        for y in [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11]:
            for column in range(1,10):
                co_ord = [x_value,y]
                player1_init_coord.append(co_ord)
                x_value += x_increment
            x_value = int(xvp*self.swidth)
        start = -41
        temp = start 
        self.board_number = []
        start_flag = True
        for i in range(0,11):
            if(i%2 != 0):
                start += 1
                temp = start 
            elif(i%2 ==0 and not(start_flag)):
                start += 17
                temp = start 
            for j in range(0,9):
                if(i%2 ==0):
                    self.board_number.append(temp)
                    temp -=1
                elif(i%2 != 0):
                    self.board_number.append(temp)
                    temp += 1       
            if(start_flag):
                start_flag = False     
        for combi in range(len(self.board_number)):
            self.player1_coord_dict[self.board_number[combi]] = player1_init_coord[combi]
   
    def player2_coords(self):  
        player2_init_coord = []
        self.player2_coord_dict = {}
        x_value = int((362/self.swidth)*self.swidth)
        x_increment = int((100/self.swidth)*self.swidth)
        r1 = int((703/self.sheight)*self.sheight)
        r2 = int((638/self.sheight)*self.sheight)
        r3 = int((578/self.sheight)*self.sheight)
        r4 = int((515/self.sheight)*self.sheight)
        r5 = int((453/self.sheight)*self.sheight)
        r6 = int((391/self.sheight)*self.sheight)
        r7 = int((330/self.sheight)*self.sheight)
        r8 = int((270/self.sheight)*self.sheight)
        r9 = int((207/self.sheight)*self.sheight)
        r10 = int((148/self.sheight)*self.sheight)
        r11 = int((87/self.sheight)*self.sheight)
        for y in [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11]:
            for column in range(1,10):
                co_ord = [x_value,y]
                player2_init_coord.append(co_ord)
                x_value += x_increment
            x_value = int((362/self.swidth)*self.swidth)           
        for combi in range(len(self.board_number)):
            self.player2_coord_dict[self.board_number[combi]] = player2_init_coord[combi]

class GameEngine():
    def __init__(self,parent,controller,parentcontrl) -> None:
        self.parent = parent
        self.control = controller
        self.ctrl = parentcontrl
        self.swidth = self.ctrl.application_width
        self.sheight = self.ctrl.application_height
        self.game_end_flag = True 
        self.reset_button_font = font.Font(family="Chiller",weight='bold',size=15)
        self.reset_button = Button(self.parent,text="Reset",
                                   font=self.reset_button_font,
                                   padx=20,command=self.reset)
        self.reset_button.place(x=int((1300/self.swidth)*self.swidth),
                                y=int((580/self.sheight)*self.sheight))
        self.snakes_list = [[49,-5],[44,-10],[27,0],[-7,11],[-36,-1],
                            [-49,8]]
        self.ladder_list = [[5,39],[12,32],[28,47],[-4,-41],[-21,-44],
                            [-9,-37]]
        self.snakes_head = [49,44,27,-7,-36,-49]
        self.ladder_base = [5,12,28,-4,-21,-9] 
        dice_value = self.control.number
        player1_position = self.control.player1_position
        player2_position = self.control.player2_position
        if(player1_position > 40):
            dice_value = abs(dice_value)
        elif(player1_position < -40):
            if(dice_value >0):
                dice_value = -(dice_value)         
        p1_curr_position = player1_position + dice_value
        if(p1_curr_position > 49 or p1_curr_position < -49):
            if(p1_curr_position == 50 or p1_curr_position == -50):
                self.control.player2_coin.place(x=int((780/self.swidth)*self.swidth),
                                                y=int((395/self.sheight)*self.sheight))
                self.control.player1_coin.place(x=int((748/self.swidth)*self.swidth),
                                                y=int((395/self.sheight)*self.sheight))
                self.control.player1_button["state"] = "normal"
                self.control.player2_button["state"] = "disabled"
                self.control.player1_position = 0
                self.control.player2_position = 0
                self.player1_win = Toplevel(self.parent)
                self.canvas4 = Canvas(self.player1_win,width=int((1200/self.swidth)*self.swidth),
                             height=int((600/self.sheight)*self.sheight),
                             highlightthickness=0,cursor="spider")
                self.player1_win.wm_transient(self.parent)      
                self.canvas4.grid(row=0,column=0) 
                congrats_bg = Image.open(self.ctrl.path_to_congrats)
                congrats_bg = congrats_bg.resize((int((1200/self.swidth)*self.swidth),
                                                  int((600/self.sheight)*self.sheight)))
                self.congrats_image = ImageTk.PhotoImage(congrats_bg)
                self.canvas4.create_image(0,0,anchor=NW,image=self.congrats_image) 
                self.player1_win.update()
                self.parent.update()
                time.sleep(3)
                self.player1_win.destroy()
                self.game_end_flag = False 
            else:
                p1_curr_position = p1_curr_position - dice_value
        if(p1_curr_position in self.snakes_head):
            self.coin_place = self.control.player1_coord_dict[p1_curr_position]
            self.control.player1_coin.place(x=self.coin_place[0],y=self.coin_place[1])
            self.player1_snake = Toplevel(self.parent)
            self.canvas6 = Canvas(self.player1_snake,width=int((1200/self.swidth)*self.swidth),
                        height=int((600/self.sheight)*self.sheight),
                        highlightthickness=0,cursor="spider")
            self.player1_snake.wm_transient(self.parent)
            self.canvas6.grid(row=0,column=0) 
            sbite_bg = Image.open(self.ctrl.path_to_sbite)
            sbite_bg = sbite_bg.resize((int((1200/self.swidth)*self.swidth),
                                        int((600/self.sheight)*self.sheight)))
            self.sbite_image = ImageTk.PhotoImage(sbite_bg)
            self.canvas6.create_image(0,0,anchor=NW,image=self.sbite_image) 
            self.player1_snake.update()
            self.parent.update()
            time.sleep(3)
            self.player1_snake.destroy()        
            iindex = self.snakes_head.index(p1_curr_position)
            p1_move = self.snakes_list[iindex]
            p1_curr_position = p1_move[1]
        elif(p1_curr_position in self.ladder_base):
            self.coin_place = self.control.player1_coord_dict[p1_curr_position]
            self.control.player1_coin.place(x=self.coin_place[0],y=self.coin_place[1])
            self.player1_ladder = Toplevel(self.parent)
            self.canvas7 = Canvas(self.player1_ladder,width=int((1200/self.swidth)*self.swidth),
                        height=int((600/self.sheight)*self.sheight),
                        highlightthickness=0,cursor="spider")
            self.player1_ladder.wm_transient(self.parent)
            self.canvas7.grid(row=0,column=0) 
            ladder_bg = Image.open(self.ctrl.path_to_ladder)
            ladder_bg = ladder_bg.resize((int((1200/self.swidth)*self.swidth),
                                          int((600/self.sheight)*self.sheight)))
            self.ladder_image = ImageTk.PhotoImage(ladder_bg)
            self.canvas7.create_image(0,0,anchor=NW,image=self.ladder_image) 
            self.player1_ladder.update()
            self.parent.update()
            time.sleep(3)
            self.player1_ladder.destroy()
            iindex = self.ladder_base.index(p1_curr_position)
            p1_move = self.ladder_list[iindex]
            p1_curr_position = p1_move[1]
        if(self.game_end_flag):
            self.control.player1_position = p1_curr_position
            self.coin_place = self.control.player1_coord_dict[p1_curr_position]
            self.control.player1_coin.place(x=self.coin_place[0],y=self.coin_place[1])
            self.control.player1_button["state"] = "disabled"
            self.control.player2_button["state"] = "normal"
            self.parent.update()
            time.sleep(1)
            self.control.player2_button["background"] = "yellow"
            self.parent.update()
            time.sleep(1)
            self.control.player2_button["background"] = "white"
            self.parent.update()
            dice_value = random.randint(-3,3)
            self.control.dice_label['image'] = self.control.dice_images_dict[dice_value]      
            self.parent.update()
            if(player2_position > 40):
                dice_value = abs(dice_value)
            elif(player2_position < -40):
                if(dice_value >0):
                    dice_value = -(dice_value)
            p2_curr_position = player2_position + dice_value
            if(p2_curr_position > 49 or p2_curr_position < -49):
                if(p2_curr_position == 50 or p2_curr_position == -50):
                    self.control.player2_coin.place(x=int((780/self.swidth)*self.swidth),
                                                    y=int((395/self.sheight)*self.sheight))
                    self.control.player1_coin.place(x=int((780/self.swidth)*self.swidth),
                                                    y=int((395/self.sheight)*self.sheight))
                    self.control.player1_button["state"] = "normal"
                    self.control.player2_button["state"] = "disabled"
                    self.control.player1_position = 0
                    self.control.player2_position = 0
                    self.player1_loss = Toplevel(self.parent)
                    self.canvas5 = Canvas(self.player1_loss,width=int((1200/self.swidth)*self.swidth),
                                height=int((600/self.sheight)*self.sheight),
                                highlightthickness=0,cursor="spider")
                    self.player1_loss.wm_transient(self.parent)
                    self.canvas5.grid(row=0,column=0) 
                    loss_bg = Image.open(self.ctrl.path_to_lossbg)
                    loss_bg = loss_bg.resize((int((1200/self.swidth)*self.swidth),
                                              int((600/self.sheight)*self.sheight)))
                    self.loss_image = ImageTk.PhotoImage(loss_bg)
                    self.canvas5.create_image(0,0,anchor=NW,image=self.loss_image) 
                    self.player1_loss.update()
                    self.parent.update()
                    time.sleep(3)
                    self.player1_loss.destroy()
                    self.game_end_flag = False 
                else:
                    p2_curr_position = p2_curr_position - dice_value
            elif(p2_curr_position in self.snakes_head):
                iindex = self.snakes_head.index(p2_curr_position)
                p2_move = self.snakes_list[iindex]
                p2_curr_position = p2_move[1]
            elif(p2_curr_position in self.ladder_base):
                iindex = self.ladder_base.index(p2_curr_position)
                p2_move = self.ladder_list[iindex]
                p2_curr_position = p2_move[1]
            if(self.game_end_flag):
                self.control.player2_position = p2_curr_position
                self.coin_place = self.control.player2_coord_dict[p2_curr_position]
                self.control.player2_coin.place(x=self.coin_place[0],y=self.coin_place[1])   
                self.control.player1_button["state"] = "normal"
                self.control.player2_button["state"] = "disabled"

    def reset(self):
        self.control.player1_position = 0
        self.control.player2_position = 0
        self.control.player2_coin.place(x=int((780/self.swidth)*self.swidth),y=int((395/self.sheight)*self.sheight))
        self.control.player1_coin.place(x=int((748/self.swidth)*self.swidth),y=int((395/self.sheight)*self.sheight))
        self.parent.update()  
        