import mysql.connector as mariadb
from flask import Flask, send_file
from flask import render_template
from flask_login import current_user, LoginManager
from mysql.connector import errorcode
from user import user_utils
from data_files import database

from predictions import table_predictions, booking_predictions, match_predictions, stats_predictions
"""
try:
    db_connection = mariadb.connect(user='root', password='V3z?RnzC', host='localhost', database='analyzer')
    db_cursor = db_connection.cursor()
    print("Successful connection")
except mariadb.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
"""
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.before_request
def clear_trailing():
    from flask import redirect, request
    rp = request.path
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])


@app.route('/')
def home():
    return render_template('index.html')


# User Profile Page
@app.route('/profile/<username>')
def profile(username):
    # Maybe optimize user checking with extra time
    db_connection = database.connect()
    db_cursor = db_connection.cursor()
    db_cursor.execute(f'select * from users where username="{username}"')
    db_cursor.fetchone()
    if db_cursor.rowcount == 0:
        return "User not found"
    else:
        return render_template('profile.html', username=username)


@app.route('/profile/<username>/table_predictions')
def user_table_predictions(username):
    db_connection = database.connect()
    db_cursor = db_connection.cursor()
    db_cursor.execute(f'select * from users where username="{username}"')
    db_cursor.fetchone()

    # Implement check for authentication to pass through to table_predictions.html later
    # For adding table add/edit/delete functionality.

    if db_cursor.rowcount == 0:
        return "User not found"
    else:
        # Need to implement error checks
        db_cursor.execute(f'select * from table_predictions')
        user = user_utils.find_by_username(username)
        predictions = table_predictions.find_public_predictions(user[0])

        return render_template('table_predictions.html', username=username, predictions=predictions)


@app.route('/profile/<username>/table_predictions/<prediction_name>')
def user_selected_table_prediction(username, prediction_name):
    db_connection = database.connect()
    db_cursor = db_connection.cursor()
    db_cursor.execute(f'select * from users where username="{username}"')
    db_cursor.fetchone()

    if db_cursor.rowcount == 0:
        return "User not found"
    else:
        prediction = table_predictions.find_prediction_by_username_and_name(username, prediction_name)
        if prediction is None:
            return "Prediction does not exist"
        return render_template('show_table_pred.html', username=username, prediction_name=prediction_name, prediction=prediction)


@app.route('/profile/<username>/table_predictions/<prediction_name>/download')
def download_table(username, prediction_name):
    path = table_predictions.export(username, prediction_name)
    if path is None:
        return 'Prediction does not exist'
    return send_file(path, as_attachment=True)


@app.route('/profile/<username>/booking_predictions')
def user_booking_predictions(username):
    user = user_utils.find_by_username(username)
    if user is None:
        return 'User not found'
    predictions = booking_predictions.find_public_predictions_by_username(username)
    if predictions is None:
        return "Prediction does not exist"
    return render_template('booking_predictions.html', predictions=predictions, username=username)


@app.route('/profile/<username>/booking_predictions/download')
def download_bookings(username):
    path = booking_predictions.export(username)
    if path is None:
        return "Prediction does not exist"
    return send_file(path, as_attachment=True)


@app.route('/profile/<username>/match_predictions')
def user_match_predictions(username):
    user = user_utils.find_by_username(username)
    if user is None:
        return 'User not found'

    predictions = match_predictions.find_public_predictions(user[0])
    return render_template('match_predictions.html', username=username, predictions=predictions)


@app.route('/profile/<username>/match_predictions/<prediction_name>')
def user_selected_match_prediction(username, prediction_name):
    user = user_utils.find_by_username(username)
    if user is None:
        return 'User not found'

    prediction = match_predictions.find_prediction_by_username_and_name(username, prediction_name)
    if prediction is None:
        return "Prediction does not exist"
    stats = stats_predictions.find_stats(prediction[4])

    return render_template('show_match_pred.html', prediction_name=prediction_name, stats=stats, prediction=prediction, username=username)


@app.route('/profile/<username>/match_predictions/<prediction_name>/download')
def download_match_pred(username, prediction_name):
    path = match_predictions.export(username, prediction_name)
    if path is None:
        return "Prediction does not exist"
    return send_file(path, as_attachment=True)


@app.route('/add_table_prediction')
def add_match_prediction():
    return f'nothing'


@app.route('/php')
def php():
    from subprocess import call
    call(["php", "/php/match_prediction.php"])


@app.route('/auth')
def auth_check():
    user = user_utils.find_by_email("test@test.com")
    return 'Test'


if __name__ == '__main__':
    #login_manager = LoginManager()
    #login_manager.init_app(app)
    #login_manager.login_view = 'login'

    app.run()
