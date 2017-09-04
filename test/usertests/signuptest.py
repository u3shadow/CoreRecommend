import json
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
    def test_signup_can_return(self):
        rv = self.app.get('/signup')
        assert str(rv.data).__len__() > 0

    def test_signup_with_wrong_method(self):
        rv = self.app.get('/signup')
        assert 'Method Not Allowed' in rv.data
    def test_signup_with_exist_user(self):
        rv = self.app.post('/signup', data=dict(
        name="u3shadow",
        psw="1",
        email="notusedemail"
    ), follow_redirects=True)
        assert '230' in rv.data
    def test_signup_with_exist_email(self):
        rv = self.app.post('/signup', data=dict(
        name="nousedname",
        psw="1",
        email="11@gmail.com"
    ), follow_redirects=True)
        assert '231' in rv.data
