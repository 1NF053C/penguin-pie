import json

def function_that_depends_on_response_from_a_backing_service(resp):
    new_title = "Title: " + resp["title"] # this function expects "title" to exist as a field in the http response
    return new_title

# this isn't an integration test, this is more of an alternative to running requests against a live backing API
# the gist here is to test the function behavior in isolation while providing an expected response from the backing service
# designing functions to operate only on argument data helps
def test_function_that_depends_on_response_from_backing_service():
    resp_data = mock_request()
    result = function_that_depends_on_response_from_a_backing_service(resp_data)
    assert result == "Title: Noise Filter"

def mock_request():
    f = open("examples/util/response_fixture.json")
    resp_data = json.load(f)
    f.close()
    return resp_data