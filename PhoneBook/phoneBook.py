#!/usr/bin/python
#
# phoneBook.py implements a simple phone book application
# It uses a dictionary implemented as described below.
#
# If the class is in file 'MyDictionary.py', import as follows:
# 
#from MyDictionary import Dictionary
#
# Three dictionary implementations (for test purposes) are
# delivered in this bundle. Uncomment one to use it or
# import your own

#from BuiltIn import Dictionary
#from LinList import Dictionary
#from BinList import Dictionary
from BSTree import Dictionary
#
# Make sure the dictionary implementation follows this API
#________________________________________________________
# # Name of class MUST be Dictionary
# class Dictionary:
#
#     # Initialize dictionary
#     def __init__(self):
#
#     # Insert value having key (returns None)
#     def insert(self, key, value):
#
#     # Delete value having key (returns None)
#     def delete(self, key):
# 
#     # Return value having key, returns None if
#     # key is not found
#     def find(self, key):
#
#     # for every value v apply f(v) exactly once
#     # (returns None)
#     def traverse(self, f):
#
#     # Returns string representation of dictionary
#     def __str__(self):
#________________________________________________________
#
#########################################################
#
# Anything below this point is dangerous to change
# MODIFY AT YOUR OWN RISK!
#
#########################################################

from Tkinter import *
import time
import tkFileDialog
import tkMessageBox
import tkFont
import random

