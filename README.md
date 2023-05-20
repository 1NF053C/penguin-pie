# Inspiration

TL:DR; I prefer to work effectively **so that I can spend time outside with friends and family** :D.

I'm working on a codebase that has prioritized functionality and release over design. This has worked well given the goals of the project and given that the codebase is relatively small.

I've been asked to make a few updates to the codebase, and the first couple changes worked OK however I'm having trouble debugging the latest change. I need to be able to make small updates with confidence without "re-architecting" everything and without offering abstract design recommendations that have too much room for misinterpretion by other developers.

I had expected file imports and path resolution to work a certain way and for asynchronous tests to work out of the box, however things don't work in Python-land like they do in Node.js / JavaScript-land so I had to do some investigation.

This repo is the result of this investigation. It includes the following examples:
- Same file Unit Test example
- Asynchronous Test example
- Read static JSON example
- Infrastructure (docker image and container) Test example
- Fuzz Test example

Small same file unit and async unit tests should be enough for now to keep troubleshooting and debugging simple.

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

