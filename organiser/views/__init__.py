"""Index page."""
from organiser.decorators import login_required

@login_required(template_file='index.html')
async def index_handler(request):
    """Index page."""
    successes = []
    errors = []
    return {
        'successes': successes,
        'errors': errors}
