import pytest

from tasks.forms import TaskForm


# Test Create task for form submission valid scenario
@pytest.mark.django_db
def test_create_task_form_valid_data(task_form_valid):
    form = TaskForm(data=task_form_valid)
    assert form.is_valid()


# Test Create task for form submission missing title scenario
@pytest.mark.django_db
def test_create_task_form_missing_title(task_form_missing_title):
    form = TaskForm(data=task_form_missing_title)
    assert not form.is_valid()
    assert "title" in form.errors


# Test Create task for form submission missing description scenario
@pytest.mark.django_db
def test_create_task_form_missing_description(task_form_missing_description):
    form = TaskForm(data=task_form_missing_description)
    assert not form.is_valid()
    assert "description" in form.errors


# Test Create task for form submission missing due date scenario
@pytest.mark.django_db
def test_create_task_form_missing_due_date(task_form_missing_due_date):
    form = TaskForm(data=task_form_missing_due_date)
    assert not form.is_valid()
    assert "due_date" in form.errors
