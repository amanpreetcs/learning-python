def requires_admin(func):

    def wrapper(user_role):
        if user_role == 'admin':
            func(user_role)
            return user_role;
        else:
            print("Access Denied")

    return wrapper


@requires_admin
def get_orders(user_role):
    print("Here are your order list: <Array>")

get_orders('admin')
get_orders('customer')