# encoding: utf-8

import pyaes
import hashlib
from Tkinter import *
import tkMessageBox
import os


def create_directory():
	try:
		os.makedirs(home+".jpass")
		os.makedirs(home+".jpass/safe_pass")
		os.makedirs(home+".jpass/tmp")
	except Exception as erro:
		None

def register():
	try:
		create_directory()
		hash = hashlib.sha256(key).hexdigest()
		password = str(hash[1])+str(hash[5])+str(hash[2])+str(hash[18])+str(hash[12])+str(hash[3])+str(hash[20])+str(hash[31])+str(hash[16])+str(hash[10])+str(hash[27])+str(hash[29])+str(hash[45])+str(hash[32])+str(hash[1])+str(hash[0])


		aes = pyaes.AESModeOfOperationCTR(password)
		file = open(home+".jpass/very.pg", 'w')
		msg = aes.encrypt(hash)
		file.write(msg)
		file.close()

		tkMessageBox.showinfo("info", 'Successfull')
		exit(0)

	except Exception as erro:
		tkMessageBox.showinfo("error",str(erro))



def get_pass():
        global key

        key = e1.get()
        conf_key = e2.get()

        if key != conf_key:
                tkMessageBox.showinfo("info","Password dont match !")

        else:
		if len(key) < 8:
			tkMessageBox.showinfo("info","Very short password, minimum 8 characters")
		else:
			register()


if os.getlogin == 'root':
	print "Dont run as root"
	exit(0)

global home
home = "/home/"+str(os.getlogin())+'/'

master = Tk()
Label(master, text="Password").grid(row=0)
Label(master, text="Re-Password").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master,text='Quit',command=master.quit).grid(row=3, column=0,sticky=W, pady=4)
Button(master,text='Install', command=get_pass).grid(row=3,column=1, sticky=W, pady=4)

mainloop()

