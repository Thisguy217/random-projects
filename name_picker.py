from tkinter import *

root=Tk()
root.title("Parent Name Generator")
root.geometry("340x100")

def synthesize(list1,list2):
	name_mom=open(list1,'r')
	name_dad=open(list2,'r')

	names_maternal=[]
	for line in name_mom:
		names_maternal.append(line.strip())

	names_paternal=[]
	for line in name_dad:
		names_paternal.append(line.strip())

	agreed_names=[]
	for x in names_maternal:
		for y in names_paternal:
			if x==y:
				agreed_names.append(x)

	agreed=open("agreed.txt",'w')
	for element in agreed_names:
		agreed.write(element+"\n")
	agreed.close()

mom=Label(root,text="Enter file for Parent 1").grid(row=0,column=0)
dad=Label(root,text="Enter file for Parent 2").grid(row=1,column=0)

mom_side=Entry(root)
dad_side=Entry(root)

mom_side.grid(row=0,column=1)
dad_side.grid(row=1,column=1)

function=Button(root,text="Compile Names",command=lambda:synthesize(mom_side.get(),dad_side.get())).grid(row=2,column=0,columnspan=2)

root.mainloop()
