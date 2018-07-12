def test_can_import_package():
    import flask_materialize


def test_can_initialize_app_and_extesion():
    from flask import Flask
    from flask_materialize import Material

    app = Flask(__name__)
    Material(app)
