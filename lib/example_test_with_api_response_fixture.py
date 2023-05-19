import json

def function_that_depends_on_response_from_a_backing_service(obj):
    new_title = "Title: " + obj["title"]
    return new_title

# this isn't an integration test, this is more of an alternative to running requests against a live backing API
# the gist here is to test the function behavior in isolation while providing an expected response from the backing service
# designing functions to operate only on argument data helps
def test_function_that_depends_on_response_from_backing_service():
    f = open("lib/util/response_fixture.json")
    data = json.load(f)
    result = function_that_depends_on_response_from_a_backing_service(data)
    assert result == "Title: Noise Filter"
    f.close()
