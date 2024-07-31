from prediction import predictImage
import cv2
from tkinter import *
from tkinter import filedialog
import base64
from PIL import Image, ImageTk



names = {'CNV': "Melanoma", 'DME': "Melanoma", 'drusen': "Retinoblastoma", 'normal': "Normal"}
def browseFiles():
    # global imglabel
    py = r"*jpeg"
    global result
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("images",py),("all files","*.*")))
    # check if file is jpeg
    # if filename.endswith(".jpeg"):
    if filename:
        # predict the image
        img = cv2.imread(filename)
        result = predictImage(img)
        print(result)
        result = names[result]
        output_text.insert(END, result+"\n")
        # Encode image to base64
        _, buffer = cv2.imencode('.jpg', img)
        image_base64 = base64.b64encode(buffer).decode('utf-8')

        img = (Image.open(filename)).resize((100, 100))
        img = ImageTk.PhotoImage(img)
        imglabel.config(image=img)

        

        window.update()
        window.update_idletasks()

        # # send a request to the server http://127.0.0.1:5000
        # import requests
        # url = "http://127.0.0.1:5000/insertInFirestore"
        # # read the image and convert it into bytes 
        # img_name = filename.split("/")[-1]
        # data = {"name":fullname_entry.get(), "age":age_entry.get(), "result":result, "image":image_base64, "img_name":img_name}
        # response = requests.post(url, data=data)
        # print(response.text)

        # select_label.config(text=filename)
    if filename == "":
        return
    
def clear():
    fullname_entry.delete(0, END)
    age_entry.delete(0, END)
    output_text.delete("1.0", END)

window = Tk()

# Set window title
window.title('Eye Cancer Detection')

# Set window size
window.geometry("800x600")

# Set window background color
window.config(background="#F8F9F9")

# Create label for title
title_label = Label(window, text="Eye Cancer Detection", font=("Helvetica", 22, "bold"), fg="#17202A", bg="#F8F9F9")
title_label.place(relx=0.5, rely=0.1, anchor=CENTER)

# Create label for full name
fullname_label = Label(window, text="Full Name", font=("Helvetica", 14), fg="#2C3E50", bg="#F8F9F9")
fullname_label.place(x=200, y=180)

# Create text box for full name
fullname_entry = Entry(window, font=("Helvetica", 12), bg="#EAECEE", bd=0, highlightthickness=0)
fullname_entry.place(x=320, y=180, width=250, height=30)

# Create label for age
age_label = Label(window, text="Age", font=("Helvetica", 14), fg="#2C3E50", bg="#F8F9F9")
age_label.place(x=200, y=240)

# Create text box for age
age_entry = Entry(window, font=("Helvetica", 12), bg="#EAECEE", bd=0, highlightthickness=0)
age_entry.place(x=320, y=230, width=250, height=30)

# Create "Browse Files" button
browse_button = Button(window, text="Browse Files", font=("Helvetica", 14), fg="#FFFFFF", bg="#27AE60", bd=0, highlightthickness=0, activebackground="#2ECC71", cursor="hand2", command=browseFiles)
browse_button.place(x=300, y=300, width=150, height=40)



select_label = Label(window, text="(Select an image)", font=("Helvetica", 10), fg="#2C3E50", bg="#F8F9F9")
select_label.place(x=310, y=270) 
# Create output label and text box
output_label = Label(window, text="Output:", font=("Helvetica", 12, "bold"), bg="white")
output_label.place(x=100, y=360)
output_text = Text(window, font=("Helvetica", 12), width=10, height=5)
output_text.place(x=100, y=380)

imglabel = Label(window)
imglabel.place(x=200, y=380, width=100, height=100)

clear_btn = Button(window, text="Clear", font=("Helvetica", 14), fg="#FFFFFF", bg="#27AE60", bd=0, highlightthickness=0, activebackground="#2ECC71", cursor="hand2", command=clear)
clear_btn.place(x=300, y=500)
# call addDataToDatabase function when button is clicked
# button1.config(command=addDataToDatabase)
window.mainloop()
