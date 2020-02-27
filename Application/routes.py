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
def index( ):
    """Renders the home page."""
    return render_template(
        'index.html' ,
        title = 'Athena' ,
        index = True
    )

@app.route( '/' )
@app.route( '/lstHistorias' )
def lstHistorias( ):
    return render_template(
        'lstHistorias.html' ,
        title = 'Athena',
        lstHistorias = True
    )




