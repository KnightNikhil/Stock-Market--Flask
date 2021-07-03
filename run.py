## Only job is to run the application ##

from stock_market import app
#There should be an app variable in the __init__.py file 

if __name__ == '__main__':
    app.run(debug=True)
