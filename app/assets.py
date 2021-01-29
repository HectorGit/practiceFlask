from flask_assets import Environment, Bundle
from app import app

# Assets bundle together files for deployment to limit number of requests. Files also get minified in the process

bundles = {
    # 'base_js': Bundle( # Name of Bundle
    #     'js/mobile/mobile.js',
    #     'js/base.js', # files to include in bundle
    #     filters='jsmin', # Minification filter
    #     output='gen/base/base.js'), #Output the asset file to /gen folder

    # 'base_css': Bundle(
    #     'css/base.css',
    #     'css/mobile.css',
    #     'css/cart.css',
    #     filters='cssmin',
    #     output='gen/base/base.css'),

    'index_js': Bundle(
        # 'js/konami.js',
        'js/index.js',
        filters='jsmin',
        output='gen/index/index.js'),

    'index_css': Bundle(
        'css/index.css',
        filters='cssmin',
        output='gen/index/index.css'),
 
}


assets = Environment(app)

assets.register(bundles)
