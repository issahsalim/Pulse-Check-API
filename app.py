from flask import Flask, request, jsonify
import threading 
import time 

app = Flask(__name__) 

monitors=[] 

def device_timout(device_id):
    for monitor in monitors:
        if monitor['id']==device_id:
            monitor["status"]="down" 
    print({
        "ALERT":f"Device {device_id} is down",
        "time":time.strftime("%H:%M:%S %Y-%m-%d" )
    }) 
            

# Register device
@app.route("/monitors", methods=["POST"])
def Monisters():

    data = request.get_json()

    device_id = data["device_id"]
    timeout = data["timeout"]
    alert = data["alert"]
    
    for monitor in monitors:
        if monitor["id"]== device_id: 
            return jsonify ({"message":"Device already exist"})

    timer = threading.Timer(timeout, device_timout, args=[device_id])
    timer.start()

    new_moniter = {
        "id": device_id,
        "timeout": timeout,
        "alert": alert, 
        "timer": timer, 
        "status": "Alive"
    }

    
    monitors.append(new_moniter)

    print(f"Monitoring {device_id} for {timeout} seconds")

    return jsonify({"message": f"Monitoring {device_id} created for {timeout} seconds"}), 201


# Heartbeat endpoint
@app.route("/monitors/<id>/heartbeat", methods=["POST"])
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

# pause endpoint
@app.route("/monitors/<id>/pause", methods=["POST"]) 
def Pause(id): 
    for moniter in monitors: 
        if moniter["id"]==id: 
            moniter["timer"].cancel() 
            moniter["status"]="paused"  
            print(f"Device {id} successfully paused") 
            return jsonify({"message": f"Monitor Device {id} successfully paused"}), 200 
        
    return jsonify({"message":"device not found"}), 404 


# MY OWN FEATURE: checking all devices status 
@app.route("/monitors/devices-status", methods=["GET"])  
def devices_status(): 
    status_info=   []
    for monitor in monitors: 
        if monitor["status"]=="Alive": 
            status="Alive" 
        elif monitor["status"]=="paused":
            status="Paused" 
        else:
            status="Down"  
        
        
        status_info.append({
                    "device_id": monitor["id"], 
                    "status": status,
                    
        }) 

        print("\n\n Curent Devices Status:") 
        print(status_info) 

    return jsonify({"devices_status": status_info}), 200


# update timer
@app.route("/monitors/<device_id>/timeout", methods=["PUT"])
def update_timeout(device_id):

    data = request.get_json()
    new_timeout = data["timeout"]

    for monitor in monitors:
        if monitor["id"] == device_id:

            # stop old timer
            monitor["timer"].cancel()

            # update timeout
            monitor["timeout"] = new_timeout

            # start new timer
            timer = threading.Timer(new_timeout, device_timout, args=[device_id])
            timer.start()

            monitor["timer"] = timer

            return jsonify({
                "message": f"Timeout for {device_id} updated to {new_timeout} seconds"
            }), 200

    return jsonify({"message": "Device not found"}), 404


if __name__ == '__main__':  
    app.run(debug=True)