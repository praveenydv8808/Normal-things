from tkinter import*
from  tkinter import ttk
from  tkinter import filedialog
from pytube import  YouTube

Folder_Name=" "
#File Location
def OpenLoaction():
    global Folder_Name
    Folder_Name=filedialog.askdirectory()
    if(len(Folder_Name)>1):
        YError.config(text=Folder_Name,fg="green")
    else:
        YError.config(text="Please Select the Folder",fg="Red")

#Download Function
def Downloadvideo():
    choise=Ychoices.get()
    url=YEntry.get()

    if(len(url)>1):
        YError.config(text="")
        yt=YouTube(url)
        if(choise==choices[0]):
            select=yt.streams.filter(progressive="True").first()
        elif(choise==choices[1]):
            select=yt.streams.filter(progressive="True",file_extension="mp4").last()
        elif(choise==choices[2]):
            select=yt.streams.filter(only_audio="True").first()
        else:
            YError.config(text="Paste link again..!!",fg="red")

    #download Function
    select.download(Folder_Name)
    YError.config(text="Download Completed!!")





root=Tk()
root.title("Youtube Downloader")
root.geometry("360x400")
root.columnconfigure(0,weight=1)

#youtube lable
YLable=Label(root,text="Enter the Youtube video Link",font=("jost",15))
YLable.grid()

#Enter the Link
YEntryVar=StringVar()
YEntry=Entry(root,width=50,textvariable=YEntryVar)
YEntry.grid()

#Error
YError =Label(root,text=" ",fg="red",font=("Jost",10))
YError.grid()

#Asking for Saving file
SaveFile=Label(root,text="Save the file",font=("jost",15,"bold"))
SaveFile.grid()

#Btn for saving file
SaveEntry=Button(width=10,text="choose path",bg="blue",fg="white",command=OpenLoaction)
SaveEntry.grid()

#Video quality
YQuality=Label(root,text="select Quality",font=("jost",15))
YQuality.grid()

#Select Quality
choices=["144p","720p","Only Audio"]
Ychoices=ttk.Combobox(root,value=choices)
Ychoices.grid()

#Download Btn
YDownload=Button(root,width=10,bg="blue",text="Download",fg="white",command=Downloadvideo)
YDownload.grid()

Devloper=Label(text="Powerd By Monster_Satya",fg="Red")
Devloper.grid()
root.mainloop()
