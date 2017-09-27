import re
from datetime import datetime
import telepot

bot = telepot.Bot('414837932:AAEpfVfWSiXvArmVMwY0kV9xUl07fFIaXN0')

try:
    from html import escape as escape_html  # noqa: F401
except ImportError:
    from cgi import escape as escape_html  # noqa: F401

# Not using future.backports.datetime here as datetime value might be an input from the user,
# making every isinstace() call more delicate. So we just use our own compat layer.
if hasattr(datetime, 'timestamp'):
    # Python 3.3+
    def _timestamp(dt_obj):
        return dt_obj.timestamp()
else:
    # Python < 3.3 (incl 2.7)
    from time import mktime

    def _timestamp(dt_obj):
        return mktime(dt_obj.timetuple())


def escape_markdown(text):
    """Helper function to escape telegram markup symbols."""
    escape_chars = '\*_`\['
    return re.sub(r'([%s])' % escape_chars, r'\\\1', text)


def to_timestamp(dt_obj):
    """
    Args:
        dt_obj (:class:`datetime.datetime`):
    Returns:
        int:
    """
    if not dt_obj:
        return None

    return int(_timestamp(dt_obj))


def from_timestamp(unixtime):
    """
    Args:
        unixtime (int):
    Returns:
        datetime.datetime:
    """
    if not unixtime:
        return None

    return datetime.fromtimestamp(unixtime)


def mention_html(user_id, name):
    """
    Args:
        user_id (:obj:`int`) The user's id which you want to mention.
        name (:obj:`str`) The name the mention is showing.
    Returns:
        :obj:`str`: The inline mention for the user as html.
    """
    if isinstance(user_id, int):
        return '<a href="tg://user?id={}">{}</a>'.format(user_id, escape_html(name))


def mention_markdown(user_id, name):
    """
    Args:
        user_id (:obj:`int`) The user's id which you want to mention.
        name (:obj:`str`) The name the mention is showing.
    Returns:
        :obj:`str`: The inline mention for the user as markdown.
    """
    if isinstance(user_id, int):
        return '[{}](tg://user?id={})'.format(escape_markdown(name), user_id)
