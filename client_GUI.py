
import socket

# Python program to  create a simple GUI
# Using Tkinter

# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
expression = ""


# Function to update expressiom
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)
# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")


# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="white")

    # set the title of GUI window
    gui.title("Simple GUI")

    # set the configuration of GUI window
    gui.geometry("600x600")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=5, ipadx=100)

    equation.set('enter your choice')

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    KEY1 = Button(gui, text=' 1 ', fg='black', bg='red',
                     command=lambda: press(1), height=1, width=7)
    KEY1.grid(row=4, column=0)

    KEY2 = Button(gui, text=' 2 ', fg='black', bg='red',
                     command=lambda: press(2), height=1, width=7)
    KEY2.grid(row=4, column=1)

    KEY3 = Button(gui, text=' 3 ', fg='black', bg='red',
                     command=lambda: press(3), height=1, width=7)
    KEY3.grid(row=4, column=2)

    KEY4 = Button(gui, text=' 4 ', fg='black', bg='red',
                     command=lambda: press(4), height=1, width=7)
    KEY4.grid(row=5, column=0)

    KEY5 = Button(gui, text=' 5 ', fg='black', bg='red',
                     command=lambda: press(5), height=1, width=7)
    KEY5.grid(row=5, column=1)

    KEY6 = Button(gui, text=' 6 ', fg='black', bg='red',
                     command=lambda: press(6), height=1, width=7)
    KEY6.grid(row=5, column=2)

    KEY7 = Button(gui, text=' 7 ', fg='black', bg='red',
                     command=lambda: press(7), height=1, width=7)
    KEY7.grid(row=6, column=0)

    KEY8 = Button(gui, text=' 8 ', fg='black', bg='red',
                     command=lambda: press(8), height=1, width=7)
    KEY8.grid(row=6, column=1)

    KEY9 = Button(gui, text=' 9 ', fg='black', bg='red',
                     command=lambda: press(9), height=1, width=7)
    KEY9.grid(row=6, column=2)

    KEY0 = Button(gui, text=' 0 ', fg='black', bg='red',
                     command=lambda: press(0), height=1, width=7)
    KEY0.grid(row=7, column=1)

    VOLUP = Button(gui, text=' VOLUP ', fg='black', bg='red',
                  command=lambda: press(13), height=1, width=7)
    VOLUP.grid(row=8, column=0)

    VOLDOWN = Button(gui, text=' VOLDOWN ', fg='black', bg='red',
                   command=lambda: press(12), height=1, width=7)
    VOLDOWN.grid(row=9, column=0)

    VOLMUTE = Button(gui, text=' VOLMUTE ', fg='black', bg='red',
                      command=lambda: press(50), height=1, width=7)
    VOLMUTE.grid(row=3, column=2)

    CHNLUP= Button(gui, text=' CHNLUP ', fg='black', bg='red',
                    command=lambda: press(104), height=1, width=7)
    CHNLUP.grid(row=8, column=2)

    CHNLDOWN = Button(gui, text=' CHNLDOWN ', fg='black', bg='red',
                    command=lambda: press(109), height=1, width=7)
    CHNLDOWN.grid(row=9, column=2)

    MENU = Button(gui, text=' MENU ', fg='black', bg='red',
                    command=lambda: press(102), height=1, width=7)
    MENU.grid(row=11, column=0)

    RETURN = Button(gui, text=' RETURN ', fg='black', bg='red',
                    command=lambda: press(1), height=1, width=7)
    RETURN.grid(row=9, column=1)

    INFO = Button(gui, text=' INFO ', fg='black', bg='red',
                command=lambda: press(115), height=1, width=7)
    INFO.grid(row=11, column=2)

    OK = Button(gui, text=' OK ', fg='black', bg='red',
                    command=lambda: press(28), height=1, width=7)
    OK.grid(row=8, column=1)

    NAV_RIGHT = Button(gui, text=' NAVRIGHT ', fg='black', bg='red',
                   command=lambda: press(106), height=1, width=7)
    NAV_RIGHT.grid(row=14, column=2)

    NAV_LEFT = Button(gui, text=' NAVLEFT ', fg='black', bg='red',
                     command=lambda: press(105), height=1, width=7)
    NAV_LEFT.grid(row=14, column=0)

    NAV_UP = Button(gui, text=' NAVUP ', fg='black', bg='red',
                    command=lambda: press(103), height=1, width=7)
    NAV_UP.grid(row=13, column=1)

    NAV_DOWN = Button(gui, text=' NAVDOWN ', fg='black', bg='red',
                   command=lambda: press(108), height=1, width=7)
    NAV_DOWN.grid(row=15, column=1)

    FAST_FORWARD = Button(gui, text=' FAST_FORWARD ', fg='black', bg='red',
                   command=lambda: press(208), height=1, width=7)
    FAST_FORWARD.grid(row=16, column=0)

    REWIND = Button(gui, text=' REWIND ', fg='black', bg='red',
                          command=lambda: press(168), height=1, width=7)
    REWIND.grid(row=16, column=2)

    PLAY_PAUSE = Button(gui, text=' PLAY/PAUSE ', fg='black', bg='red',
                          command=lambda: press(57), height=1, width=7)
    PLAY_PAUSE.grid(row=17, column=0)

    POWER = Button(gui, text=' POWER ', fg='black', bg='red',
                 command=lambda: press(142), height=1, width=7)
    POWER.grid(row=2, column=2)


    FAV = Button(gui, text=' FAV ', fg='black', bg='red',
                          command=lambda: press(49), height=1, width=7)
    FAV.grid(row=17, column=2)

    clear = Button(gui, text='Clear', fg='black', bg='red',
                   command=clear, height=1, width=7)
    clear.grid(row=18, column='2')

    # start the GUI
    gui.mainloop()

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 27015  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    # Send data
    client_socket.send(expression.encode())
    # Look for the response
    data = client_socket.recv(16).decode()
    print ('received:' + data)
    print('Enter the message or type Bye for closing the socket')
    message = input(" -> ")   # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data1 = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data1)  # show in terminal
        print('Enter the message or type Bye for closing the socket')
        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()

