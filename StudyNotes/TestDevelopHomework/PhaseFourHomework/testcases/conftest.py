import pytest

@pytest.hookimpl(hookwrapper=True,tryfirst=True)
def pytest_runtest_makereport(item, call):
    out = yield
    report = out.get_result()
    if report.outcome == "failed":
        print("截图")
    print("执行结果：%s" % report.outcome)
