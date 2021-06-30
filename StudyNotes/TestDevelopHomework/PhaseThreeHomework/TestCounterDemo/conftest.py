from typing import List

import pytest

from StudyNotes.TestDevelopHomework.PhaseThreeHomework.CounterDemo.Counter import CounterDemoTest

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


@pytest.fixture(scope="class")
def counterBegin():
    print("开始计算")
    # 实例化CounterDemo类
    counterDemoTest = CounterDemoTest()
    yield counterDemoTest

    print("计算结束")