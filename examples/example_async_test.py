from asyncio import sleep


async def func_under_test(n):
    await sleep(n)
    return "done"


async def test_func_under_test():
    result = await func_under_test(2)
    assert result == "done"

# pytest-aio doesn't require pytest marking
