from flask_assets import Environment, Bundle
from app import app

bundles = {

    'base_js': Bundle(
        'js/base.js', 
        filters='jsmin',
        output='gen/base/base.js'),

    'base_css': Bundle(
        'css/base.css',
        filters='cssmin',
        output='gen/base/base.css'),

    'bars_css': Bundle(
        'css/bars.css',
        filters='cssmin',
        output='gen/bars/bars.css'),

    'index_js': Bundle(
        'js/index.js',
        filters='jsmin',
        output='gen/index/index.js'),

    'index_css': Bundle(
        'css/index.css',
        filters='cssmin',
        output='gen/index/index.css'),

    'about_js': Bundle(
        'js/about.js',
        filters='jsmin',
        output='gen/about/about.js'),

    'about_css': Bundle(
        'css/about.css',
        filters='cssmin',
        output='gen/about/about.css'),

    'applications_js': Bundle(
        'js/applications.js',
        filters='jsmin',
        output='gen/applications/applications.js'),

    'applications_css': Bundle(
        'css/applications.css',
        filters='cssmin',
        output='gen/applications/applications.css'),

    'blog_js': Bundle(
        'js/blog.js',
        filters='jsmin',
        output='gen/blog/blog.js'),

    'blog_css': Bundle(
        'css/blog.css',
        filters='cssmin',
        output='gen/blog/blog.css'),

    'contact_js': Bundle(
        'js/contact.js',
        filters='jsmin',
        output='gen/contact/contact.js'),

    'contact_css': Bundle(
        'css/contact.css',
        filters='cssmin',
        output='gen/contact/contact.css'),

    'join_js': Bundle(
        'js/join.js',
        filters='jsmin',
        output='gen/join/join.js'),

    'join_css': Bundle(
        'css/join.css',
        filters='cssmin',
        output='gen/join/join.css'),

    'positions_js': Bundle(
        'js/positions.js',
        filters='jsmin',
        output='gen/positions/positions.js'),

    'positions_css': Bundle(
        'css/positions.css',
        filters='cssmin',
        output='gen/positions/positions.css'),


    'technology_js': Bundle(
        'js/technology.js',
        filters='jsmin',
        output='gen/technology/technology.js'),

    'technology_css': Bundle(
        'css/technology.css',
        filters='cssmin',
        output='gen/technology/technology.css')

}

assets = Environment(app)
assets.register(bundles)
