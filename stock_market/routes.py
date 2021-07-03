## It includes all the routes of the application ##

from flask import render_template, url_for, flash, redirect
from stock_market import app
from stock_market.option_strategy import *
from stock_market.forms import *
from flask import request
from IPython.display import HTML

def strategy_decider(strategy, action, strike1, strike2, strike3, strike4):
    if strategy == 1 and action == 11:
        res = short_iron_condor(strike1, strike2, strike3, strike4)
    elif strategy == 1 and action == 12:
        res = long_iron_condor(strike1, strike2, strike3, strike4)
    elif strategy == 2 and action == 11:
        res = short_straddle(strike1)   
    elif strategy == 2 and action == 12:
        res = long_straddle(strike1) 
    elif strategy == 3 and action == 11:
        res = short_strangle(strike1, strike2) 
    elif strategy == 3 and action == 12:
        res = long_strangle_cal(strike1, strike2) 
    elif strategy == 4:
        res = bull_call_spread_cal(strike1, strike2)
    elif strategy == 5:
        res = bear_call_spread_cal(strike1, strike2)
    elif strategy == 6:
        res = bull_put_spread_cal(strike1, strike2)
    elif strategy == 7:
        res = bear_put_spread_cal(strike1, strike2)
    elif strategy == 8 and action == 12:
        res = long_gut(strike1, strike2)
    elif strategy == 8 and action == 11:
        res = short_gut(strike1, strike2)
    elif strategy == 9 and action == 12:
        res = long_iron_butterfly(strike1, strike2, strike3)        
    elif strategy == 9 and action == 11:
        res = short_iron_butterfly(strike1, strike2, strike3)
    elif strategy == 10:
        res = covered_call_cal(strike1)
    elif strategy == 11:
        res = protective_call_cal(strike1)
    elif strategy == 12:
        res = covered_put_cal(strike1)
    elif strategy == 13:
        res = protective_put_cal(strike1)
    return res


@app.route("/front")
def front():
    submit=''       
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "static/"+ plot_name + ".png"
                  
    return render_template("front.html",submit=submit, filename= filename)

        
@app.route("/home")
def home():
    return render_template('layout.html', title = 'home')
    

@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('registration.html', title='Register')



@app.route("/login", methods=['GET', 'POST'])
def login():   
    return render_template('login.html', title='Login')



@app.route("/features", methods=['GET', 'POST'])
def features():
    return render_template('features.html', title= 'features')



@app.route("/strategy_selection", methods=['GET', 'POST'])
def strategy_selection():
    return render_template('strategy_selection.html', title = 'Strategy Selection')



@app.route("/iron_condor", methods=['POST','GET'])    
def iron_condor():
    submit=''       
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "static/"+ plot_name + ".png"
                  
    if request.method=="POST" and 'action' in request.form and 'strike1' in request.form and 'strike2' in request.form and 'strike3' in request.form and 'strike4' in request.form:
        # 'strategy' in request.form and 
        #strategy=int(request.form.get('strategy'))
        strategy = 1
        action=int(request.form.get('action'))

        
        strike1=int(request.form.get('strike1'))
        strike2=int(request.form.get('strike2'))
        strike3=int(request.form.get('strike3'))
        strike4=int(request.form.get('strike4'))
                  
        
        submit = strategy_decider(strategy, action, strike1, strike2, strike3, strike4)
        submit = HTML(submit.to_html(classes="table table-striped"))
        
        
    return render_template("iron_condor.html",title='Iron Condor',submit=submit, filename= filename)


@app.route("/straddle", methods=['GET', 'POST'])    
def straddle():
    submit=''       
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "static/"+ plot_name + ".png"
                  
    if request.method=="POST" and 'action' in request.form and 'strike1' in request.form:
        # and 'strike2' in request.form and 'strike3' in request.form and 'strike4' in request.form:
        # 'strategy' in request.form and 
        #strategy=int(request.form.get('strategy'))
        strategy = 2
        action=int(request.form.get('action'))

        
        strike1=int(request.form.get('strike1'))
        strike2=0
        strike3=0
        strike4=0
                  
        
        submit = strategy_decider(strategy, action, strike1, strike2, strike3, strike4)
        submit = HTML(submit.to_html(classes="table table-striped"))
        
    return render_template('straddle.html', title='Straddle',submit=submit, filename= filename)



