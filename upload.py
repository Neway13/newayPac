from PIL import ImageGrab
from tkinter import *
import easygui


import sys
import os
import time
import tkinter
import pyperclip 
rootDir='C:\\document\\IdeaProjects\\newaycdn\\'
def openDialog():
    win=tkinter.Tk()
    win.title("Image Name")
    win.geometry('200x100') #是x 不是*
    l1 = Label(win, text="文件名（为空用时间戳）：")
    l1.pack() #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
    filename_entry=tkinter.Entry(win, bg="white",fg="black")
    #entry1=tkinter.Entry(win,show="*",width=50,bg="red",fg="black")
    filename_entry.pack()
    button=tkinter.Button(win,text="确定",command=lambda:go(win,filename_entry)) #收到消息执行这个函数
    button.pack()#加载到窗体，
    win.mainloop()
    
def  go(win,filename_entry):
    result=savePic(filename_entry.get())    #获取文本框的内容
    if result == False:
        return
    win.quit()
    win.destroy()
    
def savePic(filename) :
    dirname=time.strftime("%Y_%m_%d", time.localtime())
    dir=rootDir+dirname
    if not os.path.exists(dir):
        os.makedirs(dir)
    if filename == '' :
        filename=str(time.time())
    fname=dir+'\\'+filename+'.png'
    if os.path.exists(fname):
        alert("文件已经存在，请重新输入！")
        return False  
    image = ImageGrab.grabclipboard() # 获取剪贴板文件
    image.save(fname)
    os.system("cd /d "+rootDir+" && git add * && git commit -m  ':)' && git push &&  exit")
    pyperclip.copy("https://cdn.jsdelivr.net/gh/Neway13/newaycdn/"+dirname+"/"+filename+".png")
              
def alert(str):
    win=tkinter.Tk()
    win.title("Save Image")
    win.geometry('200x100') #是x 不是*
    l1 = Label(win, text=str)
    l1.pack() #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
    button=tkinter.Button(win,text="确定",command=lambda: exitTk(win)) #收到消息执行这个函数
    button.pack()#加载到窗体，
    win.mainloop()
    
def  exitTk(win):      #关闭窗口
    win.quit()
    win.destroy()
 
openDialog()
