class BaseClass:

    # this is how we defined a constructor in python.
    def __init__(self, work, status):
        self.work = work
        self.status = status

    def summary(self):
        print(f"My work is {self.work} and my status is {self.status}")

# Inheritance
class ChildClass(BaseClass):
    def addSubWork(self, subWork):
        self.subWork = subWork
        print(f"Adding sub work is {self.subWork}")


# Composition
class AnotherClass:
    workCls = BaseClass

    def __init__(self, work, status):
        self.work = self.workCls(work, status)

    def describe(self):
        print(self.work.summary());


# Inheritance and Composition
class AllWorks(AnotherClass):
    workCls = ChildClass

    # No need for __init__ as it is inherited from AnotherClass


workBucket = AllWorks("Coding", "Busy")
workBucket.describe()

workBucket.work.addSubWork("Learning Python")
