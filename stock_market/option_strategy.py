import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from yahoo_fin.stock_info import *


mydata=pd.read_excel('stock_market/optionchain.xlsx')
new_header=mydata.iloc[0]
mydata=mydata[1:]
mydata.columns=new_header
final_data=mydata.set_index('Strike Price')


# IRON CONDOR
def long_iron_condor(strike1, strike2, strike3, strike4):
    
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "stock_market/static/"+ plot_name + ".png"
    
    low=strike1-800
    high=strike4+800
    strike=[]
    pe_buy=[]
    pe_sell=[]
    ce_sell=[]
    ce_buy=[]
    for i in range (low,high+1,100):
        strike.append(i)
                                    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[strike1]        
        if i < strike1:
            diff=strike1-i
            pe_buy.append(diff-premium[1])
        elif i == strike1:
            pe_buy.append(-premium[1])
        elif i > strike1:
            pe_buy.append(-premium[1])
   
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[strike2] 
        if i < strike2:
            diff=strike2-i
            pe_sell.append(premium[1]-diff)
        elif i == strike2:
            pe_sell.append(premium[1])
        elif i>strike2:
            pe_sell.append(premium[1])
   
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[strike3] 
        if i > strike3:
            diff=i-strike3
            ce_sell.append(premium[0]-diff)
        elif i == strike3:
            ce_sell.append(premium[0])
        elif i < strike3:
            ce_sell.append(premium[0])
    
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[strike4] 
        if i >strike4:
            diff=i-strike4
            ce_buy.append(diff-premium[0])
        elif i == strike4:
            ce_buy.append(-premium[0])
        elif i < strike4:
            ce_buy.append(-premium[0])
    
    
    net_pnl=[]
    for i in range(0,len(pe_sell)):
        net=pe_buy[i]+pe_sell[i]+ce_sell[i]+ce_buy[i]
        net_pnl.append(net)
    
    chart = pd.DataFrame(list(zip(strike,pe_buy,pe_sell,ce_sell,ce_buy,net_pnl)), 
               columns =['Strike', 'Put Buy','Put Sell','Call Sell','Call Buy','Net P&L'])
    
    ax = plt.gca()
    chart.plot(kind='line',x='Strike',y='Net P&L', color='red', ax=ax)
    plt.savefig(filename)

    plt.clf()
    return chart


def short_iron_condor(strike1, strike2, strike3, strike4):
        
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "stock_market/static/"+ plot_name + ".png"
                  
    low=strike1-800
    high=strike4+800
    strike=[]
    pe_sell=[]
    pe_buy=[]
    ce_buy=[]
    ce_sell=[]
    for i in range (low,high+1,100):
        strike.append(i)
    #print(strike)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[strike1] 
        if i < strike1:
            diff=strike1-i
            pe_sell.append(premium[1]-diff)
        elif i == strike1:
            pe_sell.append(premium[1])
        elif i>strike1:
            pe_sell.append(premium[1])
    #print(pe_sell)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[strike2]        
        if i < strike2:
            diff=strike2-i
            pe_buy.append(diff-premium[1])
        elif i == strike2:
            pe_buy.append(-premium[1])
        elif i > strike2:
            pe_buy.append(-premium[1])
    #print(pe_buy)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[strike3] 
        if i >strike3:
            diff=i-strike3
            ce_buy.append(diff-premium[0])
        elif i == strike3:
            ce_buy.append(-premium[0])
        elif i < strike3:
            ce_buy.append(-premium[0])
    #print(ce_buy)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[strike4] 
        if i > strike4:
            diff=i-strike4
            ce_sell.append(premium[0]-diff)
        elif i == strike4:
            ce_sell.append(premium[0])
        elif i < strike4:
            ce_sell.append(premium[0])
    #print(ce_sell)
    net_pnl=[]
    for i in range(0,len(pe_sell)):
        net=pe_sell[i]+pe_buy[i]+ce_buy[i]+ce_sell[i]
        net_pnl.append(net)
    
    chart = pd.DataFrame(list(zip(strike,pe_sell,pe_buy,ce_buy,ce_sell,net_pnl)), 
               columns =['Strike', 'Put Sell','Put Buy','Call Buy','Call Sell','Net P&L'])
    
    ax = plt.gca()
    chart.plot(kind='line',x='Strike',y='Net P&L', color='red', ax=ax)
        
    plt.savefig(filename)
    plt.clf()
    return chart   

    
