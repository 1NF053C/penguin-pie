def func_under_test():
    return "example function"

def test_example_same_file():
    assert func_under_test() is "example function"

# def test_example_same_file_sanity_test():
#     assert example_same_file_test() is "uncomment this test to cause a failure"
