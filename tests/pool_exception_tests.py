"""
Tests for Exceptions in queries.pool

"""
import mock
try:
    import unittest2 as unittest
except ImportError:
    import unittest
import uuid

from queries import pool


class ActivePoolErrorTestCase(unittest.TestCase):

    def setUp(self):
        self.pid = uuid.uuid4()
        self.exception = pool.ActivePoolError(self.pid)

    def test_pid_is_assigned(self):
        self.assertEqual(self.exception.pid, self.pid)

    def test_str_value(self):
        expectation = 'Pool {0!s} has at least one active connection'.format(self.pid)
        self.assertEqual(str(self.exception), expectation)


class ConnectionBusyErrorTestCase(unittest.TestCase):

    def setUp(self):
        self.cid = uuid.uuid4()
        self.exception = pool.ConnectionBusyError(self.cid)

    def test_cid_is_assigned(self):
        self.assertEqual(self.exception.cid, self.cid)

    def test_str_value(self):
        expectation = 'Connection {0!s} is busy'.format(self.cid)
        self.assertEqual(str(self.exception), expectation)


class ConnectionNotFoundErrorTestCase(unittest.TestCase):

    def setUp(self):
        self.pid = uuid.uuid4()
        self.cid = uuid.uuid4()
        self.exception = pool.ConnectionNotFoundError(self.pid, self.cid)

    def test_cid_is_assigned(self):
        self.assertEqual(self.exception.cid, self.cid)

    def test_pid_is_assigned(self):
        self.assertEqual(self.exception.pid, self.pid)

    def test_str_value(self):
        expectation = 'Connection {0!s} not found in pool {1!s}'.format(self.cid,
                                                              self.pid)
        self.assertEqual(str(self.exception), expectation)


class NoIdleConnectionsErrorTestCase(unittest.TestCase):

    def setUp(self):
        self.pid = uuid.uuid4()
        self.exception = pool.NoIdleConnectionsError(self.pid)

    def test_pid_is_assigned(self):
        self.assertEqual(self.exception.pid, self.pid)

    def test_str_value(self):
        expectation = 'Pool {0!s} has no idle connections'.format(self.pid)
        self.assertEqual(str(self.exception), expectation)


class PoolFullErrorTestCase(unittest.TestCase):

    def setUp(self):
        self.pid = uuid.uuid4()
        self.exception = pool.PoolFullError(self.pid)

    def test_pid_is_assigned(self):
        self.assertEqual(self.exception.pid, self.pid)

    def test_str_value(self):
        expectation = 'Pool {0!s} is at its maximum capacity'.format(self.pid)
        self.assertEqual(str(self.exception), expectation)
