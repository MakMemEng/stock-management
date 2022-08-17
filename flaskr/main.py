from flaskr import app
from flask import render_template


@app.route('/')
def index():
    materials = [
        {'name': 'MCL-E67',
         'inventory': 251,
         'price': 5017},
        {'name': 'SPB-AK',
         'inventory': 12,
         'price': 684}
    ]
    return render_template(
        'index.html',
        materials=materials
    )
