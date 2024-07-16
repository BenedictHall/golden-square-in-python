from lib.task_list import TaskList
from unittest.mock import Mock

def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

# Unit test `#tasks` and `#all_complete` behaviour
def test_add_tasks_to_list_mock():
    task_list = TaskList()
    fake_task_1 = Mock()
    fake_task_1.title = "task 1"
    fake_task_1.complete = False
    fake_task_2 = Mock()
    fake_task_2.title = "task 2"
    fake_task_2.complete = False
    task_list.add(fake_task_1)
    task_list.add(fake_task_2)
    result = task_list.all()
    assert result == [fake_task_1, fake_task_2]

def test_check_all_completed_when_none():
    task_list = TaskList()
    fake_task_1 = Mock()
    fake_task_1.title = "task 1"
    fake_task_1.is_complete.return_value = False
    fake_task_2 = Mock()
    fake_task_2.title = "task 2"
    fake_task_2.is_complete.return_value = False
    task_list.add(fake_task_1)
    task_list.add(fake_task_2)
    result = task_list.all_complete()
    assert result == False

def test_check_all_completed_when_one():
    task_list = TaskList()
    fake_task_1 = Mock()
    fake_task_1.title = "task 1"
    fake_task_1.is_complete.return_value = False
    fake_task_2 = Mock()
    fake_task_2.title = "task 2"
    fake_task_2.is_complete.return_value = True
    task_list.add(fake_task_1)
    task_list.add(fake_task_2)
    result = task_list.all_complete()
    assert result == False

def test_check_all_completed_when_all():
    task_list = TaskList()
    fake_task_1 = Mock()
    fake_task_1.title = "task 1"
    fake_task_1.is_complete.return_value = True
    fake_task_2 = Mock()
    fake_task_2.title = "task 2"
    fake_task_2.is_complete.return_value = True
    task_list.add(fake_task_1)
    task_list.add(fake_task_2)
    result = task_list.all_complete()
    assert result == True