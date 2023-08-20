from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
from flask_cors import CORS

from config import API_KEY
from mail import send_mail
from gsheets import add_to_google_sheets

app = Flask(__name__)
CORS(app)

bp = Blueprint('bp', __name__)
app.register_blueprint(bp, url_prefix='/')


# Before Request
@bp.before_request
def before_request():
    # Check if argument api_key equal to API_KEY
    if request.args.get('api_key') != API_KEY:
        return 'Invalid API Key'


@bp.route('/api/v1/send')
def send():
    print('Received request...')

    # Get the request body
    data = request.get_json()
    name = data['name']
    adults = data['adults']
    children = data['children']
    phone = data['phone']
    email = data['email']
    acceptance = 'Yes' if data['acceptance'] else 'No'
    recommendations = data['recommendations']
    guest_names = ', '.join(data['guestNames'])

    subject = f"RSVP from {name}"
    contents = [
        f"Name: {name}",
        f"Number of adults: {adults}",
        f"Number of children: {children}",
        f"Phone: {phone}",
        f"Email: {email}",
        f"Acceptance: {acceptance}",
        f"Recommendations: {recommendations}",
        f"Guest names: {guest_names}"
    ]

    # Send email
    send_mail(subject, '\n'.join(contents))

    # Add to Google Sheets
    add_to_google_sheets(contents)

    return 'Success'

if __name__ == '__main__':
    app.run()
