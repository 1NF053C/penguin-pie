def test_python_is_installed(host):
    assert host.package("python3").is_installed
