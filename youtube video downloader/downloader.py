from pytube import YouTube
from tkinter import *


window = Tk()
window.geometry("640x480")
window.title("YouTube Video Downloader")

background = PhotoImage(file="back.png")
background_label = Label(window, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

Label(window, text="Youtube Video Downloader", font=("Comic sans ms", "20", "normal"), bg= "#191970", fg = "red").pack(padx=10, pady=10)

logo = PhotoImage(file="youtube.png")
window.iconphoto(False, logo)

video_link = StringVar()

Label(window, text="Enter the link of the video : ", font=("Comic sans ms", "15", "normal"), bg= "#191970", fg = "red").pack(padx=10, pady=10)


entry_field = Entry(window, width = 30,font = 35, textvariable=video_link, bg="#191970", fg="red").place(x=150, y=125)

def video_download():
    try:
        yt = YouTube(str(video_link.get())) 
        video = yt.streams.first()
        video.download()
        
        Label(window, text="Video Downloaded Successfully", font=("Comic sans ms", "15", "normal"), bg= "#191970", fg = "red").pack(padx=100, pady=100)

    except Exception as e:
        Label(window, text="Don't waste my time you moron!!", font=("Comic sans ms", "15", "normal"), bg= "#191970", fg = "red").pack(padx=100, pady=100)
        print(e)
        print("Error")  

Button(window, text="Download", font=("Comic sans ms", "15", "normal"), bg= "#191970", fg = "red", command=video_download).place(x=260, y=150)

window.mainloop()






















# Created By ABHISHEK SRIVASTAVA

