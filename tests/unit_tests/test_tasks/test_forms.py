import pytest

from tasks.forms import TaskForm


# Test Create task for form submission valid scenario
@pytest.mark.django_db
def test_create_task_form_valid_data(task_form_valid):
    form = TaskForm(data=task_form_valid)
    assert form.is_valid()
