"""Lists page."""
from organiser.decorators import login_required

@login_required(template_file='lists.html')
async def list_handler(request):
    """Calendar page."""
    successes = []
    errors = []
    return {
        'successes': successes,
        'errors': errors}
