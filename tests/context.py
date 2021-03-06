"""
Add context for the tests

Changes the system directory allowing for importation
of modules in package
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import client.connection as connection
import server.clientcon as clientcon
