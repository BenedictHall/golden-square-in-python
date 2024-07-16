from lib.task_formatter import *
from unittest.mock import Mock

def test_task_added():
    fake_task = Mock()
    formatter = TaskFormatter(fake_task)
    assert formatter.task == fake_task

def test_format_completed():
    fake_task = Mock()
    fake_task.is_complete.return_value = True
    fake_task.title = "fake title"
    formatter = TaskFormatter(fake_task)
    assert formatter.format() == "[x] fake title"

def test_format_incomplete():
    fake_task = Mock()
    fake_task.is_complete.return_value = False
    fake_task.title = "fake title"
    formatter = TaskFormatter(fake_task)
    assert formatter.format() == "[ ] fake title"

def test_format_empty_title():
    fake_task = Mock()
    fake_task.is_complete.return_value = True
    fake_task.title = ""
    formatter = TaskFormatter(fake_task)
    assert formatter.format() == "[x] "