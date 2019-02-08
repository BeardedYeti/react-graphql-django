# File: ./backend/todo/tests/test_models.py

import pytest
from mixer.backend.django import mixer

# Writing to DB
pytestmark = pytest.mark.django_db

def text_message():
    obj = mixer.blend('todo.Message')
    assert obj.pk > 0

