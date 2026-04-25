import tkinter as tk, json, shutil
from tkinter.filedialog import *
from PIL import Image, ImageTk, ImageDraw



def delete_account(*args):
    def no(*args):
        first_del.destroy()

    def yes(*args):
        first_del.destroy()
        second_del = tk.Toplevel(window)
        second_del.geometry('500x400')
        second_del.title('Delete Account')
        second_del.resizable(False, False)
        second_del.grab_set()
        text_2_del = tk.Label(master=second_del, text='Введите пароль, для\nподтверждения\nоперации', font = ('Dela Gothic One', 24))
        text_2_del.place(x=48, y=32, width=404, height=138)
        tk_canvas = tk.Canvas(width=400, height=64, highlightthickness=0, bg='#000000', master=second_del)
        tk_canvas.create_image(400 / 2, 64 / 2, image=canvas_input_img_2, anchor=tk.CENTER)
        tk_canvas.place(x=50, y=215)
        second_del.mainloop()

    first_del = tk.Toplevel(window)
    first_del.geometry('500x400')
    first_del.title('Delete Account')
    first_del.grab_set()
    first_del.resizable(False, False)
    text_1_del = tk.Label(text='Вы уверены, что\nхотите покинуть\nнас?', master=first_del, font = ('Dela Gothic One', 24))
    text_1_del.place(x = 86, y=32, width=328, height=138)
    yes_btn = get_tk_image('../img/yes_btn_del_ac.png', 200,60)
    yes_lbl = tk.Label(master=first_del, image=yes_btn, height=60, width=200)
    yes_lbl.place(x = 35, y = 264)
    yes_lbl.config(cursor="hand2")
    yes_lbl.bind("<Button-1>", yes)

    no_btn = get_tk_image('../img/no_btn_del_ac.png', 200, 60)
    no_lbl = tk.Label(master=first_del, image=no_btn, height=60, width=200)
    no_lbl.place(x=265, y=264)
    no_lbl.config(cursor="hand2")
    no_lbl.bind("<Button-1>", no)


    first_del.mainloop()

def change_avatar(event=None):
    path_new_avatar = askopenfilename(filetypes=[('PNG Image file', '.png')])
    if path_new_avatar:
        global avatar_now, avatar
        shutil.copyfile(path_new_avatar, '../img/avatar.png')
        print(1)
        account_settings["Avatar"] = '../img/avatar.png'
        print(2)
        with open("../json/account_settings.json", 'w', encoding='utf-8') as json_:
            json.dump(account_settings, json_, ensure_ascii=False, indent=4)
        print(3)
        avatar_now = create_avatar('../img/avatar.png')
        avatar.create_image(161/2, 161 / 2, image =  avatar_now, anchor=tk.CENTER)

def save_button(event=None):
    for text in range(len(tk_input)):
        account_settings[ list(account_settings.keys())[text]] = tk_input[text].get("1.0", "end-1c")
    with open("../json/account_settings.json", 'w', encoding='utf-8') as json_:
        json.dump(account_settings, json_, ensure_ascii=False, indent=4)

def on_escape(event):
    widget = event.widget
    # Снимаем выделение
    widget.tag_remove(tk.SEL, "1.0", tk.END)
    # Убеждаемся, что курсор "активен" (необязательно, но надёжно)
    widget.mark_set("insert", "insert")
    widget.master.focus_set()
    # Отменяем дальнейшую обработку Escape (чтобы не было звуков/ошибок)
    return "break"

def make_single_line_handler(max_chars):
    def on_key_release(event=None):
        widget = event.widget
        text = widget.get("1.0", "end-1c")
        # Удаляем все символы новой строки (на случай вставки)
        if '\n' in text:
            text = text.replace('\n', '')
            widget.delete("1.0", "end")
            widget.insert("1.0", text[:max_chars])
        elif len(text) > max_chars:
            widget.delete(f"1.{max_chars}", "end")
        widget.edit_modified(False)
    return on_key_release

def block_enter(event):
    return "break"

def get_tk_image(path: str, resize_x: int, resize_y: int) -> ImageTk.PhotoImage:
    image = Image.open(path).convert("RGBA")
    image = image.resize((resize_x, resize_y), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(image)

def rounded_rect(canvas, x1, y1, x2, y2, radius, **kwargs):
    points = [
        x1 + radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)

def create_avatar(path):
    avatar_image = Image.open(path).resize((160,160),  Image.Resampling.LANCZOS)
    mask = Image.new("L", (160, 160), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 160, 160), fill=255)

    image = Image.new('RGBA', (160, 160))
    image.paste(avatar_image, (0, 0), mask)
    return ImageTk.PhotoImage(image)

with open("../json/account_settings.json", 'r', encoding='utf-8') as json_file:
    account_settings = json.load(json_file)
    print(account_settings)


canvas_input =[]
tk_input = []
labels = []
info_labels = []
info_labels_int = []
avatar_now = ''


window = tk.Tk()
window.title('Account settings')
window.geometry('1440x950-150-90')
window.resizable(width=False, height=False)
window.configure(bg='#EFF6FF')
window.iconphoto(True, tk.PhotoImage(file="../img/main_icon.png"))

canvas_input_img = get_tk_image('../img/input_account_settings_input.png', 550, 64)
canvas_input_img_2 = get_tk_image('../img/input_account_settings_input.png', 400, 64)