# STRADDLE
def long_straddle(strike1):
        
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "stock_market/static/"+ plot_name + ".png"
    
    low=strike1-800
    high=strike1+800
    strike=[]
    ce_buy=[]
    pe_buy=[]
    for i in range (low,high+1,100):
        strike.append(i)
    #print(strike)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[strike1] 
        if i >strike1:
            diff=i-strike1
            ce_buy.append(diff-premium[0])
        elif i == strike1:
            ce_buy.append(-premium[0])
        elif i < strike1:
            ce_buy.append(-premium[0])
    #print(ce_buy)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[strike1]        
        if i < strike1:
            diff=strike1-i
            pe_buy.append(diff-premium[1])
        elif i == strike1:
            pe_buy.append(-premium[1])
        elif i > strike1:
            pe_buy.append(-premium[1])
    #print(pe_buy)
    
    net_pnl=[]
    for i in range(0,len(ce_buy)):
        net=ce_buy[i]+pe_buy[i]
        net_pnl.append(net)
    
    chart = pd.DataFrame(list(zip(strike,ce_buy,pe_buy,net_pnl)), 
               columns =['Strike','Call Buy','Put Buy','Net P&L'])
    
    
    ax = plt.gca()
    chart.plot(kind='line',x='Strike',y='Net P&L', color='red', ax=ax)
    plt.savefig(filename)
    plt.clf()
    return chart
    
def short_straddle(strike1):
        
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "stock_market/static/"+ plot_name + ".png"
    
    low=strike1-800
    high=strike1+800
    strike=[]
    ce_sell=[]
    pe_sell=[]
    for i in range (low,high+1,100):
        strike.append(i)
    #print(strike)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[strike1] 
        if i < strike1:
            diff=strike1-i
            pe_sell.append(premium[1]-diff)
        elif i == strike1:
            pe_sell.append(premium[1])
        elif i>strike1:
            pe_sell.append(premium[1])
    #print(pe_sell)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[strike1] 
        if i > strike1:
            diff=i-strike1
            ce_sell.append(premium[0]-diff)
        elif i == strike1:
            ce_sell.append(premium[0])
        elif i < strike1:
            ce_sell.append(premium[0])
    #print(ce_sell)
    
    net_pnl=[]
    for i in range(0,len(ce_sell)):
        net=ce_sell[i]+pe_sell[i]
        net_pnl.append(net)
    
    chart = pd.DataFrame(list(zip(strike,ce_sell,pe_sell,net_pnl)), 
               columns =['Strike','Call Sell','Put Sell','Net P&L'])
    
    ax = plt.gca()
    chart.plot(kind='line',x='Strike',y='Net P&L', color='red', ax=ax)
        
    plt.savefig(filename)
    plt.clf()
    return chart

# STRANGLE
def long_strangle(strike1, strike2):
    
    put_strike = strike2
    call_strike = strike1
    
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "stock_market/static/"+ plot_name + ".png"
    
    low=put_strike-800
    high=call_strike+800
    strike=[]
    ce_buy=[]
    pe_buy=[]
    for i in range (low,high+1,100):
        strike.append(i)
    #print(strike)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[call_strike] 
        if i > call_strike:
            diff=i-call_strike
            ce_buy.append(diff-premium[0])
        elif i == call_strike:
            ce_buy.append(-premium[0])
        elif i < call_strike:
            ce_buy.append(-premium[0])
    #print(ce_buy)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[put_strike]        
        if i < put_strike:
            diff=put_strike-i
            pe_buy.append(diff-premium[1])
        elif i == put_strike:
            pe_buy.append(-premium[1])
        elif i > put_strike:
            pe_buy.append(-premium[1])
    #print(pe_buy)
    
    net_pnl=[]
    for i in range(0,len(ce_buy)):
        net=ce_buy[i]+pe_buy[i]
        net_pnl.append(net)
    
    chart = pd.DataFrame(list(zip(strike,ce_buy,pe_buy,net_pnl)), 
               columns =['Strike','Call Buy','Put Buy','Net P&L'])
    
    ax = plt.gca()
    chart.plot(kind='line',x='Strike',y='Net P&L', color='red', ax=ax)
        
    plt.savefig(filename)
    plt.clf()
    return chart



