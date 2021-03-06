#!/usr/bin/env python

"""Sample test module."""

import unittest


class Test{{cookiecutter.package_name | capitalize}}(unittest.TestCase):

    """Sample test class."""

    def test_dependency_import(self):
        """Sample test method."""
        try:
            import testpackage  # pylint: disable=W0612
            assert True
        except ImportError:
            self.fail()
