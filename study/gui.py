import tkinter as tk

root = tk.Tk()

#lable
label1 = tk.Label(root, text = "用户名:")
label1.grid(row = 0, column = 0)
label2 = tk.Label(root, text = "密 码:")
label2.grid(row = 1, column = 0)
#输入框
entry1 = tk.Entry(root)
entry1.grid(row = 0, column = 1)
entry2 = tk.Entry(root)
entry2.grid(row = 1, column = 1)
#复选框
checkbutton = tk.Checkbutton(root, text = "记住密码")
checkbutton.grid(row = 2, column = 0, rowspan = 1, columnspan = 2, sticky=tk.W)  #sticky设置控件的对其方位，这里设置为靠西(左西右东)
#
# img = tk.PhotoImage(file = "/image/image_test.png")
# imageview = tk.Label(root, image= img)
# imageview.grid(row = 0, column = 2, rowspan = 2, columnspan = 2)
#
button1 = tk.Button(root, text = "登 录")
button1.grid(row = 2, column = 2)
button1 = tk.Button(root, text = "退 出")
button1.grid(row = 2, column = 3)
root.mainloop()