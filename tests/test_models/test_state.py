#!/usr/bin/python3
"""doc doc"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """doc doc"""

    def __init__(self, *args, **kwargs):
        """doc doc"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """doc doc"""
        new = self.value()
        self.assertEqual(type(new.name), str)
