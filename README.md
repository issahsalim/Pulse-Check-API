## 8. Documentation Requirements
Your final `README.md` must replace these instructions. It must cover:

1.  **Architecture Diagram** 

![Architecture Diagram](ArchitectureDiagram.png)




2.  **Setup Instructions** 
## Setup Instructions

Follow these steps to run the project on your computer.

### 1. Clone the Repository

After cloning the repo,

Move into the project folder:

```bash
cd Pulse-Check-API
```

---

### 2. Install Dependencies

Make sure Python is installed on your computer.

Install the required packages:

```bash
pip install -r requirements.txt
```

This project uses the following main package:

* Flask

---

### 3. Run the Server

Start the application:

open the built-in terminal by pressing(cntrl + `) if you are using vscode, or open cmd and cd into 
the folder when the project exist and type the below command. 

```bash
python app.py
```

If everything works correctly, you should see something like:

```
* Running on http://127.0.0.1:5000
```

---

### 4. Test the API

You can test the endpoints using **curl** or **Postman**.

Example: To register a device, open cmd(specifically) and paste the below url command 

curl -X POST http://127.0.0.1:5000/monitor -H "Content-Type: application/json" -d "{\"device_id\":\"device-1\",\"timeout\":10,\"alert\":\"salim@gmail.com\"}"




This will create a new monitor and start tracking the device.

---

### 5. Stop the Server

Press:
```
CTRL + C
```
to stop the server. 




3.  **API Documentation** 

This API monitors remote devices using a **Dead Man’s Switch** mechanism.
Each device registers with a timeout and must send periodic heartbeats.
If the heartbeat is not received before the timeout expires, the system triggers an alert.

Base URL:

```
http://127.0.0.1:5000
```

---

# 1. Register a Monitor

This endpoint registers a new device and starts a monitoring timer.

### Endpoint

```
POST /moniter
```

### Request Body

```json
{
  "device_id": "device-1",
  "timeout": 10,
  "alert": "admin@email.com"
}
```

### Curl Test

```
curl -X POST http://127.0.0.1:5000/moniter -H "Content-Type: application/json" -d "{\"device_id\":\"device-1\",\"timeout\":10,\"alert\":\"salim@gmail.com\"}"

```

### Response

```
201 Created
``` 

```json
{
  "message": "Monitoring (device_id) created for it (timeout)"
}
```

### What Happens

1. The device is registered.
2. A timer starts with the specified timeout.
3. If the timer reaches zero, an alert is triggered.

---


# 2. Send Heartbeat
Devices must periodically send a heartbeat to reset the timer.

### Endpoint

```
POST /moniter/{device_id}/heartbeat
```

### Example

```
POST /moniter/device-1/heartbeat
```

### Curl Test

```
curl -X POST http://127.0.0.1:5000/moniter/device-1/heartbeat
```

### Response

```
200 OK
```

```json
{
  "message": "Heartbeat received"
}
```

### What Happens

1. The system checks if the device exists.
2. The current timer is cancelled.
3. A new timer starts again from the beginning.

---

# 3. Pause Monitoring

This endpoint pauses monitoring for a device.

This is useful when a technician is repairing the device.

### Endpoint

```
POST /moniter/{device_id}/pause
```

### Example

```
POST /moniter/device-1/pause
```

### Curl Test

```
curl -X POST http://127.0.0.1:5000/moniter/device-1/pause
```

### Response

```
200 OK
```

```json
{
  "message": "Monitor paused"
}
```

### What Happens

1. The device timer is cancelled.
2. Monitoring is paused.
3. No alert will trigger while paused.

---

# 4. Get All Device Status (Developer’s Choice Feature)

This endpoint shows the status of all monitored devices.

### Endpoint

```
GET /moniter/devices-status
```

### Curl Test

```
curl http://127.0.0.1:5000/moniter/devices-status
```

### Response

```
200 OK
```

Example output:

```json
[
  {
    "device_id": "device-1",
    "status": "down"
  },
  {
    "device_id": "device-2",
    "status": "alive"
  },
  {
    "device_id": "device-3",
    "status": "pause"
  }
]
```

### What Happens

The system loops through all registered monitors and prints:

all devices status for instance:
 {
    "device_id": "device-3",
    "status": "pause"
  }


in the server console.

This allows administrators to quickly view the status of all devices.

---
