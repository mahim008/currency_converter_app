from tkinter import *

class CurrencyConverter:
    def __int__(self):
        app_window = Tk()   # created application window
        app_window.title("Currency Converter")  # added title to application window
        app_window.configure(bg="yellow")   # added background-color

        # added label widgets to the window
        Label(app_window, font="Helvetica 12 bold", bg="yellow", text="Amount to Convert").grid(row = 1, column = 1, stricky = W)
        Label(app_window, font="Helvetica 12 bold", bg="yellow", text="Conversion Rate").grid(row = 2, column = 1, stricky = W)
        Label(app_window, font="Helvetica 12 bold", bg="yellow", text="Converted Amount").grid(row = 3, column = 1, stricky = W)

        # created objects and added entry functions
        self.amount_to_convert_var = StringVar()
        Entry(app_window, textvariable=self.amount_to_convert_var, justify = RIGHT).grid(row = 1, column = 2)
        self.conversion_rate_var = StringVar()
        Entry(app_window, textvariable=self.conversion_rate_var, justify = RIGHT).grid(row = 2, column = 2)
        self.converted_amount_var = StringVar()
        lbl_converted_amount = Label(app_window, font="Helvetica 12 bold", bg="yellow", textvariable = self.converted_amount_var).grid(row=3, column=2, stricky = E)




