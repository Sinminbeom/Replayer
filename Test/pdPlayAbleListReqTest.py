import socketio

from App.Protocols.Messages.dataClass.pdPlayAbleListPacket import pdPlayAbleListReq


def main():

    sio = socketio.Client()

    @sio.event
    def connect():
        print("Connected to the server")

    @sio.event
    def disconnect():
        print("Disconnected from the server")

    def send_message_to_server(message):
        sio.emit('message', message)

    sio.connect('http://localhost:9999')

    send_message_to_server("""{"protocol_id": "PD_100", "message_direction": 1, "sender": "UI", "receiver": "REST_SERVER", "vehicleId": "e-100", "sensorIdList": ["LIDAR"], "startTime": "20230602000000", "endTime": "20230602000115"}""")

    sio.wait()
    pass

if __name__ == '__main__':
    main()