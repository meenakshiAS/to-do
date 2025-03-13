from tasks.models import Task


# Test for Task model
def test_task_model_string_representation(task):
    saved_task = Task.objects.get(id=task.id)
    assert str(saved_task) == task.title