class PhoneApp:

    def __init__(this):
        this.__isChanged = False
        this.__nameDic   = Dictionary()
        this.__phoneDic  = Dictionary()
        this.__root      = Tk()
        this.__root.title("Phone Book")
        menubar          = Menu(this.__root)
        fileMenu         = Menu(menubar, tearoff=0)
        fileMenu.add_command(label="New Dictionary", command=this.__doNew)
        fileMenu.add_command(label="Open Dictionary", command=this.__doOpen)
        fileMenu.add_command(label="Save Dictionary", command=this.__doSave)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=this.__doExit)
        this.__root.protocol("WM_DELETE_WINDOW", this.__doExit)
        menubar.add_cascade(label="File", menu=fileMenu)
        opsMenu          = Menu(menubar, tearoff=0)
        opsMenu.add_command(label="Insert", command=this.__doInsert)
        opsMenu.add_command(label="Delete", command=this.__doDelete)
        opsMenu.add_command(label="Find", command=this.__doFind)
        opsMenu.add_separator()
        opsMenu.add_command(label="List All", command=this.__doListAll)
        opsMenu.add_command(label="Test", command=this.__doTest)
        menubar.add_cascade(label="Operations", menu=opsMenu)
        menubar.add_command(label="About", command=this.__doAbout)
        this.__root.config(menu=menubar)
        Button(this.__root, width=6, text="Insert", command=this.__doInsert).grid(row=0, column=0)
        Button(this.__root, width=6, text="Delete", command=this.__doDelete).grid(row=1, column=0)
        Button(this.__root, width=6, text="Find", command=this.__doFind).grid(row=2, column=0)
        Label(this.__root, text="Name: ").grid(row=0, column=1, sticky=W)
        Label(this.__root, text="Phone number: ").grid(row=1, column=1, sticky=W)
        this.__nameEntry  = Entry(this.__root, width=30)
        this.__nameEntry.grid(row=0, column=2, sticky=W)
        this.__phoneEntry = Entry(this.__root, width=20)
        this.__phoneEntry.grid(row=1, column=2, sticky=W)
        this.__msgLbl    = StringVar()
        this.__msgLbl.set("")
        Label(this.__root, textvariable=this.__msgLbl).grid(row=3, column=0, columnspan=3)
        this.__timeLbl   = StringVar()
        this.__timeLbl.set("")
        Label(this.__root, textvariable=this.__timeLbl).grid(row=2, column=1, columnspan=2)
        this.__root.mainloop()
        

    def __doInsert(this):
        t_b = time.clock()
        this.__msgLbl.set("")
        name = this.__nameEntry.get()
        nbr  = this.__phoneEntry.get()
        if name == '' or nbr == '':
            this.__msgLbl.set("One or more entry is empty. Nothing inserted!")
        else:
            if this.__nameDic.find(name):
                this.__msgLbl.set(str(name)+" already exists!!")
            elif this.__phoneDic.find(nbr):
                this.__msgLbl.set(str(nbr)+" already exists!!")
            else:
                p = Person(name, nbr)
                this.__nameDic.insert(name, p)
                this.__phoneDic.insert(nbr, p)
                this.__isChanged = True
        t_f = time.clock()
        this.__timeLbl.set("Insert: "+str(t_f-t_b)+" secs")


    def __doDelete(this):
        t_b = time.clock()
        this.__msgLbl.set("")
        name = this.__nameEntry.get()
        nbr  = this.__phoneEntry.get()
        if name == '' and nbr == '':
            this.__msgLbl.set("Both entries are empty. Nothing to delete!")
        else:
            p = None
            if name != '':
                p = this.__nameDic.find(name)
            else:
                p = this.__phoneDic.find(nbr)
            if not p:
                this.__msgLbl.set("Nothing found!")
            else:
                this.__nameDic.delete(p.getName())
                this.__phoneDic.delete(p.getNumber())
                this.__nameEntry.delete(0,len(name))
                this.__phoneEntry.delete(0,len(nbr))
                this.__isChanged = True
        t_f = time.clock()
        this.__timeLbl.set("Delete: "+str(t_f-t_b)+" secs")


    def __doFind(this):
        t_b = time.clock()
        this.__msgLbl.set(" ")
        name = this.__nameEntry.get()
        nbr  = this.__phoneEntry.get()
        if name == '' and nbr == '':
            this.__msgLbl.set("Both entries are empty. Nothing to find!")
        else:
            p = None
            if name != '':
                p = this.__nameDic.find(name)
            else:
                p = this.__phoneDic.find(nbr)
            if not p:
                p = Person('', '')
                this.__msgLbl.set("Nothing found!")
            this.__nameEntry.delete(0,len(name))
            this.__phoneEntry.delete(0,len(nbr))
            this.__nameEntry.insert(END, p.getName())
            this.__phoneEntry.insert(END, p.getNumber())
        t_f = time.clock()
        this.__timeLbl.set("Find: "+str(t_f-t_b)+" secs")


    def __doNew(this):
        t_b = time.clock()
        this.__msgLbl.set(" ")
        if this.__isChanged:
            this.__doSave()
        this.__nameDic   = Dictionary()
        this.__phoneDic  = Dictionary()
        this.__isChanged = False
        this.__nameEntry.delete(0,len(this.__nameEntry.get()))
        this.__phoneEntry.delete(0,len(this.__phoneEntry.get()))
        t_f = time.clock()
        this.__timeLbl.set("New: "+str(t_f-t_b)+" secs")


    def __doRead(this, file):
        name = file.readline()
        while name != '':
            nbr = file.readline()
            p = Person(name[:-1], nbr[:-1])
            this.__nameDic.insert(p.getName(), p)
            this.__phoneDic.insert(p.getNumber(), p)
            name = file.readline()
        file.close()

    def __doOpen(this):
        t_b = time.clock()
        this.__msgLbl.set(" ")
        this.__doNew()
        fileName = tkFileDialog.askopenfilename(parent=this.__root, defaultextension='.phn')
        if fileName != '' and fileName != None:
            this.__doRead(open(fileName, 'r'))
        t_f = time.clock()
        this.__timeLbl.set("Open: "+str(t_f-t_b)+" secs")


    def __writeOnePerson(this, person):
        this.__file.write(person.getName()+'\n')
        this.__file.write(person.getNumber()+'\n')
    
    def __doSave(this):
        t_b = time.clock()
        this.__msgLbl.set(" ")
        fileName = tkFileDialog.asksaveasfilename(parent=this.__root, defaultextension='.phn')
        if fileName != '' and fileName != None:
            this.__file = open(fileName, 'w')
            this.__nameDic.traverse(this.__writeOnePerson)
            this.__file.close()
            this.__isChanged = False
        t_f = time.clock()
        this.__timeLbl.set("Save: "+str(t_f-t_b)+" secs")


    def __doExit(this):
        this.__timeLbl.set(" ")
        this.__msgLbl.set(" ")
        if this.__isChanged:
            if tkMessageBox.askyesno("", "Phone book has changed!\nSave it first?"):
                this.__doSave()
        if tkMessageBox.askyesno("", "Really Quit?"):
            this.__root.quit()


    def __doListAll(this):
        t_b  = time.clock()
        this.__msgLbl.set(" ")
        ListWin(this.__root, this.__nameDic)
        t_f  = time.clock()
        this.__timeLbl.set("List: "+str(t_f-t_b)+" secs")


    def __doTest(this):
        this.__msgLbl.set(" ")
        this.__timeLbl.set(" ")
        TestWin(this.__root)


    def __doAbout(this):
        this.__timeLbl.set(" ")
        this.__msgLbl.set(" ")
        tkMessageBox.showinfo("About PhoneBook", "A Simple Phone Book Application\n(as part of a data structures course)\nby\nBengt J. Nilsson")



