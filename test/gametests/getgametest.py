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
    def test_getgames_can_return(self):
        rv = self.app.get('/getgames')
        assert str(rv.data).__len__() > 0
    def test_getgames_with_wrong_method(self):
        rv = self.app.get('/getgames')
        assert 'Method Not Allowed' in rv.data
    def test_getgames_with_wrong_id(self):
        rv = self.app.post('/getgames', data=dict(
        id="wrong id"
    ), follow_redirects=True)
        assert rv.data == ''
    def test_getgames_with_right_id(self):
        rv = self.app.post('/getgames', data=dict(
        id="fb8dc787-f9fb-475c-a272-2b82cac043cc"
    ), follow_redirects=True)
        assert "id" in rv.data
        assert "sid" in rv.data

