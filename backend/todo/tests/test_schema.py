# File: ./backend/todo/tests/test_schema.py

import pytest
from mixer.backend.django import mixer

from .. import schema


pytestmark = pytest.mark.django_db


def test_message_type():
    instance = schema.MessageType()
    assert instance


def test_resolve_all_messages():
    mixer.blend('todo.Message')
    mixer.blend('todo.Message')
    q = schema.Query()
    res = q.resolve_all_messages(None)
    assert res.count() == 2, 'Should return all messages'