@app.route("/strangle", methods=['GET', 'POST'])    
def strangle():
    submit=''       
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "static/"+ plot_name + ".png"
                  
    if request.method=="POST" and 'action' in request.form and 'strike1' in request.form and 'strike2' in request.form:
        # and 'strike2' in request.form and 'strike3' in request.form and 'strike4' in request.form:
        # 'strategy' in request.form and 
        #strategy=int(request.form.get('strategy'))
        strategy = 3
        action=int(request.form.get('action'))

        
        strike1=int(request.form.get('strike1'))
        strike2=int(request.form.get('strike2'))
        strike3=0
        strike4=0
                  
        
        submit = strategy_decider(strategy, action, strike1, strike2, strike3, strike4)
        submit = HTML(submit.to_html(classes="table table-striped"))
        
    return render_template('strangle.html', title='Strangle',submit=submit, filename= filename)



@app.route("/bull_call_spread", methods=['GET', 'POST'])    
def bull_call_spread():
    submit=''       
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "static/"+ plot_name + ".png"
                  
    if request.method=="POST" and 'strike1' in request.form and 'strike2' in request.form:
        # and 'strike2' in request.form and 'strike3' in request.form and 'strike4' in request.form:
        # 'strategy' in request.form and 
        #strategy=int(request.form.get('strategy'))
        strategy = 4
        # action=int(request.form.get('action'))
        action= 0
        
        strike1=int(request.form.get('strike1'))
        strike2=int(request.form.get('strike2'))
        strike3=0
        strike4=0
                  
        
        submit = strategy_decider(strategy, action, strike1, strike2, strike3, strike4)
        submit = HTML(submit.to_html(classes="table table-striped"))
        
    return render_template('bull_call_spread.html', title='Bull Call Spread',submit=submit, filename= filename)



@app.route("/bear_call_spread", methods=['GET', 'POST'])
def bear_call_spread():
    submit=''       
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "static/"+ plot_name + ".png"
                  
    if request.method=="POST" and 'strike1' in request.form and 'strike2' in request.form:
        # and 'strike2' in request.form and 'strike3' in request.form and 'strike4' in request.form:
        # 'strategy' in request.form and 
        #strategy=int(request.form.get('strategy'))
        strategy = 5
        action= 0

        
        strike1=int(request.form.get('strike1'))
        strike2=int(request.form.get('strike2'))
        strike3=0
        strike4=0
                  
        
        submit = strategy_decider(strategy, action, strike1, strike2, strike3, strike4)
        submit = HTML(submit.to_html(classes="table table-striped"))
    return render_template('bear_call_spread.html', title='Bear Call Spread',submit=submit, filename= filename)



@app.route("/bull_put_spread", methods=['GET', 'POST'])    
def bull_put_spread():
    submit=''       
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "static/"+ plot_name + ".png"
                  
    if request.method=="POST" and 'strike1' in request.form and 'strike2' in request.form:
        # and 'strike2' in request.form and 'strike3' in request.form and 'strike4' in request.form:
        # 'strategy' in request.form and 
        #strategy=int(request.form.get('strategy'))
        strategy = 6
        action= 0

        
        strike1=int(request.form.get('strike1'))
        strike2=int(request.form.get('strike2'))
        strike3=0
        strike4=0
                  
        
        submit = strategy_decider(strategy, action, strike1, strike2, strike3, strike4)
        submit = HTML(submit.to_html(classes="table table-striped"))
        
    return render_template('bull_put_spread.html', title='Bull Put Spread',submit=submit, filename= filename)



@app.route("/bear_put_spread", methods=['GET', 'POST'])    
def bear_put_spread():
    submit=''       
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "static/"+ plot_name + ".png"
                  
    if request.method=="POST" and 'strike1' in request.form and 'strike2' in request.form:
        # and 'strike2' in request.form and 'strike3' in request.form and 'strike4' in request.form:
        # 'strategy' in request.form and 
        #strategy=int(request.form.get('strategy'))
        strategy = 7
        action= 0 

        
        strike1=int(request.form.get('strike1'))
        strike2=int(request.form.get('strike2'))
        strike3=0
        strike4=0
                  
        
        submit = strategy_decider(strategy, action, strike1, strike2, strike3, strike4)
        submit = HTML(submit.to_html(classes="table table-striped"))
    return render_template('bear_put_spread.html', title='Bear Put Spread',submit=submit, filename= filename)



@app.route("/gut", methods=['GET', 'POST'])    
def gut():
    submit=''       
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "static/"+ plot_name + ".png"
                  
    if request.method=="POST" and 'action' in request.form and 'strike1' in request.form and 'strike2' in request.form:
        # and 'strike2' in request.form and 'strike3' in request.form and 'strike4' in request.form:
        # 'strategy' in request.form and 
        #strategy=int(request.form.get('strategy'))
        strategy = 8
        action=int(request.form.get('action'))

        
        strike1=int(request.form.get('strike1'))
        strike2=int(request.form.get('strike2'))
        strike3=0
        strike4=0
                  
        
        submit = strategy_decider(strategy, action, strike1, strike2, strike3, strike4)
        submit = HTML(submit.to_html(classes="table table-striped"))
    return render_template('gut.html', title='Gut',submit=submit, filename= filename)



