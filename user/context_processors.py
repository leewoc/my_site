from .forms import LoginForm


def login_modal_form(request):
    context = {'login_modal_form': LoginForm()}
    return context
