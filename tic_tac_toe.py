from tkinter import*
import random

root = Tk()
root.title("Tic Tac Toe")
tile_width = 10
tile_height = 5
tiles = ["","","","","","","","",""]
empty_tiles = ["bt0","bt1","bt2","bt3","bt4","bt5","bt6","bt7","bt8"]

my_symbol = ""
cpu_symbol = ""
player_dan = ""

def select_symbol(select_sym_name):
    global my_symbol,cpu_symbol,player_dan
    if select_sym_name == "x":
        my_symbol = "x"
        cpu_symbol = "o"
        player_dan = "x"
    elif select_sym_name == "o":
        my_symbol = "o"
        cpu_symbol = "x"
        player_dan = "o"

def cpu_dan():
    if tiles[0] == "" and tiles[1] == my_symbol and tiles[2] == my_symbol:
        fill_tile_array(cpu_symbol,"bt0")
        empty_tiles.remove("bt0")
    elif tiles[0] == my_symbol and tiles[1] == "" and tiles[2] == my_symbol:
        fill_tile_array(cpu_symbol,"bt1")
        empty_tiles.remove("bt1")
    elif tiles[0] == my_symbol and tiles[1] == my_symbol and tiles[2] == "":
        fill_tile_array(cpu_symbol,"bt2")
        empty_tiles.remove("bt2")
    else:
        fill_tile_array(cpu_symbol,random.choice(empty_tiles))


def hit_tile(tile_id):
    if player_dan == my_symbol:
        fill_tile_array(my_symbol,tile_id)
        cpu_dan()

def fill_tile_array(fill_symbol,fill_tile_id):
    if fill_tile_id == "bt0":
        tiles[0] = fill_symbol
        empty_tiles.remove("bt0")
        btn0_text.set(fill_symbol)
    elif fill_tile_id == "bt1":
        tiles[1] = fill_symbol
        empty_tiles.remove("bt1")
        btn1_text.set(fill_symbol)
    elif fill_tile_id == "bt2":
        tiles[2] = fill_symbol
        empty_tiles.remove("bt2")
        btn2_text.set(fill_symbol)
    elif fill_tile_id == "bt3":
        tiles[3] = fill_symbol
        empty_tiles.remove("bt3")
        btn3_text.set(fill_symbol)
    elif fill_tile_id == "bt4":
        tiles[4] = fill_symbol
        empty_tiles.remove("bt4")
        btn4_text.set(fill_symbol)
    elif fill_tile_id == "bt5":
        tiles[5] = fill_symbol
        empty_tiles.remove("bt5")
        btn5_text.set(fill_symbol)
    elif fill_tile_id == "bt6":
        tiles[6] = fill_symbol
        empty_tiles.remove("bt6")
        btn6_text.set(fill_symbol)
    elif fill_tile_id == "bt7":
        tiles[7] = fill_symbol
        empty_tiles.remove("bt7")
        btn7_text.set(fill_symbol)
    elif fill_tile_id == "bt8":
        tiles[8] = fill_symbol
        empty_tiles.remove("bt8")
        btn8_text.set(fill_symbol)
    print(empty_tiles)



f = Frame(root, width=400,height=400)
f.pack()

select_symbol_x = Button(f,text = "Select X",width=tile_width+5,height=tile_height,bg="dodgerblue",fg="#fff",command=lambda:select_symbol("x"))
select_symbol_x.grid(column=3, row=0)

select_symbol_o = Button(f,text = "Select O",width=tile_width+5,height=tile_height,bg="dodgerblue",fg="#fff",command=lambda:select_symbol("o"))
select_symbol_o.grid(column=3, row=1)




# ------- 9 Tile grid buttons---------------

btn0_text =StringVar()
bt0 = Button(f,textvariable = btn0_text,width=tile_width,height=tile_height,command=lambda:hit_tile("bt0"))
bt0.grid(column=0, row=0)

btn1_text =StringVar()
bt1 = Button(f,textvariable = btn1_text,width=tile_width,height=tile_height,command=lambda:hit_tile("bt1"))
bt1.grid(column=1, row=0)

btn2_text =StringVar()
bt2 = Button(f,textvariable = btn2_text,width=tile_width,height=tile_height,command=lambda:hit_tile("bt2"))
bt2.grid(column=2, row=0)



btn3_text =StringVar()
bt3 = Button(f,textvariable = btn3_text,width=tile_width,height=tile_height,command=lambda:hit_tile("bt3"))
bt3.grid(column=0, row=1)

btn4_text =StringVar()
bt4 = Button(f,textvariable = btn4_text,width=tile_width,height=tile_height,command=lambda:hit_tile("bt4"))
bt4.grid(column=1, row=1)

btn5_text =StringVar()
bt5 = Button(f,textvariable = btn5_text,width=tile_width,height=tile_height,command=lambda:hit_tile("bt5"))
bt5.grid(column=2, row=1)



btn6_text =StringVar()
bt6 = Button(f,textvariable = btn6_text,width=tile_width,height=tile_height,command=lambda:hit_tile("bt6"))
bt6.grid(column=0, row=2)

btn7_text =StringVar()
bt7 = Button(f,textvariable = btn7_text,width=tile_width,height=tile_height,command=lambda:hit_tile("bt7"))
bt7.grid(column=1, row=2)

btn8_text =StringVar()
bt8 = Button(f,textvariable = btn8_text,width=tile_width,height=tile_height,command=lambda:hit_tile("bt8"))
bt8.grid(column=2, row=2)


root.mainloop()
