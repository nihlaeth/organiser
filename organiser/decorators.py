"""Handy decorators."""
from functools import wraps
import aiohttp_login
from aiohttp_jinja2 import template

def login_required(template_file):
    """
    Require user to be logged in and pass necessary data for navigation bar.
    """
    def decorator(handler):
        @aiohttp_login.login_required
        @template(template_file)
        @wraps(handler)
        async def inner_decorator(request):
            result = await handler(request)
            return result
        return inner_decorator
    return decorator
