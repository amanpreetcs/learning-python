def prepare_order():
    print("Welcome! what chai would you like to have?")
    order = yield
    print(f"Thanks for ordering {order}")
    while True:
        print(f"Preparing {order}.....")
        order = yield
        print(f"Thanks for ordering {order}")


take_order = prepare_order()
next(take_order) # start the generator and pause it where it gets the yield value
take_order.send("Green Tea")
take_order.send("Lemon Tea")