from .flaskr import app
from userapi import user_blue_print
from gameapi import game_blue_print
app.register_blueprint(user_blue_print)
app.register_blueprint(game_blue_print)
