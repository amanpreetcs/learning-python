class Tooltip ():
    default_text = "Hi, I am a tooltip"

    def fill(self):
        print(self.default_text)



tooltip_one = Tooltip()
# Calling a method through the object/instance.
tooltip_one.fill()

# Calling a method through the class. We need to pass the context(Object/instance)
Tooltip.fill(tooltip_one)