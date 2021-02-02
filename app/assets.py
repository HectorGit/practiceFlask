from flask_assets import Environment, Bundle
from app import app

bundles = {
    'index_js': Bundle(
        'js/index.js',
        filters='jsmin',
        output='gen/index/index.js'),

    'index_css': Bundle(
        'css/index.css',
        filters='cssmin',
        output='gen/index/index.css')
}

assets = Environment(app)
assets.register(bundles)
