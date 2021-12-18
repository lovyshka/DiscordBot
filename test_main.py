import main
import pytest
import unittest.mock

@pytest.mark.asyncio
async def test_func():
    ctx = unittest.mock.Mock()
    ctx.author.id = 3
    ctx.send = unittest.mock.AsyncMock()
    await main.hello(ctx)
    ctx.send.assert_called()
    a = ctx.send.call_args.args[0]
    assert a.startswith('Привет,дорогой,')


import sys

if __name__ == '__main__':
    sys.exit(pytest.main())

