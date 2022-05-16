from tkinter import *
from tkinter import filedialog
import tkinter.font as font
import customtkinter

# import webbrowser
from steganography import hide, unhide


# Configutation variables

RES_X, RES_Y = 1000, 620


# Global variables
INPUT_IMG = ""
INPUT_TEXT = ""
OUTPUT_IMG = "secret_image.png"
OUTPUT_TEXT = "extracted_text.txt"
# Member functions

# def callback(url):
#     webbrowser.open_new(url)


def hide_button():
    print("hide button pressed")
    hide(INPUT_IMG, INPUT_TEXT, OUTPUT_IMG)
    print("hide button finished")


def unhide_button():
    print("unhide button pressed")
    unhide(OUTPUT_IMG, OUTPUT_TEXT)
    print("unhide button finished")


def browse_inp_image():
    file = filedialog.askopenfile(
        mode="r",
        filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg")],
        title="Select an Image",
    )
    if file:
        print(f"Input image file received: {file.name}")
        global INPUT_IMG
        INPUT_IMG = file.name


def browse_inp_text():
    file = filedialog.askopenfile(
        mode="r", filetypes=[("Text Files", "*.txt")], title="Select an Image"
    )
    if file:
        print(f"Input Text file received: {file.name}")
        global INPUT_TEXT
        INPUT_TEXT = file.name



def browse_out_image():
    file = filedialog.askopenfile(
        mode="r",
        filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg")],
        title="Select an Image",
    )
    if file:
        print(f"Output image file received: {file.name}")
        global OUTPUT_IMG
        OUTPUT_IMG = file.name

# Window Configutations

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: blue (default), dark-blue, green

window = customtkinter.CTk()  # create CTk window like you do with the Tk window
window.title("Hide Secret Text")
x = window.winfo_screenwidth() // 2 - RES_X // 2
y = window.winfo_screenheight() // 2 - RES_Y // 2
window.geometry(f"{RES_X}x{RES_Y}+{x}+{y}")
window.configure(bg="#3A7FF6")


# Creating Canvas

canvas = Canvas(
    window,
    bg="#3A7FF6",
    height=620,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)


# Making rectangles and text_box in Canvas
canvas.create_rectangle(500.0, 0.0, 1000.0, 620.0, fill="#e6e9f0", outline="")

canvas.create_rectangle(
    39.0, 145.00000000000006, 147.0, 153.00000000000006, fill="#FFFFFF", outline=""
)

canvas.create_text(
    39.0,
    64.00000000000006,
    anchor="nw",
    text="Hide Secret Text",
    fill="#FFFFFF",
    font=("NewRocker Regular", 57 * -1),
)

canvas.create_text(
    23.0,
    197.00000000000006,
    anchor="nw",
    text="This tool hides a text file in an image",
    fill="#FFFFFF",
    font=("Neuton Regular", 26 * -1),
)

canvas.create_rectangle(
    529.0, 30.000000000000057, 969.0, 346.00000000000006, fill="#FBEBCE", outline=""
)

canvas.create_rectangle(
    529.0, 375.00000000000006, 969.0, 586.0, fill="#FBEBCE", outline=""
)

canvas.create_text(
    546.0,
    160.00000000000006,
    anchor="nw",
    text="Select text file:",
    fill="#171413",
    font=("Neuton Bold", 32 * -1),
)

canvas.create_text(
    545.0,
    408.00000000000006,
    anchor="nw",
    text="Select image:",
    fill="#171413",
    font=("Neuton Bold", 32 * -1),
)

canvas.create_text(
    545.0,
    60.00000000000006,
    anchor="nw",
    text="Select image:",
    fill="#171413",
    font=("Neuton Bold", 32 * -1),
)

canvas.create_text(
    89.0,
    569.0,
    anchor="nw",
    text="www.github.com/theviking733n",
    fill="#FFFFFF",
    font=("Neuton Regular", 20 * -1, "bold"),
)

canvas.create_text(
    26.0,
    277.00000000000006,
    anchor="nw",
    text="To hide your secret text, select an",
    fill="#FFFFFF",
    font=("Neuton Regular", 26 * -1),
)

canvas.create_text(
    23.0,
    313.00000000000006,
    anchor="nw",
    text=" image (jpg or png) and a text file,",
    fill="#FFFFFF",
    font=("Neuton Regular", 26 * -1),
)

canvas.create_text(
    23.0,
    355.00000000000006,
    anchor="nw",
    text=" and then click on Hide",
    fill="#FFFFFF",
    font=("Neuton Regular", 26 * -1),
)

canvas.create_text(
    23.0,
    432.00000000000006,
    anchor="nw",
    text="To get your text back, select the",
    fill="#FFFFFF",
    font=("Neuton Regular", 26 * -1),
)

canvas.create_text(
    23.0,
    472.00000000000006,
    anchor="nw",
    text="output image file and click on Unhide",
    fill="#FFFFFF",
    font=("Neuton Regular", 26 * -1),
)


# Creating buttons
buttonFont1 = font.Font(family="Helvetica", size=20, weight="bold")
buttonFont2 = font.Font(family="Helvetica", size=35, weight="bold")

btn1 = customtkinter.CTkButton(
    master=window,
    text="Browse",
    command=browse_inp_image,
    height=45,
    width=30,
    corner_radius=30,
    text_font=buttonFont1,
)
btn1.configure(
    bg_color="#FBEBCE", fg_color="#3A7FF6", hover_color="#3A59F6", text_color="white"
)
btn1.place(x=760, y=55)

btn2 = customtkinter.CTkButton(
    master=window,
    text="Browse",
    command=browse_inp_text,
    height=45,
    width=30,
    corner_radius=30,
    text_font=buttonFont1,
)
btn2.configure(
    bg_color="#FBEBCE", fg_color="#3A7FF6", hover_color="#3A59F6", text_color="white"
)
btn2.place(x=760, y=155)

btn3 = customtkinter.CTkButton(
    master=window,
    text="HIDE",
    command=hide_button,
    height=65,
    width=250,
    corner_radius=30,
    text_font=buttonFont2,
)
btn3.configure(
    bg_color="#FBEBCE", fg_color="#09db48", hover_color="#00AA00", text_color="white"
)
btn3.place(x=620, y=250)

btn4 = customtkinter.CTkButton(
    master=window,
    text="Browse",
    command=browse_out_image,
    height=45,
    width=30,
    corner_radius=30,
    text_font=buttonFont1,
)
btn4.configure(
    bg_color="#FBEBCE", fg_color="#3A7FF6", hover_color="#3A59F6", text_color="white"
)
btn4.grid(padx=760, pady=405)

btn5 = customtkinter.CTkButton(
    master=window,
    text="UNHIDE",
    command=unhide_button,
    height=65,
    width=250,
    corner_radius=30,
    text_font=buttonFont2,
)
btn5.configure(
    bg_color="#FBEBCE", fg_color="#09db48", hover_color="#00AA00", text_color="white"
)
btn5.place(x=620, y=490)


window.mainloop()
