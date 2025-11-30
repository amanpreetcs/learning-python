class Tooltip ():
    default_text = "Hi, I am a tooltip"


tooltip_one = Tooltip()
tooltip_one.default_text="Hi, I am a new tooltip"

print(tooltip_one.default_text)

del tooltip_one.default_text

# this is known as prop shadowing as it will now fallback to the Class itself, in case of the Class does have the property. it will throw an error
print(tooltip_one.default_text)
