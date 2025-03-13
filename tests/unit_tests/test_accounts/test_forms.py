from accounts.forms import RegisterUserForm


# Test Register User form functionality
def test_form_register_user(register_user_valid):
    form = RegisterUserForm(data=register_user_valid)
    assert form.is_valid()


# Test Register User form functionality with invalid data
def test_form_register_user_invalid_data(register_user_invalid):
    form = RegisterUserForm(data=register_user_invalid)
    assert form.errors == {"password2": ["This field is required."]}
