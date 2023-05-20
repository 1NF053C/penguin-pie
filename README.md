# Inspiration

I'm working on a small codebase. I've been asked to make a few updates, and the first couple changes worked OK, however I'm having trouble debugging the latest change. I need to be able to make small updates with confidence without "re-architecting" everything.

I had expected file imports and path resolution to work a certain way and for asynchronous tests to work out of the box, however things don't work in Python-land like they do in Node.js / JavaScript-land so I had to do some investigation.

This repo is the result of this investigation. It includes the following examples:
- Same file Unit Test example
- Asynchronous Test example
- API Response fixture example (read static Json as mock http response)
- Infrastructure example (docker image and container)
- Fuzz Test example

Everything except fuzz tests are runnable from `pytest`.

# Conclusions
- Small same file unit and async unit tests should be enough to keep troubleshooting and debugging simple, for now.
- A few infrastructure tests may be useful to catch simple mistakes while changing my dockerfile.
- I don't think Fuzz tests and API response mocking are needed while this project is so small.

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

