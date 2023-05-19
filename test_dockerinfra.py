import pytest
import subprocess
import testinfra


# scope='session' uses the same container for all the tests;
# scope='function' uses a new container per test function.
@pytest.fixture(scope="session")
def host(request):
    # build local ./Dockerfile
    subprocess.check_call(["docker", "build", "-t", "myimage", "."])
    # run a container
    docker_id = (
        subprocess.check_output(["docker", "run", "-d", "myimage"]).decode().strip()
    )

    # return a testinfra connection to the container
    yield testinfra.get_host("docker://" + docker_id)
    # at the end of the test suite, destroy container and delete image
    subprocess.check_call(["docker", "rm", "-f", docker_id])
    subprocess.check_call(["docker", "image", "remove", "myimage"])


def test_myimage(host):
    # 'host' now binds to the container
    assert host.exists("python3")
    #assert host.exists("python")
