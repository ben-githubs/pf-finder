from flask import Blueprint
from flask import current_app as app

home_bp = Blueprint(
    'main_bp', __name__,
    template_folder = 'templates',
    static_folder = 'static'
)

@home_bp.route('/', methods=['GET', 'POST'])
def home():
    """This is the homepage"""

    return "Home!"