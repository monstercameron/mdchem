from flask import Blueprint, render_template, request

simple_page = Blueprint('simple_page', __name__, template_folder='templates')


@simple_page.route('/')
def show():
    title = 'MDCHEM!'
    return render_template('index.html', title=title)
