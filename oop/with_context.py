class MyClass(object):

    def __enter__(self):
        print('we have entered "with"')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('we are leaving "with"')

    def sayhi(self):
        print('Hi! instance is %s' %(id(self)))

with MyClass() as cc:
    cc.sayhi()

    print('after the "with" block')
