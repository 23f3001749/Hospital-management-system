from flask import Flask
from flask_security import Security # you will import the old way 
from backend.controllers.database import db

app=Flask(__name__) #__name__ is the special built_in python variable that conatins name of the current module
#this can help us by simplyfying to a general context so that it can run for any
if __name__== "__main__": # this indicates that the file to be run only when directly executed and not imported
        app.run(debug=True)
