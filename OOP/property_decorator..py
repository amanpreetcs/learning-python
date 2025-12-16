class TeaLeaf:

    def __init__(self, age):
        self._age=age

    # Define Getter for age property
    @property
    def age(self):
        return self.age

    # Define Setter for age property
    @age.setter
    def age(self, age):
        if(1<= age <= 10):
            self._age = age
        else:
            raise ValueError("Age must be between 1 and 10")


teaLeaf = TeaLeaf(2)
print(teaLeaf._age)