@app.route("/iron_butterfly", methods=['GET', 'POST'])    
def iron_butterfly():
    submit=''       
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "static/"+ plot_name + ".png"
                  
    if request.method=="POST" and 'action' in request.form and 'strike1' in request.form and 'strike2' in request.form and 'strike3' in request.form:
        # 'strategy' in request.form and 
        #strategy=int(request.form.get('strategy'))
        strategy = 9
        action=int(request.form.get('action'))

        
        strike1=int(request.form.get('strike1'))
        strike2=int(request.form.get('strike2'))
        strike3=int(request.form.get('strike3'))
        strike4=0
                  
        
        submit = strategy_decider(strategy, action, strike1, strike2, strike3, strike4)
        submit = HTML(submit.to_html(classes="table table-striped"))
    return render_template('iron_butterfly.html', title='Iron Butterfly',submit=submit, filename= filename)




@app.route("/covered_call", methods=['GET', 'POST'])    
def covered_call():
    submit=''       
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "static/"+ plot_name + ".png"
                  
    if request.method=="POST" and 'strike1' in request.form:
        # and 'strike2' in request.form and 'strike3' in request.form and 'strike4' in request.form:
        # 'strategy' in request.form and 
        #strategy=int(request.form.get('strategy'))
        strategy = 10
        action= 0

        
        strike1=int(request.form.get('strike1'))
        strike2=0
        strike3=0
        strike4=0
                  
        
        submit = strategy_decider(strategy, action, strike1, strike2, strike3, strike4)
        submit = HTML(submit.to_html(classes="table table-striped")) 
    return render_template('covered_call.html', title='Covered Call',submit=submit, filename= filename)




@app.route("/protective_call", methods=['GET', 'POST'])    
def protective_call():
    submit=''       
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "static/"+ plot_name + ".png"
                  
    if request.method=="POST" and 'strike1' in request.form:
        # and 'strike2' in request.form and 'strike3' in request.form and 'strike4' in request.form:
        # 'strategy' in request.form and 
        #strategy=int(request.form.get('strategy'))
        strategy = 11
        action= 0

        
        strike1=int(request.form.get('strike1'))
        strike2=0
        strike3=0
        strike4=0
                  
        
        submit = strategy_decider(strategy, action, strike1, strike2, strike3, strike4)
        submit = HTML(submit.to_html(classes="table table-striped")) 
    return render_template('protective_call.html', title='Protective Call',submit=submit, filename= filename)




@app.route("/covered_put", methods=['GET', 'POST'])    
def covered_put():
    submit=''       
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "static/"+ plot_name + ".png"
                  
    if request.method=="POST" and 'strike1' in request.form:
        # and 'strike2' in request.form and 'strike3' in request.form and 'strike4' in request.form:
        # 'strategy' in request.form and 
        #strategy=int(request.form.get('strategy'))
        strategy = 12
        action= 0

        
        strike1=int(request.form.get('strike1'))
        strike2=0
        strike3=0
        strike4=0
                  
        
        submit = strategy_decider(strategy, action, strike1, strike2, strike3, strike4)
        submit = HTML(submit.to_html(classes="table table-striped")) 
    return render_template('covered_put.html', title='Covered Put',submit=submit, filename= filename)



@app.route("/protective_put", methods=['GET', 'POST'])    
def protective_put():
    submit=''       
    now= datetime.now()
    plot_name = now.strftime("%d%m%Y%H%M%S")
    filename = "static/"+ plot_name + ".png"
                  
    if request.method=="POST" and 'strike1' in request.form:
        # and 'strike2' in request.form and 'strike3' in request.form and 'strike4' in request.form:
        # 'strategy' in request.form and 
        #strategy=int(request.form.get('strategy'))
        strategy = 13
        action= 0

        
        strike1=int(request.form.get('strike1'))
        strike2=0
        strike3=0
        strike4=0
                  
        
        submit = strategy_decider(strategy, action, strike1, strike2, strike3, strike4)
        submit = HTML(submit.to_html(classes="table table-striped")) 
    return render_template('protective_put.html', title='Protective Put',submit=submit, filename= filename)









# @app.route("/result", methods=['GET', 'POST'])
# def result():
#     return render_template('result.html', title='result')



# @app.route("/condor", methods=['GET', 'POST'])    
# def condor():
#     return render_template('condor.html', title='Condor',submit=submit, filename= filename)



# @app.route("/butterfly", methods=['GET', 'POST'])    
# def butterfly():
#     return render_template('butterfly.html', title='Butterfly')



# @app.route("/collar", methods=['GET', 'POST'])    
# def collar():
#     return render_template('collar.html', title='Collar')




