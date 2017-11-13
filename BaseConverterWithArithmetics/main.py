from View.UI import UI
from Controller.Controller import Controller

def main():
    controller = Controller()
    ui = UI(controller)
    
    ui.mainMenu()

main()