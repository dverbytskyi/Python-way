class TestClass:
    @classmethod
    def setup_class(cls):
        print("\n *** Setup TestClass ***")

    @classmethod
    def teardown_class(cls):
        print("\n *** Teardown TestClass *** ")

    def setup_method(self, method):
        if method == self.test1:
            print("\nSetting up test1")
        elif method == self.test2:
            print("\nSetting up test2")
        else:
            print("\nSetting up unknown test")

    def teardown_method(self, method):
        if method == self.test1:
            print("\nTearing down test1")
        elif method == self.test2:
            print("\nTearing down test2")
        else:
            print("\nTearing down unknown test")


    def test1(self):
        print("Executing test1")
        assert True

    def test2(self):
        print("Executing test2")
        assert True


'''
def setup_module():
def teardown_module():

def setup_function():
def teardown_function():

def setup_class():
def teardown_class():

// Test Methods in Test Classes
def setup_method():
def teardown_method():
'''