class Person:
    def __init__(this, name, number):
        this.__name   = name
        this.__number = number
    def getName(this):
        return this.__name
    def getNumber(this):
        return this.__number
    def __str__(this):
        return "("+str(this.__name)+": "+str(this.__number)+")"


class ListWin(Toplevel):
    def __init__(this, parent, dic):
        Toplevel.__init__(this)
        this.transient(parent)
        sbar = Scrollbar(this)
        sbar.pack(side=RIGHT, fill=Y)
        msg  = Text(this, yscrollcommand=sbar.set)
        msg.pack()
        msg.insert(END, str(dic))
        sbar.config(command=msg.yview)
        Button(this, text="OK", command=this.destroy, default=ACTIVE).pack()
        this.bind("<Return>", this.destroy)
        this.protocol("WM_DELETE_WINDOW", this.destroy)
        this.grab_set()
        this.wait_window(this)


class TestWin(Toplevel):
    def __init__(this, parent):
        Toplevel.__init__(this)
        this.title("Test Dictionary")
        this.transient(parent)
        Label(this, text="Min Size:").grid(row=0, column=0, sticky=W)
        this.__min = Entry(this, width=8)
        this.__min.grid(row=0, column=1)
        Label(this, text="Max Size:").grid(row=0, column=2, sticky=W)
        this.__max = Entry(this, width=8)
        this.__max.grid(row=0, column=3)
        Label(this, text="Operations:").grid(row=1, column=0, sticky=W)
        this.__ops = Entry(this, width=8)
        this.__ops.grid(row=1, column=1)
        Button(this, text="Calculate...", command=this.__ok, default=ACTIVE).grid(row=1, column=5, sticky=E)
        this.__msgVar = StringVar()
        this.__pLbl = Label(this, textvariable=this.__msgVar)
        this.__pLbl.grid(row=2, column=0, columnspan=6)
        font = tkFont.Font(family="Fixedsys", size=12, weight=tkFont.NORMAL)
        this.__msgVar.set("")
        fr = Frame(this)
        fr.grid(row=3, column=0, columnspan=6)
        sbar = Scrollbar(fr)
        sbar.pack(side=RIGHT, fill=Y)
        this.__resArea = Text(fr, font=font, yscrollcommand=sbar.set)
        this.__resArea.pack()
        sbar.config(command=this.__resArea.yview)
        Button(this, text="Done", command=this.destroy).grid(row=4, column=5, sticky=E)
        this.bind("<Return>", this.__ok)
        this.protocol("WM_DELETE_WINDOW", this.destroy)
        this.bind("<Escape>", this.destroy)
        this.grab_set()
        this.wait_window(this)

    def __calc(this, min, max, ops):
        range = [min, min+(max-min)/4, min+(max-min)/2, min+3*(max-min)/4, max]
        this.__resArea.insert(END, mkblanks(1000,max)+"Size Total(secs): Inserts Deletes   Finds  Avg(msecs): Insert  Delete    Find\n")
        tot = 0
        for i in range:
            tot = tot + i
        tot = tot + len(range)*3*ops
        this.current = 0
        perc  = 0
        for size in range:
            this.__resArea.insert(END, this.__doTest(size, max, ops, tot, 100*this.current/tot))
        this.__resArea.insert(END, '\n')


    def __doTest(this, size, max, ops, total, perc):
        D = Dictionary()
        for i in xrange(size):
            D.insert(str(i), Person(str(i), str(i)))
            this.current = this.current + 1
            if this.current*100/total > perc:
                perc = perc + 1
                this.__msgVar.set("Calculating: "+mkblanks(perc, 100)+str(perc)+"% done")
                this.__pLbl.update()
        randrange = []
        try:
            randrange = random.sample(xrange(size), ops)
        except AttributeError:
            randrange = xrange(ops)
        t_b  = time.clock()
        for i in randrange:
            p = D.find(str(i))
            this.current = this.current + 1
            if this.current*100/total > perc:
                perc = perc + 1
                this.__msgVar.set("Calculating: "+mkblanks(perc, 100)+str(perc)+"% done")
                this.__pLbl.update()
        t_f  = time.clock()
        fnd = t_f - t_b
        t_b  = time.clock()
        for i in randrange:
            D.delete(str(i))
            this.current = this.current + 1
            if this.current*100/total > perc:
                perc = perc + 1
                this.__msgVar.set("Calculating: "+mkblanks(perc, 100)+str(perc)+"% done")
                this.__pLbl.update()
        t_f  = time.clock()
        dlt = t_f - t_b
        t_b  = time.clock()
        for i in randrange:
            D.insert(str(i), Person(str(i), str(i)))
            this.current = this.current + 1
            if this.current*100/total > perc:
                perc = perc + 1
                this.__msgVar.set("Calculating: "+mkblanks(perc, 100)+str(perc)+"% done")
                this.__pLbl.update()
        t_f  = time.clock()
        ins = t_f - t_b
        strins = (str(ins)+'000000')[:6]
        strdlt = (str(dlt)+'000000')[:6]
        strfnd = (str(fnd)+'000000')[:6]
        avgins = (str(1000*ins/ops)+'000000')[:6]
        avgdlt = (str(1000*dlt/ops)+'000000')[:6]
        avgfnd = (str(1000*fnd/ops)+'000000')[:6]
        return mkblanks(size,max)+mkblanks(max,"Size")+str(size)+'  ops='+\
               mkblanks(ops,"(secs)")+str(ops)+\
               mkblanks(strins,": Inserts")+strins+\
               mkblanks(strdlt," Deletes")+strdlt+\
               mkblanks(strfnd,"   Finds")+strfnd+\
               mkblanks(avgins,"  Avg(msecs): Insert")+avgins+\
               mkblanks(avgdlt,"  Delete")+avgdlt+\
               mkblanks(avgfnd,"    Find")+avgfnd+'\n'

    def __ok(this):
        err = False
        try:
            max = int(this.__max.get())
            min = int(this.__min.get())
            ops = int(this.__ops.get())
        except ValueError:
            err = True
        this.__msgVar.set("")
        this.__pLbl.update()
        if not err and max >= min and min >= ops and ops >= 1:
            this.__calc(min, max, ops)
        elif not err and max >= min:
            tkMessageBox.showinfo("", "Error: More operations than min value or operations < 1!")
        elif not err:
            tkMessageBox.showinfo("", "Error: max value is smaller than min value!")
        else:
            tkMessageBox.showinfo("", "Error: One or more value is not integer!")




def mkblanks(v, max):
    if len(str(v)) >= len(str(max)):
        return ''
    else:
        return ' ' + mkblanks(' '+str(v), str(max))


def askyesno(win, title, message):
    r.result = False
    YesNoWin(win, title, message, r)
    return r.result

class YesNoWin(Toplevel):
    def __init__(this, parent, title, message, r):
        Toplevel.__init__(this)
        this.transient(parent)
        this.title(title)
        this.bind("<Return>", this.__yes)
        this.bind("<Escape>", this.__no)
        this.protocol("WM_DELETE_WINDOW", this.__no)
        Label(this, text="Phone book has changed!").grid(row=0, column=0, columnspan=2)
        Button(this, text="Yes", command=this.__yes).grid(row=2, column=0)
        Button(this, text="No", command=this.__no).grid(row=2, column=1)
        this.grab_set()
        this.res = r
        this.wait_window(this)
    def __yes(this):
        this.res.result = True
        this.destroy()
    def __no(this):
        this.res.result = False
        this.destroy()


app = PhoneApp()
