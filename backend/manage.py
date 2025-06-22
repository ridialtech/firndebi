#!/usr/bin/env python3
"""Test runner for backend unit tests."""
import os
import sys
import unittest

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    project_root = os.path.dirname(base_dir)
    sys.path.insert(0, project_root)
    suite = unittest.defaultTestLoader.discover(os.path.join(base_dir, 'tests'))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful())
