import pathlib

_PASSED_TASKS = set()
_FAILED_TASKS = set()


def _count_all_tasks(project_root):
    tests_dir = project_root / "tests"
    return len(list(tests_dir.glob("week*/test_task*.py")))


def pytest_configure(config):
    project_root = pathlib.Path(__file__).resolve().parent
    config._pz_project_root = project_root
    config._pz_max_tasks = _count_all_tasks(project_root)
    config._pz_selected_max = 0
    _PASSED_TASKS.clear()
    _FAILED_TASKS.clear()


def pytest_collection_modifyitems(session, config, items):
    config._pz_selected_max = len(items)


def pytest_runtest_logreport(report):
    task_id = report.nodeid.split("::", 1)[0]

    if report.failed:
        _FAILED_TASKS.add(task_id)
        _PASSED_TASKS.discard(task_id)
        return

    if report.when == "call" and report.passed and task_id not in _FAILED_TASKS:
        _PASSED_TASKS.add(task_id)


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    max_tasks = getattr(config, "_pz_max_tasks", 0)
    selected_max = getattr(config, "_pz_selected_max", 0)
    passed_tasks = len(_PASSED_TASKS)
    failed_selected = max(0, selected_max - passed_tasks)
    failed_tasks = max(0, max_tasks - passed_tasks)

    terminalreporter.section("VV1 PZ body")
    terminalreporter.write_line(
        f"Splnené úlohy v tomto behu: {passed_tasks} z {selected_max}"
    )
    terminalreporter.write_line(
        f"Body (VV1): {passed_tasks} / {max_tasks}"
    )
    terminalreporter.write_line(
        f"Nesplnené úlohy v tomto behu: {failed_selected}"
    )
    terminalreporter.write_line(
        f"Zostáva do maxima VV1: {failed_tasks}"
    )
