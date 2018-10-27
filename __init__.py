from nsepy import get_history
from datetime import date
from matplotlib import pyplot as plt
sbin = get_history(symbol='SBIN',
                   start=date(2015,1,1),
                   end=date(2015,1,10))

from tkinter import *

root = Tk()
root.geometry("300x200")


from datetime import date
from nsepy import get_history


stock_fut = get_history(symbol="SBIN",
start=date(2015,1,1),
end=date(2015,1,10),
futures=True,
expiry_date=date(2015,1,29))

stock_opt = get_history(symbol="SBIN",
start=date(2015,1,1),
end=date(2015,1,10),
option_type="CE",
strike_price=300,
expiry_date=date(2015,1,29))



nifty_fut = get_history(symbol="NIFTY",
start=date(2015,1,1),
end=date(2015,1,10),
index=True,
futures=True,
expiry_date=date(2015,1,29))

nifty_futo = get_history(symbol="NIFTY",
start=date(2015,1,20),
end=date(2015,1,30),
index=True,
futures=True,
expiry_date=date(2015,1,29))

nifty_futoo = get_history(symbol="NIFTY",
start=date(2015,1,10),
end=date(2015,1,20),
index=True,
futures=True,
expiry_date=date(2015,1,29))

nifty_next50 = get_history(symbol="NIFTY NEXT 50",
start=date(2015,1,1),
end=date(2015,3,13),
index=True)

nifty_next100 = get_history(symbol="NIFTY NEXT 50",
start=date(2015,1,10),
end=date(2015,1,20),
index=True)

nifty_eq_wt = get_history(symbol="NIFTY50 EQUAL WEIGHT",
start=date(2017,6,1),
end=date(2017,6,10),
index=True)

stock_opt[['Close', 'Underlying']].plot(secondary_y="Underlying")


def index1():
    print(nifty_next50)

def onClick():
    print(stock_fut)

def onClick1():
    print(nifty_fut)

def onClick3():
    print(nifty_futo)

def onClick2():
    print(nifty_futoo)


btnSubmit = Button(root,text="Show me weekly stock predictions",command=onClick)
btnSubmit.pack()
btnSubmit = Button(root,text="Show me weekly Nifty predictions",command=onClick1)
btnSubmit.pack()
btnSubmit = Button(root,text="next week Nifty predictions",command=onClick2)
btnSubmit.pack()
btnSubmit = Button(root,text="third week Nifty predictions",command=onClick3)
btnSubmit.pack()
btnSubmit = Button(root,text="index of next 50 nifty",command=index1)
btnSubmit.pack()

root.mainloop()

