# Generator functions are used for saving the memory as it stream the output.

def cup_list() :
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

gen_func = cup_list() # pointing the generator function but not executing it.

print(gen_func)
print(next(gen_func)) # execute the generator function and return the first yield value
print(next(gen_func)) # return the next yield value
