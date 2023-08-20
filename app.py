from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
from flask_cors import CORS

from config import API_KEY
from mail import send_mail, connect_mail
from gsheets import add_to_google_sheets, connect_google_sheets
from encryption import Decrypt_File

app = Flask(__name__)
CORS(app)

bp = Blueprint('bp', __name__)


# Before Request
@bp.before_request
def before_request():
    # Check if argument api_key equal to API_KEY
    if request.args.get('api_key') != API_KEY:
        return 'Invalid API Key'


@bp.route('/api/v1/send', methods=['POST'])
def send():
    print('Received request...')

    # Get the request body
    data = request.get_json()
    name = data['name']
    adults = data['adults']
    children = data['children']
    phone = data['phone'] if data['phone'] else 'N/A'
    email = data['email'] if data['email'] else 'N/A'
    acceptance = 'Yes' if data['acceptance'] else 'No'
    recommendations = data['recommendations'] if data['recommendations'] else 'N/A'
    guest_names = ', '.join(data['guestNames'])

    subject = f"RSVP from {name}"
    contents = [
        f"Name: {name}",
        f"Acceptance: {acceptance}",
        f"Number of adults: {adults}",
        f"Number of children: {children}",
        f"Phone: {phone}",
        f"Email: {email}",
        f"Guest names: {guest_names}",
        f"Recommendations: {recommendations}"
    ]

    # Send email
    smtp = connect_mail()
    send_mail(smtp, subject, '\n'.join(contents))

    Decrypt_File('service-account.bin', 'service-account.json')

    # Add to Google Sheets
    rows = [
        acceptance,
        name,
        adults,
        children,
        phone,
        email,
        guest_names,
        recommendations
    ]
    gsheets = connect_google_sheets()
    add_to_google_sheets(gsheets, rows)

    print('Request completed!')
    return 'Success'


app.register_blueprint(bp, url_prefix='/')


if __name__ == '__main__':
    app.run()
