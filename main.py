from tkinter import *
import qrcode

global i
i=1

def generate():
    img = qrcode.make(link_var.get())
    img.save("qr.png")
    qr_photoimage.config(file="qr.png")

root = Tk()

root.resizable(False,False)
root.title("QR Code Generator")
root.geometry("500x500")

link_var = StringVar()

link_entry = Entry(root, text=link_var, width=50)
link_entry.pack(pady=15)

generate_btn = Button(root, text="Generate QR Code", width=25, command=generate)
generate_btn.pack(pady=20)

qr_photoimage = PhotoImage()

qr_label = Label(root, image=qr_photoimage)
qr_label.pack(pady=25)

root.mainloop()
