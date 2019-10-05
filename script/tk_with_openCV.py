#!/usr/bin/env python
import Tkinter as tk
from PIL import Image
from PIL import ImageTk
import cv2
import time

class Update_image:
	def __init__(self , parent):
		self.label = tk.Label(parent,text='1')
		self.label.pack()
		self.cap = cv2.VideoCapture(0)
		self.label.after(1000,self.refresh_Label)
	def refresh_Label(self):
		suc , image = self.cap.read()
		if suc:
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			image = Image.fromarray(image)
			image = ImageTk.PhotoImage(image)
			self.label.configure(image=image)
			self.label.image = image
			self.label.after(50, self.refresh_Label)
		else:
			print("trouble")

def main():
	root = tk.Tk()
	root.geometry("800x900")
	update_image = Update_image(root)
	root.mainloop()
if __name__ == '__main__':
  main()
