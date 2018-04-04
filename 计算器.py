from tkinter import *
#计算器的重置机制
reset=True
#计算器功能的主要实现
def buttonCallBack(event):
    global label
    global reset
    num=event.widget['text']
    #当按钮为C的时候，重置为0
    if num=='C':
        label['text']="0"
        return
    #当按钮为=的时候，eval计算字符串转化成的计算结果并显示
    if num in "=":
        label['text']=str(eval(label['text']))
        reset=True
        return
    s=label['text']
    #如果字符串是0，则开始新的操作
    if s=='0':
        s=""
        reset=False
    #最后label显示字符串叠加
    label['text']=s+num
#窗口
root=Tk()
#标题
root.wm_title("最简单计算器")
#显示设置1
label=Label(root,text="0",background="white",anchor="e")
label['width']=35
label['height']=2
label.grid(row=1,columnspan=3,sticky=W)
#按钮设置和排布
showText="7894561230C/-+*"
#j横向i纵向设置一个5*3的格局
for i in range(5):
    for j in range(3):
        #b的初始化
        b=Button(root,text=showText[i*3+j],width=10)
        #自动布局
        b.grid(row=i+2,column=j)
        #Button按钮响应
        b.bind("<Button-1>",buttonCallBack)
#设置按钮=
b=Button(root,text="=")
b.grid(row=8,columnspan=3,sticky="we")
b.bind("<Button-1>",buttonCallBack)
root.mainloop()