def short_strangle(strike1, strike2):
    
    put_strike = strike2
    call_strike = strike1
    
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "stock_market/static/"+ plot_name + ".png"
    
    low=put_strike-800
    high=call_strike+800
    strike=[]
    ce_sell=[]
    pe_sell=[]
    for i in range (low,high+1,100):
        strike.append(i)
    #print(strike)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[put_strike] 
        if i < put_strike:
            diff=put_strike-i
            pe_sell.append(premium[1]-diff)
        elif i == put_strike:
            pe_sell.append(premium[1])
        elif i>put_strike:
            pe_sell.append(premium[1])
    #print(pe_sell)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[call_strike] 
        if i > call_strike:
            diff=i-call_strike
            ce_sell.append(premium[0]-diff)
        elif i == call_strike:
            ce_sell.append(premium[0])
        elif i < call_strike:
            ce_sell.append(premium[0])
    #print(ce_sell)
    net_pnl=[]
    for i in range(0,len(ce_sell)):
        net=ce_sell[i]+pe_sell[i]
        net_pnl.append(net)
    
    chart = pd.DataFrame(list(zip(strike,ce_sell,pe_sell,net_pnl)), 
               columns =['Strike','Call Sell','Put Sell','Net P&L'])
    
    ax = plt.gca()
    chart.plot(kind='line',x='Strike',y='Net P&L', color='red', ax=ax)
        
    plt.savefig(filename)
    plt.clf()
    return chart

#BULL CALL SPREAD
def bull_call_spread_cal(strike1, strike2):
    
    lower_strike_call=strike1
    higher_strike_call=strike2
   
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "stock_market/static/"+ plot_name + ".png"
    
    low=lower_strike_call-800
    high=higher_strike_call+800
    strike=[]
    ce_buy=[]
    ce_sell=[]
    for i in range (low,high+1,100):
        strike.append(i)
    #print(strike)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[lower_strike_call] 
        if i > lower_strike_call:
            diff=i-lower_strike_call
            ce_buy.append(diff-premium[0])
        elif i == lower_strike_call:
            ce_buy.append(-premium[0])
        elif i < lower_strike_call:
            ce_buy.append(-premium[0])
    #print(ce_buy)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[higher_strike_call] 
        if i > higher_strike_call:
            diff=i-higher_strike_call
            ce_sell.append(premium[0]-diff)
        elif i == higher_strike_call:
            ce_sell.append(premium[0])
        elif i < higher_strike_call:
            ce_sell.append(premium[0])
    #print(ce_sell)
    
    net_pnl=[]
    for i in range(0,len(ce_buy)):
        net=ce_buy[i]+ce_sell[i]
        net_pnl.append(net)
        
    chart = pd.DataFrame(list(zip(strike,ce_buy,ce_sell,net_pnl)), 
               columns =['Strike','Call Sell','Put Sell','Net P&L'])
    ax = plt.gca()
    chart.plot(kind='line',x='Strike',y='Net P&L', color='red', ax=ax)
    plt.savefig(filename)
    plt.clf()
    return chart 
    
#BEAR CALL SPREAD
def bear_call_spread_cal(strike1, strike2):
    
    lower_strike_call= strike1
    higher_strike_call= strike2
    
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "stock_market/static/"+ plot_name + ".png"
    
    low=lower_strike_call-800
    high=higher_strike_call+800
    strike=[]
    ce_buy=[]
    ce_sell=[]
    for i in range (low,high+1,100):
        strike.append(i)
    #print(strike)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[higher_strike_call] 
        if i > higher_strike_call:
            diff=i-higher_strike_call
            ce_buy.append(diff-premium[0])
        elif i == higher_strike_call:
            ce_buy.append(-premium[0])
        elif i < higher_strike_call:
            ce_buy.append(-premium[0])
    #print(ce_buy)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[lower_strike_call] 
        if i > lower_strike_call:
            diff=i-lower_strike_call
            ce_sell.append(premium[0]-diff)
        elif i == lower_strike_call:
            ce_sell.append(premium[0])
        elif i < lower_strike_call:
            ce_sell.append(premium[0])
    #print(ce_sell)
    
    net_pnl=[]
    net_pnl=[]
    for i in range(0,len(ce_buy)):
        net=ce_buy[i]+ce_sell[i]
        net_pnl.append(net)
    
    chart = pd.DataFrame(list(zip(strike,ce_buy,ce_sell,net_pnl)), 
               columns =['Strike','Call Buy','Call Sell','Net P&L'])
    ax = plt.gca()
    chart.plot(kind='line',x='Strike',y='Net P&L', color='red', ax=ax)
    plt.savefig(filename)
    plt.clf()
    return chart 


