from flask import Flask, request, jsonify
import threading 


app = Flask(__name__) 

monitors=[] 

def timout(device_id):
    for monitor in monitors:
        if monitor['id']==device_id:
            monitor["status"]="down" 
    print({
        "ALERT":f"Device {device_id} is down",
        "time":f"{device_id} has not checked in for 5 minutes" 
    }) 
            
@app.route('/monitor', methods=['POST']) 
def monitor():
    data=request.get_json() 

    monitor.append({
        "id":device_id,
        "timeout":timeout,
        "alert":alert,
    })

    device_id = data["device_id"]
    timeout = data["timeout"]
    alert = data["alert"] 

    timer=threading.Timer(timeout, timout, args=[device_id]) 
    timer.start() 

    print(f"Monitoring {device_id} for {timeout} seconds")

    return jsonify({"message": f"Monitoring {device_id} created for {timeout} seconds"}), 201


if __name__ == '__main__':  
    app.run(debug=True)