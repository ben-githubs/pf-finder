from flask import Blueprint
from flask import current_app as app

from . import models as m

entries_bp = Blueprint(
    'entries_bp', __name__,
    template_folder = 'templates',
    static_folder = 'static'
)

@entries_bp.route('/search', methods=['GET', 'POST'])
def search():
    """This is the page for searching items, spells, etc."""

    return "Search Page!"