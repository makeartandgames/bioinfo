# Docker Instructions

# Running tests

Build Image, Run Tests:

```sh
./build_docker.sh my_app
docker run -t my_app ./run_tests.sh
```


Run a single test in the class TodoTestCase, with the name "test_home"

```sh
./build_docker.sh my_app
docker run -t my_app ./run_tests.sh TodoTestCase.test_home
```
