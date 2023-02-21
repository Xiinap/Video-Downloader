'''
FR version
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
      win.title('YouTube video download | Как пользоваться')
      win["bg"] = 'white'

      Label(win, text='Comment utiliser le programme ', bg='white', font=('Times', 20)).pack()

      Label(win, text='1. Saisissez le lien dans le champ \n2 approprié. Cliquez sur le bouton "Vérifier le lien" \n3. Choisissez une qualité élevée ou faible\n (Haute qualité - maximum, \n Basse qualité - minimum (144p))\n4. Le fichier sera enregistré dans le dossier avec le fichier \n\n ! Si vous entrez le mauvais lien, le programme peut se fermer !', bg='white', font=('Times', 10)).pack()


      win.mainloop()

   def show_message():

      def low():
         messagebox.showinfo('Téléchargement commencé', 'Téléchargement commencé\nFermer cette fenêtre\nQualité : Faible', icon='question')
         output = video.streams.get_lowest_resolution()
         output.download()
         messagebox.showinfo('Téléchargement terminé', 'Téléchargement terminé\nLe fichier a été enregistré dans le dossier du programme')

      def high():
         messagebox.showinfo('Téléchargement commencé', 'Téléchargement commencé\nFermer cette fenêtre\nQualité : élevée', icon='question')
         output = video.streams.get_highest_resolution()
         output.download()
         messagebox.showinfo('Téléchargement terminé', 'Téléchargement terminé\nLe fichier a été enregistré dans le dossier du programme')

      link = entry.get()
      video = YouTube(link)
      if video == YouTube(link):

         Label(self, text='Sélectionnez la qualité : ', bg='black', fg='white', font=('Times', 15)).place(x=10, y=175)


         high_btn = Button(self, text='Haute qualité', relief='flat', bg='black', fg='green', font=('Times', 15), command=high)
         high_btn.place(x=30, y=205)

         low_btn = Button(self, text='Basse qualité', relief='flat', bg='black', fg='crimson', font=('Times', 15), command=low)
         low_btn.place(x=230, y=205)
      else:
         messagebox.showerror('Erreur !', 'Erreur ! \nLien invalide')

      print(video)
      print(entry.get())

   root.destroy()
   self = Tk()
   self.geometry('600x400')
   self.title('YouTube video download')
   self["bg"] = 'black'

   ready_btn = Button(self, text='Vérifier\nle lien', relief='flat', bg='black', fg='white', font=('Times', 15),
                      command=show_message)
   ready_btn.place(x=470, y=100)
   ready_btn["border"] = "0"

   how_use_btn = Button(self, text='Comment utiliser', relief='flat', bg='black', fg='blue', font=('Times', 15),
                        command=info)
   how_use_btn.place(x=10, y=352)
   how_use_btn["border"] = "0"

   Button(self, text='Sortir', relief='flat', bg='black', fg='red', font=('Times', 15),
                        command=self.destroy).place(x=515, y=350)


   Label(self, text='Entrez le lien vidéo :', bg='black', fg='white', font=('Times', 15)).place(x=10, y=100)

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