#BULL PUT SPREAD
def bull_put_spread_cal(strike1, strike2):
    
    lower_strike_put= strike1
    higher_strike_put= strike2
    
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "stock_market/static/"+ plot_name + ".png"
    
    low=lower_strike_put-800
    high=higher_strike_put+800
    strike=[]
    pe_buy=[]
    pe_sell=[]
    for i in range (low,high+1,100):
        strike.append(i)
    #print(strike)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[lower_strike_put]        
        if i < lower_strike_put:
            diff=lower_strike_put-i
            pe_buy.append(diff-premium[1])
        elif i == lower_strike_put:
            pe_buy.append(-premium[1])
        elif i > lower_strike_put:
            pe_buy.append(-premium[1])
    #print(pe_buy)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[ higher_strike_put] 
        if i < higher_strike_put:
            diff= higher_strike_put-i
            pe_sell.append(premium[1]-diff)
        elif i == higher_strike_put:
            pe_sell.append(premium[1])
        elif i> higher_strike_put:
            pe_sell.append(premium[1])
    #print(pe_sell)
    
    net_pnl=[]
    for i in range(0,len(pe_buy)):
        net=pe_buy[i]+pe_sell[i]
        net_pnl.append(net)
    
    chart = pd.DataFrame(list(zip(strike,pe_buy,pe_sell,net_pnl)), 
               columns =['Strike','Put Buy','Put Sell','Net P&L'])
    ax = plt.gca()
    chart.plot(kind='line',x='Strike',y='Net P&L', color='red', ax=ax)
    plt.savefig(filename)
    plt.clf()
    return chart
    
#BEAR PUT SPREAD
def bear_put_spread_cal(strike1, strike2):
    
    lower_strike_put= strike1
    higher_strike_put= strike2
    
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "stock_market/static/"+ plot_name + ".png"
    
    low=lower_strike_put-800
    high=higher_strike_put+800
    strike=[]
    pe_buy=[]
    pe_sell=[]
    for i in range (low,high+1,100):
        strike.append(i)
    #print(strike)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[higher_strike_put]        
        if i < higher_strike_put:
            diff=higher_strike_put-i
            pe_buy.append(diff-premium[1])
        elif i == higher_strike_put:
            pe_buy.append(-premium[1])
        elif i > higher_strike_put:
            pe_buy.append(-premium[1])
    #print(pe_buy)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[lower_strike_put] 
        if i < lower_strike_put:
            diff= lower_strike_put-i
            pe_sell.append(premium[1]-diff)
        elif i == lower_strike_put:
            pe_sell.append(premium[1])
        elif i> lower_strike_put:
            pe_sell.append(premium[1])
    #print(pe_sell)
    
    net_pnl=[]
    for i in range(0,len(pe_buy)):
        net=pe_buy[i]+pe_sell[i]
        net_pnl.append(net)
    
    chart = pd.DataFrame(list(zip(strike,pe_buy,pe_sell,net_pnl)), 
               columns =['Strike','Put Buy','Put Sell','Net P&L'])
    ax = plt.gca()
    chart.plot(kind='line',x='Strike',y='Net P&L', color='red', ax=ax)
    plt.savefig(filename)
    plt.clf()
    return chart
    
