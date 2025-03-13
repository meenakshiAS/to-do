from accounts.forms import RegisterUserForm


# Test Register User form functionality
def test_form_register_user(register_user_valid):
    form = RegisterUserForm(data=register_user_valid)
    assert form.is_valid()
