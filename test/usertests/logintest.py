import os
import flaskr.flaskr.flaskr as flaskr
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.testing = True
        self.app = flaskr.app.test_client()
        with flaskr.app.app_context():
            flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])
    def test_login_can_return(self):
        rv = self.app.get('/login')
        assert str(rv.data).__len__() > 0
    def test_login_with_wrong_method(self):
        rv = self.app.get('/login')
        assert b'231' in rv.data
    def test_login_with_not_exitst_user(self):
        rv = self.app.post('/login', data=dict(
        name="notexistuser",
        psw="1"
    ), follow_redirects=True)
        assert b'230' in rv.data
    def test_login_with_wrong_psw(self):
        rv = self.app.post('/login', data=dict(
        name="u3shadow",
        psw="1234"
    ), follow_redirects=True)
        assert b'230' in rv.data
    def test_login_with_right_info(self):
        rv = self.app.post('/login', data=dict(
        name="u3shadow",
        psw="1"
    ), follow_redirects=True)
        assert b'200' in rv.data
        assert b'id' in rv.data
