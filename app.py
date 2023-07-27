# importing all of the needed libraries
from flask import Flask, request
from backup import backup_folder
from data import get_log, get_stat

#naming flask app
app = Flask(__name__)

#defining the route for log
@app.route('/log')
def log():
    try:
        start = request.args.get('start')
        end = request.args.get('end')

        logs = get_log(start, end)
        response = logs
        return response
    except ValueError:
        response = "Invalid Dates"
        return response, 400

#definiitng stat function
@app.route('/stat')
def stat():
    stats = get_stat()
    response = stats
    return response

#defining backup function
@app.route('/', methods=['POST'])
def backup():
    folder_to_backup = request.json["path"]
    try:
        if folder_to_backup is None:
            response = "No folder path supplied"
            return response, 400

        backup_folder(folder_to_backup)
        response = "Backup completed"
        return response, 201
    except ValueError:
        response = "No such folder: " + folder_to_backup
        return response, 404


if __name__ == '__main__':
    app.run(host='0.0.0.0')
