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


