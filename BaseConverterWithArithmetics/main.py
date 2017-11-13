'''
Created on Nov 13, 2017

@author: Gabriel Em
'''

from View.UI import UI
from Controller.Controller import Controller

def main():
    controller = Controller()
    ui = UI(controller)
    
    ui.mainMenu()

main()