header_shadow = tk.Frame(window, bg='#EBEBEB', width=1440, height=114)
header_shadow.place(x=0, y=0)

header_shadow_2 = tk.Frame(window, bg='#D8DEE7', width=1440, height=110)
header_shadow_2.place(x=0, y=0)

header_frame = tk.Frame(window, bg="#FFFFFF", width=1440, height=106)
header_frame.place(x=0, y=0)  # или используй grid/pack при необходимости

header_frame.pack_propagate(False)
header_shadow.pack_propagate(False)
header_shadow_2.pack_propagate(False)


main_text = tk.Label(text='ЭкзаменПро', font = ('Dela Gothic One', 24), bg='#FFFFFF')
main_text.place(x=113,y=21)

logo_img = get_tk_image('../img/main_icon.png', 91,91)
logo_img_lb = tk.Label(window, image=logo_img, height=91, width=91, bg='#FFFFFF')
logo_img_lb.place(x=12, y=4)


account_info_frame = tk.Canvas( width=866, height=746, bg="#EFF6FF", highlightthickness=0)
account_info_frame.place(x=25, y=139)
rounded_rect(account_info_frame, 0, 0, 866, 746, radius=84, fill="#FFFFFF", outline="")

statistic_frame = tk.Canvas(width=456, height=345, bg="#EFF6FF", highlightthickness=0)
statistic_frame.place(x=952, y=139)
rounded_rect(statistic_frame, 0, 0, 456, 345, radius=73, fill="#FFFFFF", outline="")

theme_frame = tk.Canvas(width=456, height=131, bg='#EFF6FF', highlightthickness=0)
theme_frame.place(x=952, y=537)
rounded_rect(theme_frame, 0, 0, 456, 131, radius= 130, fill='#FFFFFF', outline='')

delete_account_frame = tk.Canvas(width=370, height=150, bg='#EFF6FF', highlightthickness=0)

image_delete = get_tk_image('../img/Кнопка удалить.png', 350,120)
delete_account_frame.create_image(350/2,130/2, image=image_delete, anchor=tk.CENTER)
delete_account_frame.place(x=1006-20,y=754-20)
delete_account_frame.bind('<Button-1>', delete_account)
delete_account_frame.config(cursor="hand2")

statistic_text = tk.Label(text='Общая статистика', font = ('Dela Gothic One', 24), bg='#FFFFFF')
statistic_text.place(x=1000,y=167)

for i in range(len(account_settings['Info_keys'])):
        y = 244 + i * 46
        info_labels.append(tk.Label(text=account_settings["Info_text"][i], font = ('Dela Gothic One', 15), bg='#FFFFFF'))
        info_labels[i].place(x=970,y=y)
        info_labels_int.append(tk.Label(text=account_settings[account_settings['Info_keys'][i]], font = ('Dela Gothic One', 15), bg='#FFFFFF'))
        info_labels_int[i].place(x=1342,y=y)

for i in range(6):
    labels.append(tk.Label(text=list(account_settings.keys())[i], font = ('Dela Gothic One', 20), bg='#FFFFFF'))
    canvas_input.append(tk.Canvas(width=550, height=64, highlightthickness=0, bg='#000000'))
    tk_input.append(tk.Text(width=28, height=1, font = ('Dela Gothic One', 15), bg='#FFFFFF', borderwidth=0, highlightthickness=0))
    if i<2:
        canvas_input[i].place(x=273, y=177+i*113)
        tk_input[i].place(x=290, y=190+i*113)
        labels[i].place(x=291, y=139+i*110)

    else:
        canvas_input[i].place(x=53, y=406+(i-2)*124)
        tk_input[i].place(x=70, y=419+(i-2)*124)
        labels[i].place(x=53, y=361+(i-2)*123)
    tk_input[i].insert('1.0', list(account_settings.values())[i])
    tk_input[i].bind("<KeyRelease>", make_single_line_handler(34))
    tk_input[i].bind("<Return>", block_enter)
    tk_input[i].bind("<Escape>", on_escape)
    canvas_input[i].create_image(550 / 2, 64 / 2, image=canvas_input_img, anchor=tk.CENTER)

image_save = get_tk_image('../img/save_button.png', 219, 141)
btn_save = tk.Canvas(width=219, height=141, highlightthickness=0, bg='#000000')
btn_save.place(x=636, y=698)
btn_save.create_image(218/2, 140/2, image=image_save, anchor=tk.CENTER)
btn_save.bind("<Button-1>", save_button)
btn_save.config(cursor="hand2")

avatar = tk.Canvas(width=161, height=161, bg='#FFFFFF', highlightthickness=0)
avatar.place(x=53,y=171)
avatar_now = create_avatar(account_settings["Avatar"])
avatar.create_image(161/2, 161 / 2, image =  avatar_now, anchor=tk.CENTER)

avatar_set = tk.Canvas(width=43, height=43, highlightthickness=0)
avatar_set_img = get_tk_image('../img/edit_avatar_img.png', 43,43)
avatar_set.create_image(43/2, 43/2, image = avatar_set_img, anchor=tk.CENTER)
avatar_set.place(x=162,y=294)
avatar_set.bind("<Button-1>", change_avatar)
btn_save.config(cursor="hand2")

window.mainloop()