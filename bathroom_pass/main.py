from flask import Flask, render_template, request, jsonify
import threading
import requests
import json
import serial  # Import pyserial for serial communication

from static.assets.api.assets import javaURI

app = Flask(__name__)

# Static queue data (replace with a dynamic backend)
queue = ["John Mortensen", "Srijan Atti"]
current_user = ""
next_up = "Matthew Wakayama"

def barcode_reader():
    ss = ""
    print("Ready to scan a barcode. Please scan now.")
    
    while True:
        # Read the barcode input from the terminal directly as a string
        barcode_input = input()  # This captures whatever is typed into the terminal (barcode)
        
        if barcode_input:
            ss = barcode_input.strip()  # Capture the barcode input into ss
            
            print(f"Scanned barcode: {ss}")  # Print out the scanned barcode
            
            # Simulate finishing the scan (i.e., sending the barcode when Enter is pressed)
            print(f"Final scanned barcode: {ss}")
            
            # Assuming you need to do something with the scanned value:
            name = get_name_by_sid(ss)  # Fetch the name using the scanned SID
            
            # Call a function to add to the queue or handle further logic
            add_to_queue("jmort1021@gmail.com", name, javaURI)
            
            # Return the scanned barcode
            return ss
        else:
            print("No input detected. Please scan again.")


def send_barcode_to_server(student_id):
    """Send barcode data to Flask endpoint"""
    url = f"{javaURI}/api/queue/add"
    data = {"student_id": student_id}

    try:
        response = requests.post(url, json=data)
        print(f"Sent {student_id} to server: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending barcode: {e}")

def barcode_listener():
    """Continuously listens for barcode scans and sends them to the Flask server."""
    while True:
        student_id = barcode_reader()
        send_barcode_to_server(student_id)

def get_name_by_sid(sid):
    url = f"http://localhost:8085/api/{sid}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Data fetched successfully:", response.json())
            return response.json()
        else:
            print(f"GET request failed {response.status_code}: {response.text}")
    except requests.exceptions.RequestException as e:
        print("Error during GET request:", e)

def add_to_queue(teacherEmail, studentName, uri):
    payload = {
        "studentName": studentName,
        "teacherEmail": teacherEmail,
        "uri": uri
    }
    url = "http://localhost:8085/api/queue/add"
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 201:
            print("Data posted successfully: ", response.json())
        else:
            print(f"POST request failed with status code {response.status_code}: {response.text}")
    except requests.exceptions.RequestException as e:
        print("Error during POST request:", e)
    
@app.route('/')
def home():
    return render_template('index.html', current_user=current_user, next_up=next_up, queue=queue)

@app.route('/scan', methods=['POST'])
def scan_barcode():
    """Handles barcode scans"""
    global current_user, next_up, queue

    data = request.get_json()
    scanned_id = data.get("student_id")

    if scanned_id:
        print(f"Scanned ID: {scanned_id}")
        # Update queue logic
        current_user = next_up
        if queue:
            next_up = queue.pop(0)
        else:
            next_up = "Nobody"

        return jsonify({"message": "Queue updated", "current_user": current_user, "next_up": next_up, "queue": queue})
    
    return jsonify({"error": "Invalid scan"}), 400

if __name__ == '__main__':
    # Start barcode listening thread
    threading.Thread(target=barcode_listener, daemon=True).start()
    
    # Run Flask app
    app.run(port=4100, debug=True)