# GUT
def long_gut(strike1, strike2):
    
    call_strike = strike1
    put_strike = strike2
    
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "stock_market/static/"+ plot_name + ".png"
    
    low=call_strike-500
    high=put_strike+500
    strike=[]
    ce_buy=[]
    pe_buy=[]
    
    for i in range (low,high+1,100):
        strike.append(i)
    #print(strike)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[call_strike] 
        if i > call_strike:
            diff=i-call_strike
            ce_buy.append(diff-premium[0])
        elif i == call_strike:
            ce_buy.append(-premium[0])
        elif i < call_strike:
            ce_buy.append(-premium[0])
    #print(ce_buy)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[put_strike]        
        if i < put_strike:
            diff=put_strike-i
            pe_buy.append(diff-premium[1])
        elif i == put_strike:
            pe_buy.append(-premium[1])
        elif i > put_strike:
            pe_buy.append(-premium[1])
    #print(pe_buy)
    
    net_pnl=[]
    for i in range(0,len(ce_buy)):
        net=ce_buy[i]+pe_buy[i]
        net_pnl.append(net)
    
    chart = pd.DataFrame(list(zip(strike,ce_buy,pe_buy,net_pnl)), 
               columns =['Strike','Call Buy','Put Buy','Net P&L'])
    ax = plt.gca()
    chart.plot(kind='line',x='Strike',y='Net P&L', color='red', ax=ax)
    plt.savefig(filename)
    plt.clf()
    return chart


def short_gut(strike1, strike2):
    
    call_strike = strike1
    put_strike = strike2
    
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "stock_market/static/"+ plot_name + ".png"
    
    low=call_strike-800
    high=put_strike+800
    strike=[]
    ce_sell=[]
    pe_sell=[]
    
    for i in range (low,high+1,100):
        strike.append(i)
    #print(strike)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[put_strike] 
        if i < put_strike:
            diff=put_strike-i
            pe_sell.append(premium[1]-diff)
        elif i == put_strike:
            pe_sell.append(premium[1])
        elif i>put_strike:
            pe_sell.append(premium[1])
    #print(pe_sell)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[call_strike] 
        if i > call_strike:
            diff=i-call_strike
            ce_sell.append(premium[0]-diff)
        elif i == call_strike:
            ce_sell.append(premium[0])
        elif i < call_strike:
            ce_sell.append(premium[0])
    #print(ce_sell)
    
    net_pnl=[]
    for i in range(0,len(ce_sell)):
        net=ce_sell[i]+pe_sell[i]
        net_pnl.append(net)
    
    chart = pd.DataFrame(list(zip(strike,ce_sell,pe_sell,net_pnl)), 
               columns =['Strike','Call Sell','Put Sell','Net P&L'])
    ax = plt.gca()
    chart.plot(kind='line',x='Strike',y='Net P&L', color='red', ax=ax)
    plt.savefig(filename)
    plt.clf()
    return chart

# IRON BUTTERFLY
def long_iron_butterfly(strike1, strike2, strike3):
    
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "stock_market/static/"+ plot_name + ".png"
    
    low=strike1-800
    high=strike3+800
    strike=[]
    pe_buy=[]
    pe_sell=[]
    ce_sell=[]
    ce_buy=[]
    for i in range (low,high+1,100):
        strike.append(i)
        
    #print(strike)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[strike1]        
        if i < strike1:
            diff=strike1-i
            pe_buy.append(diff-premium[1])
        elif i == strike1:
            pe_buy.append(-premium[1])
        elif i > strike1:
            pe_buy.append(-premium[1])
    #print(pe_buy)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[strike2] 
        if i < strike2:
            diff=strike2-i
            pe_sell.append(premium[1]-diff)
        elif i == strike2:
            pe_sell.append(premium[1])
        elif i>strike2:
            pe_sell.append(premium[1])
    #print(pe_sell)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[strike2] 
        if i > strike2:
            diff=i-strike2
            ce_sell.append(premium[0]-diff)
        elif i == strike2:
            ce_sell.append(premium[0])
        elif i < strike2:
            ce_sell.append(premium[0])
    #print(ce_sell)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[strike3] 
        if i >strike3:
            diff=i-strike3
            ce_buy.append(diff-premium[0])
        elif i == strike3:
            ce_buy.append(-premium[0])
        elif i < strike3:
            ce_buy.append(-premium[0])
    #print(ce_buy)
    
    net_pnl=[]
     
    for i in range(0,len(pe_sell)):
        net=pe_buy[i]+pe_sell[i]+ce_sell[i]+ce_buy[i]
        net_pnl.append(net)
    
    chart = pd.DataFrame(list(zip(strike,pe_buy,pe_sell,ce_sell,ce_buy,net_pnl)), 
               columns =['Strike', 'Put Buy','Put Sell','Call Sell','Call Buy','Net P&L'])
    ax = plt.gca()
    chart.plot(kind='line',x='Strike',y='Net P&L', color='red', ax=ax)
   
    plt.savefig(filename)
    plt.clf()
    return chart

