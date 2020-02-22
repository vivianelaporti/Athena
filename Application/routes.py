from Application import app

from datetime import datetime
from flask import render_template

# @app.route( '/' )
# @app.route( '/index' )
# def index( ):
#     """Renders the home page."""
#     return render_template(
#         'index.html' ,
#         title = 'Athena' ,
#         # year = datetime.now( ).year
#         index = True
#     )

@app.route( '/' )
@app.route( '/index' )
def lstHistorias( ):
    """Renders the home page."""
    return render_template(
        'index.html' ,
        title = 'Athena' ,
        # year = datetime.now( ).year
        index = True
    )