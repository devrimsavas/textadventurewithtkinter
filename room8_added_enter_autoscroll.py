from tkinter import *
from tkinter import messagebox
from PART_1_CLASSES import * #room class and constructor
from opening import opening_screen
from PIL import ImageTk,Image

intro_text=""
#start game, take player name and initialize 
def start_new_game():
    screen.delete("1.0",END)
    global player
    global player_entry
    global intro_text
    take_player_window=Toplevel(root)

    def take_name():
        global player
        global intro_text
        player_name=player_entry.get()
        if player_name=="":
            player_name="Unknown Hero"

        take_player_window.destroy()
        player=Player(player_name)
        player.location=living_room
        player_location_label.config(text=f"Your Location:\n{player.location}")
        intro_text=f"""\n\n
Player {player_name.upper()} Welcome to House of the Ushers,\n
in this house,stupid adventures wait you.\n
Collect all items in the house. Dangerous and Stupid.\n
Good Luck {player_name.upper()}
-----------------------------------------------------
"""
        screen.insert("1.0",intro_text)
    
    take_player_window.title("enter player name ")
    take_player_window.geometry("420x260")

    player_label=Label(take_player_window,text="What is your name traveller ?",font=("Terminal",16))
    player_label.place(x=50,y=50)
    player_entry=Entry(take_player_window,width=20,font=("Terminal",16))
    player_entry.place(x=110,y=80)
  
    get_name = Button(take_player_window, text="Submit your name",font=("terminal",14 ),command=take_name) # , command=take_player_window.destroy)
    get_name.place(x=130, y=120)


    
    screen.insert("1.0",intro_text)
    



def move_player(player_command):
    global player
   
    #player should not player if he did not start new game
    if player is None:
        messagebox.showwarning("Warning","you must start a new game from main menu")
        return 
    command_entry.delete(0,END)
    
    if player_command in ["north", "south", "east", "west"]:
        move_result = player.move(player_command)
        screen.insert(END, f'{move_result}\n')
        
    #other commands
    elif player_command=="look around":
        look_result = player.look_around()
        screen.insert(END, look_result)

    elif player_command.startswith("take "):
        item = player_command[5:]
        player.take(item)
        screen.insert(END,f'{player.name} you took item: {item}\n')

    elif player_command=="show inventory":
        inventory_result = player.show_inventory()
        screen.insert(END,f'{inventory_result}')

    elif player_command=="quit":
        screen.insert(END,f'you gave up so easy {player.name}\nBye bye')
        root.destroy()
        
    else:
        screen.insert(END,f"I did not understand that command\n")

    player_location_label.config(text=f"Your Location:\n{player.location}")
    screen.yview_moveto(1.0)

       
    

def exit_game():
    pass

def about_game():
    about_window=Toplevel(root)
    about_text="""
MisAdventures of Lousy Traveller
This text adventure show how we can
create a simple or complex text-based
graphic adventure game
by Devrim Savas yilmaz
"""
    about_window.title("About Game")
    about_window.geometry("420x260")
    info_text = Text(about_window, width=40, height=10, wrap=WORD, borderwidth=3, spacing3=2, font=("terminal",14 ))
    info_text.place(x=10, y=10)
    info_text.insert(END, about_text)
    info_text.config(state="disabled", bg="beige")
    close_this = Button(about_window, text="CLOSE THIS WINDOW",font=("terminal",14 ), command=about_window.destroy)
    close_this.place(x=130, y=220)


root=Tk()
root.geometry("1075x770")
root.title("Heroe's Adventure")
root.iconbitmap("hero_icon.ico")
root.config(bg="lightblue")
root.resizable(False,False)

#MENU BAR
menubar=Menu(root)
gamemenu=Menu(menubar,tearoff=0,font=("Terminal",16))
menubar.add_cascade(label="Game",menu=gamemenu,font=("Terminal",16))

gamemenu.add_command(label="New Game",command=start_new_game)
gamemenu.add_command(label="Exit Game",command=exit_game)

