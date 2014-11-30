# -*- coding: UTF-8 -*-

import os
from flask import Flask, g, request, flash, redirect, session
from config import config
from flask.ext.babel import Babel

babel = Babel()

def create_app(config_name):
    app = Flask(__name__)


    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    babel.init_app(app)

    from .mod_main import mod_main as main_blueprint
    app.register_blueprint(main_blueprint,url_prefix='/<lang_code>')

    # If someone navigates to the site domain without the lang code
    # we append the lang code to the request url and redirect

    @app.before_request
    def before_request():
        if request.view_args==None:
            if not 'lang_code' in session.keys():
                return redirect('/fr' + request.full_path)
            else:
                return redirect('/'+session['lang_code']+request.full_path)


    @app.context_processor
    def inject_lang():
        return dict(sess_lang=session['lang_code'])

    @babel.localeselector
    def get_locale():
        #session['lang_code']=request.accept_languages.best_match()
        g.lang_code = session['lang_code']
        return g.get('lang_code', 'fr')


    return app
