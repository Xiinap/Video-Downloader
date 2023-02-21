'''
CN version
'''
from pytube import YouTube
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry('600x400')
root.title('YouTube video download')
root["bg"] = 'black'


def start():

   def info():
      win = Tk()
      win.geometry('400x170')
      win.title('YouTube video download | 如何使用')
      win["bg"] = 'white'

      Label(win, text='如何使用程序 ', bg='white', font=('Times', 20)).pack()

      Label(win, text='1. 在相应的字段中输入链接           \n2. 单击“检查链接”按钮          \n3. 选择高质量或低质量             \n         （高品质 - 最大, \n             低质量 - 最小(144р))\n4. 该文件将与文件一起保存在文件夹中                   \n\n!如果输入错误的链接，程序可能会关闭！', bg='white', font=('Times', 10)).pack()


      win.mainloop()

   def show_message():

      def low():
         messagebox.showinfo('下载开始', '下载开始\n关闭此窗口\n质量：低', icon='question')
         output = video.streams.get_lowest_resolution()
         output.download()
         messagebox.showinfo('加载完成', '加载完成\n该文件保存在程序文件夹中')

      def high():
         messagebox.showinfo('下载开始', '下载开始\n关闭此窗口\n质量：高', icon='question')
         output = video.streams.get_highest_resolution()
         output.download()
         messagebox.showinfo('加载完成', '加载完成\n该文件保存在程序文件夹中')

      link = entry.get()
      video = YouTube(link)
      if video == YouTube(link):

         Label(self, text='选择品质: ', bg='black', fg='white', font=('Times', 15)).place(x=10, y=175)


         high_btn = Button(self, text='高质量', relief='flat', bg='black', fg='green', font=('Times', 15), command=high)
         high_btn.place(x=30, y=205)

         low_btn = Button(self, text='低质量', relief='flat', bg='black', fg='crimson', font=('Times', 15), command=low)
         low_btn.place(x=230, y=205)
      else:
         messagebox.showerror('错误！', '错误！ \n链接无效')

      print(video)
      print(entry.get())

   root.destroy()
   self = Tk()
   self.geometry('600x400')
   self.title('YouTube video download')
   self["bg"] = 'black'

   ready_btn = Button(self, text='查看\n关联', relief='flat', bg='black', fg='white', font=('Times', 15),
                      command=show_message)
   ready_btn.place(x=470, y=100)
   ready_btn["border"] = "0"

   how_use_btn = Button(self, text='如何使用', relief='flat', bg='black', fg='blue', font=('Times', 15),
                        command=info)
   how_use_btn.place(x=10, y=352)
   how_use_btn["border"] = "0"

   Button(self, text='Выйти', relief='flat', bg='black', fg='red', font=('Times', 15),
                        command=self.destroy).place(x=515, y=350)


   Label(self, text='输入视频链接: ', bg='black', fg='white', font=('Times', 15)).place(x=10, y=100)

   label = Label(self, text=" YouTube video downloader", bg='black', fg='white', font=('Times', 35))
   label.place(x=25, y=10)

   label1 = Label(self, text=" YouTube", bg='black', fg='red', font=('Times', 35))
   label1.place(x=25, y=10)


   entry = ttk.Entry(self, width=70)
   entry.place(x=5, y=130)



   self.mainloop()

#button
loadimage = PhotoImage(file="image.png")
btn = Button(root, image=loadimage, relief='flat', bg='black', command=start)
btn.place(x=115, y=200)
btn["border"] = "0"

#labels
label = Label(root, text=" YouTube video downloader", bg='black', fg='white', font=('Times', 35))
label.place(x=25, y=100)

label1 = Label(root, text=" YouTube", bg='black', fg='red', font=('Times', 35))
label1.place(x=25, y=100)



root.mainloop()

