from flask import Flask, request, jsonify
import threading 


app = Flask(__name__) 

monitors=[] 

def device_timout(device_id):
    for monitor in monitors:
        if monitor['id']==device_id:
            monitor["status"]="down" 
    print({
        "ALERT":f"Device {device_id} is down",
        "time":f"{device_id} has not checked in for 5 minutes" 
    }) 
            

# Register device
@app.route("/moniter", methods=["POST"])
def Monisters():

    data = request.get_json()

    device_id = data["device_id"]
    timeout = data["timeout"]
    alert = data["alert"]

    timer = threading.Timer(timeout, device_timout, args=[device_id])
    timer.start()

    new_moniter = {
        "id": device_id,
        "timeout": timeout,
        "alert": alert,
        "timer": timer, 
        "status": "ACTIVE"
    }

    monitors.append(new_moniter)

    print(f"Monitoring {device_id} for {timeout} seconds")

    return jsonify({"message": f"Monitoring {device_id} created for {timeout} seconds"}), 201


# Heartbeat endpoint
@app.route("/moniter/<id>/heartbeat", methods=["POST"])
def heartbeat(id):
    for moniter in monitors:

        if moniter["id"] == id:

            # cancel old timer if running
            if moniter["timer"]:
                moniter["timer"].cancel()

            # start new timer
            timer = threading.Timer(moniter["timeout"], device_timout, args=[id])
            timer.start()

            moniter["timer"] = timer
            moniter["status"] = "Alive"

            print(f"Heartbeat received from {id}, timer reset")

            return jsonify({"message": f"Heartbeat received from {id}"}), 200

    return jsonify({"error": "Device not found"}), 404 




if __name__ == '__main__':  
    app.run(debug=True)