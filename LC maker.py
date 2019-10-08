from mkmany import print_all
from lc import give_print
import tkinter
from tkinter import *
import pandas
from pandas import *
df=read_csv('dbaa.csv')


m=Tk()

def p_a():
    print_all()

def display(f2):
    for x in range(0,len(df['जनरल रजिस्टर क्र.'])):
        if str(df['जनरल रजिस्टर क्र.'][x])==str(e.get()):
            print(df['आडनाव'][x])
            print(e.get())
            dat={}
            dat['अ. क्र. ']=str(df['अ. क्र. '][x])
            dat['जनरल रजिस्टर क्र.']=str(df['जनरल रजिस्टर क्र.'][x])
            dat['स्टुडंट आय डी']=str(df['स्टुडंट आय डी'][x])
            dat['यु आय डी नं.']=str(df['यु आय डी नं.'][x])
            dat['आडनाव']=str(df['आडनाव'][x])
            dat['नाव ']=str(df['नाव '][x])
            dat['वडिलांचे नाव ']=str(df['वडिलांचे नाव '][x])
            dat['आईचे नाव']=str(df['आईचे नाव'][x])
            dat['राष्ट्रीयत्व']=str(df['राष्ट्रीयत्व'][x])
            dat['मातृभाषा']=str(df['मातृभाषा'][x])
            dat['धर्म']=str(df['धर्म'][x])
            dat['जात']=str(df['जात'][x])
            dat['पोटजात']=str(df['पोटजात'][x])
            dat['जन्मस्थळ']=str(df['जन्मस्थळ'][x])
            dat['तालुका']=str(df['तालुका'][x])
            dat['जिल्हा']=str(df['जिल्हा'][x])
            dat['राज्य']=str(df['राज्य'][x])
            dat['देश']=str(df['देश'][x])
            dat['इ.सनाप्रमाणे जन्मदिनांक']=str(df['इ.सनाप्रमाणे जन्मदिनांक'][x])
            dat['जन्मदिनांक अक्षरी']=str(df['जन्मदिनांक अक्षरी'][x])
            dat['या पूर्वीची शाळा व इयत्ता ']=str(df['या पूर्वीची शाळा व इयत्ता '][x])
            dat['या शाळेत प्रवेश घेतल्याचा दिनांक ']=str(df['या शाळेत प्रवेश घेतल्याचा दिनांक '][x])
            dat['इयत्ता ']=str(df['इयत्ता '][x])
            dat['अभ्यासातली प्रगती']=str(df['अभ्यासातली प्रगती'][x])
            dat['वर्तणूक ']=str(df['वर्तणूक '][x])
            dat['शाळा सोडल्याचा दिनांक']=str(df['शाळा सोडल्याचा दिनांक'][x])
            dat['कोणत्या इयत्तेत शिकत होता व केव्हापासून']=str(df['कोणत्या इयत्तेत शिकत होता व केव्हापासून'][x])
            dat['शाळा सोडण्याचे कारण ']=str(df['शाळा सोडण्याचे कारण '][x])
            dat['शेरा']=str(df['शेरा'][x])
            print(dat)
            lab=Label(f2,text="\n\t"+str(df['आडनाव'][x])+"\n")
            p=Button(f2,text='Print',command=lambda:givecom(dat))
            back=Button(f2,text='Back',command=lambda:goback(f1))
            lab.grid(row=0)
            p.grid(row=1)
            back.grid(row=2)
            f2.tkraise()
            #give_print(dat)

def goback(f1):
    f1.tkraise()

def givecom(dat):
    give_print(dat)

#frame.grid(row=0, column=0, sticky="news")
#frame.tkraise()
f1 = Frame(m)
f1.grid(row=0, column=0, sticky='news')
f2 = Frame(m)
f2.grid(row=0, column=0, sticky='news')
Label(f1,text="Enter G.R.No.").grid(row=0)
e=Entry(f1)
e.grid(row=0,column=1)
b=Button(f1,text='View',command=lambda:display(f2))
b.grid(row=1)
b1=Button(f1,text='Print All',command=lambda:p_a())
b1.grid(row=2)
f1.tkraise()
m.mainloop()