def short_iron_butterfly(strike1, strike2, strike3):
    
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "stock_market/static/"+ plot_name + ".png"
    
    low=strike1-800
    high=strike3+800
    strike=[]
    pe_buy=[]
    pe_sell=[]
    ce_sell=[]
    ce_buy=[]
    for i in range (low,high+1,100):
        strike.append(i)
        
    #print(strike)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[strike1] 
        if i < strike1:
            diff=strike1-i
            pe_sell.append(premium[1]-diff)
        elif i == strike1:
            pe_sell.append(premium[1])
        elif i>strike1:
            pe_sell.append(premium[1])
    #print(pe_sell)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[strike2]        
        if i < strike2:
            diff=strike2-i
            pe_buy.append(diff-premium[1])
        elif i == strike2:
            pe_buy.append(-premium[1])
        elif i > strike2:
            pe_buy.append(-premium[1])
    #print(pe_buy)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[strike2] 
        if i >strike2:
            diff=i-strike2
            ce_buy.append(diff-premium[0])
        elif i == strike2:
            ce_buy.append(-premium[0])
        elif i < strike2:
            ce_buy.append(-premium[0])
    #print(ce_buy)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[strike3] 
        if i > strike3:
            diff=i-strike3
            ce_sell.append(premium[0]-diff)
        elif i == strike3:
            ce_sell.append(premium[0])
        elif i < strike3:
            ce_sell.append(premium[0])
    #print(ce_sell)
    
    net_pnl=[]
    for i in range(0,len(pe_sell)):
        net=pe_sell[i]+pe_buy[i]+ce_buy[i]+ce_sell[i]
        net_pnl.append(net)
    
    chart = pd.DataFrame(list(zip(strike,pe_sell,pe_buy,ce_buy,ce_sell,net_pnl)), 
               columns =['Strike', 'Put Sell','Put Buy','Call Buy','Call Sell','Net P&L'])
    ax = plt.gca()
    chart.plot(kind='line',x='Strike',y='Net P&L', color='red', ax=ax)
   
    plt.savefig(filename)
    plt.clf()
    return chart
    




# PROTECTIVE CALL
def protective_call_cal(call_strike):
    
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "stock_market/static/"+ plot_name + ".png"
    
    live_price=get_live_price('^NSEI') #dictionary to be used later 
    low=call_strike-800
    high=call_strike+800
    strike=[]
    ce_buy=[]
    equity_sell=[]
    
    for i in range (low,high+1,100):
        strike.append(i)
    #print(strike)
    
    #print(live_price)
    
    for i in range(low,high+1,100):
        diff =live_price-i
        equity_sell.append(diff)
    #print(equity_sell)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[call_strike] 
        if i >call_strike:
            diff=i-call_strike
            ce_buy.append(diff-premium[0])
        elif i == call_strike:
            ce_buy.append(-premium[0])
        elif i < call_strike:
            ce_buy.append(-premium[0])
    #print(ce_buy)
    
    net_pnl=[]
    for i in range(0,len(ce_buy)):
        net=equity_sell[i]+ce_buy[i]
        net_pnl.append(net)
    
    chart = pd.DataFrame(list(zip(strike,equity_sell,ce_buy,net_pnl)), 
               columns =['Strike','Equity Sell','Call Buy','Net P&L'])
    ax = plt.gca()
    chart.plot(kind='line',x='Strike',y='Net P&L', color='red', ax=ax)
   
    plt.savefig(filename)
    plt.clf()
    return chart
    
