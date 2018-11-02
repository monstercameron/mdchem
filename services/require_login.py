from flask import Blueprint, redirect, request, session

require = Blueprint('require', __name__)


@require.before_request
def require_login():
    # allowed_routes = ['login', 'register', 'index', 'static', 'storage']
    allowed_routes = ['login']
    print('endpoint -->', request.endpoint)
    if request.endpoint not in allowed_routes and 'email' not in session:
        return redirect('/')
