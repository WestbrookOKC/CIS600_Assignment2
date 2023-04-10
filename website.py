from flask import Flask, render_template, request
import boto3
from datetime import datetime, timedelta

app = Flask(__name__)

# Set up the DynamoDB client
dynamodb = boto3.resource('dynamodb', aws_access_key_id='AKIAZAS5CYFQRUYRKDVA', aws_secret_access_key='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', region_name='us-east-2')
table = dynamodb.Table('wx_data')

# Set the timestamp threshold
time_threshold = datetime.now() - timedelta(hours=5)

# @app.route('/station_2')
# def home():
#     response = table.scan()
#     items = response['Items']
#
#     # data = []
#     # for item in items:
#     #     data.append(item['device_data'])
#     # print(len(data))
#     data = []
#     for item in items:
#         if(item['device_data']['station_id'] == 'station-2'):
#             data.append(item['device_data'])
#
#     # Sort the data based on the timestamp
#     data = sorted(data, key=lambda x: x['timestamp'], reverse=True)
#
#     # Select the latest value
#     latest_data = data[0]
#
#     return render_template('home.html', items=latest_data)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sensor_data', methods=['POST'])
def sensor_data():
    sensor_name = request.form['sensor_name']
    time_threshold = datetime.now() - timedelta(hours=5)
    response = table.scan()
    items = response['Items']
    print(sensor_name)
    print(type(sensor_name))
    # Filter data based on the sensor name and timestamp
    data = []
    for item in items:
        device_data = item['device_data']
        timestamp_str = device_data['timestamp']
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f')
        if  timestamp > time_threshold and sensor_name in device_data:
            data.append({
                'station_id': device_data['station_id'],
                'timestamp': device_data['timestamp'],
                'value': device_data[sensor_name]
            })

    # Sort the data based on the timestamp
    data = sorted(data, key=lambda x: x['timestamp'], reverse=True)
    print(data)
    return render_template('sensor_data.html', sensor_name=sensor_name, data=data)




@app.route('/station_2')
def station_2():
    response = table.scan()
    items = response['Items']

    data = []
    for item in items:
        if(item['device_data']['station_id'] == 'station-2'):
            data.append(item['device_data'])

    # Sort the data based on the timestamp
    data = sorted(data, key=lambda x: x['timestamp'], reverse=True)

    # Select the latest value
    latest_data = data[0]

    return render_template('home.html', items=latest_data)

@app.route('/station_1')
def station_1():
    response = table.scan()
    items = response['Items']

    data = []
    for item in items:
        if(item['device_data']['station_id'] == 'station-1'):
            data.append(item['device_data'])

    # Sort the data based on the timestamp
    data = sorted(data, key=lambda x: x['timestamp'], reverse=True)

    # Select the latest value
    latest_data = data[0]

    return render_template('home2.html', items=latest_data)





# Run the application
if __name__ == '__main__':
    app.run(debug=True)