aboutmenu=Menu(menubar,tearoff=0,font=("Terminal",16))

menubar.add_cascade(label="About",menu=aboutmenu,font=("Terminal",16))
aboutmenu.add_command(label="About",command=lambda:about_game())


root.config(menu=menubar)
#BIG FRAME
main_frame=LabelFrame(root,width=1075,height=770,bd=4,relief="sunken",bg="brown")
main_frame.place(x=2,y=2)

#SCREEN
screen_holder=LabelFrame(main_frame,text="Play Screen",width=730,height=570,bd=5,relief="sunken",bg="beige",font=("Terminal",14))
screen_holder.place(x=30,y=30)
    #screen
screen=Text(screen_holder,width=70,height=29,borderwidth=5,relief="sunken",font=("Terminal",16),bg="black", fg="#FFCC00",wrap="word")
screen.configure(state="normal")
screen.yview_moveto(1.0)


screen.place(x=10,y=10)



#intro
global opening_screen
screen.insert("1.0",opening_screen)


#PLAYER INFO 
player_info_holder=LabelFrame(main_frame,text="Player Info",width=280,height=715,bg="beige",relief="sunken",font=("Terminal",14))
player_info_holder.place(x=765,y=30)

#PLAYER LOCATION
player_location_label=Label(player_info_holder,text="Your Location:",bg="beige",font=("Terminal",14))
player_location_label.place(x=1,y=10)

picture_holder=LabelFrame(player_info_holder,width=250,height=300,relief="sunken")
picture_holder.place(x=10,y=200)
#insert a picture later here comes room pictures. now just demo
demo_image=Image.open("cover.jpg")
demo_image=ImageTk.PhotoImage(demo_image)
image_label=Label(picture_holder,image=demo_image)
image_label.place(x=0,y=0)

#COMMANDS
player_command_holder=LabelFrame(main_frame,text="Commands",width=730,height=145,bg="blue",relief="sunken",font=("Terminal",14))
player_command_holder.place(x=30,y=605)
clear_screen=Button(player_command_holder,text="clear",font=("Terminal",16),command=lambda:screen.delete("1.0",END))
clear_screen.place(x=610,y=73)
    #commands label,entry
commands_text="Commands: [north,east,west,south]-[take,look around,show inventory, quit]"
defined_commands=Label(player_command_holder,text=commands_text,fg="black",bg="blue",font=("Terminal",14))
defined_commands.place(x=3,y=5)
command_label=Label(player_command_holder,text="Your command:",font=("Terminal",16),bg="blue")
command_label.place(x=3,y=73)
command_entry=Entry(player_command_holder,width=30,font=("Terminal",16),bg="#dce8da",fg="black",borderwidth=4,relief="sunken")
command_entry.bind("<Return>",lambda event,entry=command_entry:move_player(entry.get()))
command_entry.place(x=136,y=73)

#command enter
submit_button=Button(player_command_holder,width=10,text="ENTER",font=("Terminal",12),command=lambda:move_player(command_entry.get()))
submit_button.place(x=460,y=73)

#direction_set
direction_holder=LabelFrame(player_info_holder,text="Directions",width=250,height=130,relief="sunken",font=("Terminal",16))
direction_holder.place(x=10,y=550)

b_north=Button(direction_holder,text="NORTH",width=6,font=("Terminal",12),command=lambda:move_player("north"))
b_north.place(x=80,y=5)

b_south=Button(direction_holder,text="SOUTH",width=6,font=("Terminal",12),command=lambda:move_player("south"))
b_south.place(x=80,y=65)

b_west=Button(direction_holder,text="WEST",width=5,font=("Terminal",12),command=lambda:move_player("west"))
b_west.place(x=1,y=35)

b_east=Button(direction_holder,text="EAST",width=5,font=("Terminal",12),command=lambda:move_player("east"))
b_east.place(x=165,y=35)

direct_text=Label(direction_holder, text="─┼─",font=("Terminal",15,"bold"))
direct_text.place(x=90,y=35)


root.mainloop()
