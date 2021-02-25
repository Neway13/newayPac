from PIL import ImageGrab
from tkinter import *
import easygui


import sys
import os
import time
import tkinter
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
    dirs=rootDir+time.strftime("%Y_%m_%d", time.localtime())
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    if filename == '' :
        filename=str(time.time())
    fname=dirs+'\\'+filename+'.png'
    if os.path.exists(fname):
        alert("文件已经存在，请重新输入！")
        return False  
    image = ImageGrab.grabclipboard() # 获取剪贴板文件
    image.save(fname)
    runCMD("cd /d "+rootDir+" && git add * && git commit -m  ':)' && git push &&  exit")
    
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
# 执行cmd
def runCMD(cmd, mode="r", buffering=-1):
    if not isinstance(cmd, str):
        raise TypeError("invalid cmd type (%s, expected string)" % type(cmd))
    if mode not in ("r", "w"):
        raise ValueError("invalid mode %r" % mode)
    if buffering == 0 or buffering is None:
        raise ValueError("popen() does not support unbuffered streams")
    import subprocess, io
    if mode == "r":
        proc = subprocess.Popen(cmd,
                                shell=True,
                                stdout=subprocess.PIPE,
                                bufsize=buffering)
        return _wrap_close(io.TextIOWrapper(proc.stdout), proc)
    else:
        proc = subprocess.Popen(cmd,
                                shell=True,
                                stdin=subprocess.PIPE,
                                bufsize=buffering)
        return _wrap_close(io.TextIOWrapper(proc.stdin), proc)
openDialog()
