# pytest-exemplar

pytest examples

## activate virtual env
```sh
source venv/bin/activate
```

## How to run fuzz tests:

```sh
py-afl-fuzz -m 600 -i fuzzing-inputs/ -o fuzzing-results/ -- python lib/example_fuzzing.py @@
```

[lib/example_fuzzing.py](lib/example_fuzzing.py)


## How to run infrastructure tests:

```sh
pytest ./
```

[test_local_infra_example.py](test_local_infra_example.py)

[test_dockerinfra.py](test_dockerinfra.py)


## How to run unit tests:

```sh
pytest examples/*
```

[examples/example_unit_test_same_file.py](examples/example_unit_test_same_file.py)

[examples/example_test_with_api_response_fixture.py](examples/example_test_with_api_response_fixture.py)

[examples/example_async_test.py](examples/example_async_test.py) # pytest-aio does not require any extra setup

