from tkinter import *

class win:
    ''' The main window of the game with the relative number '''
    def __init__(self,player_count):
        self.window=Tk()
        self.window.title("Yathzee!!!")
        window=self.window
        
        # first column
        
        d=dict([(1,'Aces'),(2,'Twos'),(3,'Threes'),(4,'Fours'),(5,'Fives'),(6,'Sixes')])
        
        Label(window,text="UPPER SECTION").grid(row=0,column=0)
        
        for r in range(1,7):
            Label(window,text='%s'%d[r]).grid(row=r,column=0)
            
        Label(window,text="TOTAL OF DICES").grid(row=7,column=0,columnspan=2)
        Label(window,text="BONUS").grid(row=8,column=0)
        Label(window,text="TOTAL OF UPPER SECTION:").grid(row=9,column=0,columnspan=2)
        
        Label(window,text="LOWER SECTION ").grid(row=11,column=0)
        Label(window,text="2 of a kind \n(optional)").grid(row=12,column=0)
        Label(window,text="3 of a kind").grid(row=13,column=0)
        Label(window,text="4 of a kind").grid(row=14,column=0)
        Label(window,text="Full House").grid(row=15,column=0)
        Label(window,text="Sequence of four").grid(row=16,column=0)
        Label(window,text="Sequence of five").grid(row=17,column=0)
        Label(window,text="YATHZEE").grid(row=18,column=0)
        Label(window,text="Chance").grid(row=19,column=0)
        Label(window,text="YATHZEE BONUS").grid(row=20,column=0)
        Label(window,text="TOAL OF LOWER SECTION:").grid(row=21,column=0,columnspan=2)
        Label(window,text="GRAND TOTAL").grid(row=23,column=0,columnspan=2)
        
            
        # second column
        
        f2=Label(window,text="HOW TO COUNT")
        f2.grid(row=0,column=1)
        
        for r in range(1,7):
            Label(window,text="Count only \n%s"%d[r]).grid(row=r,column=1)
            
        Label(window,text="Add 35 if total \n63 or more").grid(row=8,column=1)
        
        Label(window,text="Count total of \nALL dices").grid(row=12,column=1)
        Label(window,text="Count total of \nALL dices").grid(row=13,column=1)
        Label(window,text="Count total of \nALL dices").grid(row=14,column=1)
        Label(window,text="Score 25").grid(row=15,column=1)
        Label(window,text="Score 30").grid(row=16,column=1)
        Label(window,text="Score 40").grid(row=17,column=1)
        Label(window,text="Score 50").grid(row=18,column=1)
        Label(window,text="Count total of \nALL dices").grid(row=19,column=1)
        Label(window,text="Score 100 for every \nbonus Yathzee").grid(row=20,column=1)
        
        # the class player creates and handles the column relative to the n-th player
        class player:
            ''' Creates the column relative to the n-th player  '''
            def __init__(self,n):
                
                def totals(*args):
                    U=[u1_in,u2_in,u3_in,u4_in,u5_in,u6_in]
                    ut1=sum(int(x.get()) for x in U if x.get()!='')     #upper total
                    bonus=35 if ut1>=63 else 0
                    ut2=ut1+bonus                       #upper total with bonus
                    
                    L=[l1_in,l2_in,l3_in,l4_in,l5_in,l6_in,l7_in,l8_in,l9_in]
                    lt=sum([int(x.get()) for x in L if x.get()!=''])  # lower total
                    gt=lt+ut2                                         # grand total
                    
                    UpperTot1_in.set(ut1)
                    Bonus_in.set(bonus)
                    UpperTot2_in.set(ut2)
                    LowerTot_in.set(lt)
                    GrandTot_in.set(gt)
                    
                Label(window,text='Player \n%d'%n).grid(row=0,column=n+2)    
                u1_in=StringVar()
                u1=Entry(window,textvariable=u1_in)
                u1_in.trace('w',totals)
                u2_in=StringVar()
                u2=Entry(window,textvariable=u2_in)
                u2_in.trace('w',totals)
                u3_in=StringVar()
                u3=Entry(window,textvariable=u3_in)
                u3_in.trace('w',totals)
                u4_in=StringVar()
                u4=Entry(window,textvariable=u4_in)
                u4_in.trace('w',totals)
                u5_in=StringVar()
                u5=Entry(window,textvariable=u5_in)
                u5_in.trace('w',totals)
                u6_in=StringVar()
                u6=Entry(window,textvariable=u6_in)
                u6_in.trace('w',totals)
                
                UpperTot1_in=StringVar()
                UpperTot1=Label(window,textvariable=UpperTot1_in)
                Bonus_in=StringVar()
                Bonus=Label(window,textvariable=Bonus_in)
                UpperTot2_in=StringVar()
                UpperTot2=Label(window,textvariable=UpperTot2_in)
                
                l1_in=StringVar()
                l1=Entry(window,textvariable=l1_in)
                l1_in.trace('w',totals)
                l2_in=StringVar()
                l2=Entry(window,textvariable=l2_in)
                l2_in.trace('w',totals)
                l3_in=StringVar()
                l3=Entry(window,textvariable=l3_in)
                l3_in.trace('w',totals)
                l4_in=StringVar()
                l4=Entry(window,textvariable=l4_in)
                l4_in.trace('w',totals)
                l5_in=StringVar()
                l5=Entry(window,textvariable=l5_in)
                l5_in.trace('w',totals)
                l6_in=StringVar()
                l6=Entry(window,textvariable=l6_in)
                l6_in.trace('w',totals)
                l7_in=StringVar()
                l7=Entry(window,textvariable=l7_in)
                l7_in.trace('w',totals)
                l8_in=StringVar()
                l8=Entry(window,textvariable=l8_in)
                l8_in.trace('w',totals)
                l9_in=StringVar()
                l9=Entry(window,textvariable=l9_in)
                l9_in.trace('w',totals)
                
                LowerTot_in=StringVar()
                LowerTot=Label(window,textvariable=LowerTot_in)
                LowerTot_in.trace('w',totals)
                GrandTot_in=StringVar()
                GrandTot=Label(window,textvariable=GrandTot_in)
                GrandTot_in.trace('w',totals)
                
                u1.grid(row=1,column=n+2)
                u2.grid(row=2,column=n+2)
                u3.grid(row=3,column=n+2)
                u4.grid(row=4,column=n+2)
                u5.grid(row=5,column=n+2)
                u6.grid(row=6,column=n+2)
                UpperTot1.grid(row=7,column=n+2)
                Bonus.grid(row=8,column=n+2)
                UpperTot2.grid(row=9,column=n+2)
                l1.grid(row=12,column=n+2)
                l2.grid(row=13,column=n+2)
                l3.grid(row=14,column=n+2)
                l4.grid(row=15,column=n+2)
                l5.grid(row=16,column=n+2)
                l6.grid(row=17,column=n+2)
                l7.grid(row=18,column=n+2)
                l8.grid(row=19,column=n+2)
                l9.grid(row=20,column=n+2)
                LowerTot.grid(row=21,column=n+2)
                GrandTot.grid(row=23,column=n+2)
        
        for i in range(1,player_count+1):
            player(i)
        
        window.mainloop()
            
            

# first start a window asking the number of players, then start the main game 
ask=Tk()
ask.title("Yathzee!!!")
Label(ask,text="Insert the number of players:").grid(row=0,column=0)

N=StringVar()
Entry(ask,textvariable=N).grid(row=0,column=1,columnspan=2)

def start_main(*args):
    try:
        player_count=int(N.get())
        ask.destroy()
        win(player_count)
    except ValueError:
        N.set("Insert an integer")
        
Button(ask,command=start_main,text="Submit").grid(row=2,column=1)
        
ask.mainloop()
            
