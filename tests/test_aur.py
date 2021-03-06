# MIT licensed
# Copyright (c) 2013-2017 lilydjwg <lilydjwg@gmail.com>, et al.

from flaky import flaky
import pytest
pytestmark = pytest.mark.asyncio

@flaky(max_runs=5)
async def test_aur(get_version):
    assert await get_version("ssed", {"aur": None}) == "3.62-2"

@flaky(max_runs=5)
async def test_aur_strip_release(get_version):
    assert await get_version("ssed", {"aur": None, "strip-release": 1}) == "3.62"