# PROTECTIVE PUT
def protective_put_cal(put_strike):
    
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "stock_market/static/"+ plot_name + ".png"
    
    live_price=get_live_price('^NSEI') #dictionary to be used later 
    low=put_strike-800
    high=put_strike+800
    strike=[]
    pe_buy=[]
    equity_buy=[]
    
    for i in range (low,high+1,100):
        strike.append(i)
    #print(strike)
    
    #print(live_price)
    
    for i in range(low,high+1,100):
        diff =i-live_price
        equity_buy.append(diff)
    #print(equity_buy)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[put_strike]        
        if i < put_strike:
            diff=put_strike-i
            pe_buy.append(diff-premium[1])
        elif i == put_strike:
            pe_buy.append(-premium[1])
        elif i > put_strike:
            pe_buy.append(-premium[1])
    #print(pe_buy)
    
    net_pnl=[]
    for i in range(0,len(pe_buy)):
        net=equity_buy[i]+pe_buy[i]
        net_pnl.append(net)
    
    chart = pd.DataFrame(list(zip(strike,equity_buy,pe_buy,net_pnl)), 
               columns =['Strike','Equity Buy','Put Buy','Net P&L'])
    ax = plt.gca()
    chart.plot(kind='line',x='Strike',y='Net P&L', color='red', ax=ax)
   
    plt.savefig(filename)
    plt.clf()
    return chart 

# COVERED PUT
def covered_put_cal(put_strike):
    
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "stock_market/static/"+ plot_name + ".png"
    
    live_price=get_live_price('^NSEI') #dictionary to be used later 
    low=put_strike-800
    high=put_strike+800
    strike=[]
    pe_sell=[]
    equity_sell=[]
    
    for i in range (low,high+1,100):
        strike.append(i)
    #print(strike)
    
    #print(abs(live_price))
    
    for i in range(low,high+1,100):
        diff =live_price-i
        equity_sell.append(diff)
    #print(equity_sell)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[put_strike] 
        if i < put_strike:
            diff=put_strike-i
            pe_sell.append(premium[1]-diff)
        elif i == put_strike:
            pe_sell.append(premium[1])
        elif i>put_strike:
            pe_sell.append(premium[1])
    #print(pe_sell)
    
    net_pnl=[]
    for i in range(0,len(pe_sell)):
        net=equity_sell[i]+pe_sell[i]
        net_pnl.append(net)
    
    chart = pd.DataFrame(list(zip(strike,equity_sell,pe_sell,net_pnl)), 
               columns =['Strike','Equity Sell','Put Sell','Net P&L'])
    ax = plt.gca()
    chart.plot(kind='line',x='Strike',y='Net P&L', color='red', ax=ax)
   
    plt.savefig(filename)
    plt.clf()
    return chart

# COVERED CALL
def covered_call_cal(call_strike):
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "stock_market/static/"+ plot_name + ".png"
    
    live_price=get_live_price('^NSEI') #dictionary to be used later 
    low=call_strike-800
    high=call_strike+800
    strike=[]
    ce_sell=[]
    equity_buy=[]
    
    for i in range (low,high+1,100):
        strike.append(i)
    #print(strike)
    
    #print(live_price)
    
    for i in range(low,high+1,100):
        diff =i-live_price
        equity_buy.append(diff)
    #print(equity_buy)
    
    for i in range (low,high+1,100):
        premium=final_data['BidPrice'].loc[call_strike] 
        if i > call_strike:
            diff=i-call_strike
            ce_sell.append(premium[0]-diff)
        elif i == call_strike:
            ce_sell.append(premium[0])
        elif i < call_strike:
            ce_sell.append(premium[0])
   #print(ce_sell)
    
    net_pnl=[]
    for i in range(0,len(ce_sell)):
        net=equity_buy[i]+ce_sell[i]
        net_pnl.append(net)
    #print(net_pnl)
    
    chart = pd.DataFrame(list(zip(strike,equity_buy,ce_sell,net_pnl)), 
               columns =['Strike','Equity Buy','Call sell','Net P&L'])
    print(chart)
    
    ax = plt.gca()
    chart.plot(kind='line',x='Strike',y='Net P&L', color='red', ax=ax)
    plt.savefig(filename)
    plt.clf()
    return chart 



