"""Calendar page."""
from organiser.decorators import login_required

@login_required(template_file='calendar.html')
async def calendar_handler(request):
    """Calendar page."""
    successes = []
    errors = []
    return {
        'successes': successes,
        'errors': errors}
