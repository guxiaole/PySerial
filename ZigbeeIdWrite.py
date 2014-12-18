#!/usr/bin/env python

from Tkinter import *
import tkFont
from tkMessageBox import askquestion,showerror,showinfo
from functools import partial
import serial
import binascii
from serial.tools.list_ports import comports
def Write_to_sreial(EdNetID,EdNodeID,com):
	#init serial
	ser=serial.Serial(com)
	ser.baudrate=38400
	#ser.open()
	Openflag=False
        Openflag=ser.isOpen()

	sendData="FF"+EdNetID.get()+EdNodeID.get()


	if Openflag==True: 
		MessageBoxResult=askquestion("Wrte to ROMs","Are you want to Write the ID")
		if MessageBoxResult=='yes':
			#data2int=int(sendData)
			Hexdata=binascii.b2a_hex(sendData)  
			print Hexdata
			Hexdata=Hexdata.decode("hex")

			#print type(Hexdata)
			#Hexdata=hex(data2int)
			#Hexdata=hex(sendData)
			#ser.writelines('\xFF')
			ser.write(Hexdata)
			ser.close()
			print  sendData
			#print  data2int
			print  Hexdata
			showinfo("","done")
		else:
			pass
	else:
		showerror("","fail to open com")

def main():
	top=Tk()
	top.title("Zigbee_IDReader")
	top.resizable(0,0)

	Label(top,text=" NetID:").grid(row=0,sticky=E)
	Label(top,text="NodeID:").grid(row=1,sticky=E)
	#e1 = Entry(top)
	#e2 = Entry(top)
	#e1.grid(row=0, column=1)
	#e2.grid(row=1, column=1)

	entry_font = tkFont.Font(size=12)
	EdNetID=Entry(top,font=entry_font)
	EdNodeID=Entry(top,font=entry_font)
	EdNetID.grid(row=0,column=1, columnspan=4,sticky=E,padx=5,pady=5)
	EdNodeID.grid(row=1,column=1,columnspan=4,sticky=E,padx=5,pady=5)
	
        if comports:
		for port, desc, hwid in sorted(comports()):
			com=port
	
        print com
	WriteButton=Button(top,text="Write",command=lambda: Write_to_sreial(EdNetID,EdNodeID,com))
	WriteButton.grid(row=2,column=2)
	mainloop()


if __name__=='__main__':
	main()
