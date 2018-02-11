''' Currency Converter, made using tkinter,requests,BeautifulSoup 
    (converting values imported from GoogleFinance. 
    ALWAYS CHECK FOR UPDATES IN HTML CODE FOR THE CODE TO WORK)  '''

import tkinter as tk
import requests 
from bs4 import BeautifulSoup

''' 
first, gets two lists:
    - currencies,       where the name of the currencies are stored
    - currencies_tags,  where the tags used by the site to point to the
                        currencies are stored
'''
    
r=requests.get("https://www.google.com/finance/converter?a=1&from=BAM&to=BMD&meta=ei%3Dc--3WenQO4LAsQH3kKrIAg")
c=r.content
soup=BeautifulSoup(c,"html.parser")
all=soup.find_all("div")
all=all[0].find_all("div")[1].find_all("option")

currencies=[]
currencies_tags=[]
for item in all:
    currencies.append(item.text)
    currencies_tags.append(item['value'])
    
# now creates the main window

class MainApplication(tk.Frame):
    
    def __init__(self,parent): 
        
        tk.Frame.__init__(self,parent)
        
        def convert():
            f=currencies_tags[self.from_curr]
            t=currencies_tags[self.to_curr]
            if f!=t and type(self.e1_in.get()) in [float,int]:
                    r_n=requests.get(
                            "https://finance.google.com/finance/converter?a=1&from=%s&to=%s&meta=ei%%3Durq7WfnFL47usQGCg7KYCQ"%(f,t))
                    c_n=r_n.content
                    soup_n=BeautifulSoup(c_n,"html.parser")
            
                    all_n=soup_n.find_all("div")[-1]
                    ratio=float(
                            all_n.find_all("span",{"class":"bld"})[0].text.split()[0])
                    self.l2_in.set(round(self.e1_in.get()*ratio,5))
               
        def set_from(i):
            self.from_curr=i
            for currency in self.l1:
                currency.set(0)
            self.l1[i].set(1)
            self.mb1_in.set(currencies[i])
            
        def set_to(i):
            self.to_curr=i
            for currency in self.l2:
                currency.set(0)
            self.l2[i].set(1)
            self.mb2_in.set(currencies[i])
            
        self.from_curr=0
        self.to_curr=1
        
        self.mb1_in=tk.StringVar()
        self.mb1_in.set(currencies[self.from_curr])
        self.mb1 = tk.Menubutton(self, textvariable=self.mb1_in, relief="raised")
        self.mb1.grid(row=0,column=1)
        
        self.e1_in=tk.DoubleVar()
        self.e1=tk.Entry(self,textvariable=self.e1_in)
        self.e1.grid(row=0,column=2)
        
        self.mb2_in=tk.StringVar()
        self.mb2_in.set(currencies[self.to_curr])
        self.mb2 = tk.Menubutton(self, textvariable=self.mb2_in, relief= "raised")
        self.mb2.grid(row=1,column=1)
        
        self.l2_in=tk.DoubleVar()
        self.l2=tk.Label(self,textvariable=self.l2_in)
        self.l2.grid(row=1,column=2)
        
        tk.Label(self,text="From").grid(row=0,column=0)
        tk.Label(self,text="To").grid(row=1,column=0)
        
        # creates the two menus
        self.mb1.menu = tk.Menu(self.mb1)
        self.mb1["menu"]=self.mb1.menu
        self.mb2.menu = tk.Menu(self.mb2)
        self.mb2["menu"]=self.mb2.menu
        
        self.l1=[tk.IntVar() for i in range(len(currencies))]
        self.l2=[tk.IntVar() for i in range(len(currencies))]
        for i in range(len(currencies)):
            self.mb1.menu.add_checkbutton(label=currencies[i],
                                          variable=self.l1[i],
                                          command= lambda x=i: set_from(x))
            
            self.mb2.menu.add_checkbutton(label=currencies[i],
                                          variable=self.l2[i],
                                          command= lambda x=i: set_to(x))
            
        self.conv=tk.Button(self,text="Convert",command=convert)
        self.conv.grid(row=2,column=2)

        
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Currency converter")
    MainApplication(root).pack()
    root.mainloop()






