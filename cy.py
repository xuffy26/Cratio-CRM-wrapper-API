from flask import Flask, request, jsonify
import requests
import os

# Define app before using @app.route
app = Flask(__name__)

@app.route('/send-cratio-lead', methods=['POST'])
def send_cratio_lead():
    try:
        lead_data = request.get_json()
        payload = {
            "records": [lead_data]
        }

        cratio_url = "https://apps.cratiocrm.com/api/apirequest.php?operation=insertRecords&formname=Leads&apikey=NF8xXzMwNTYkQDM5NSMjMjAyNC0xMi0yNyAxNTo0NTowMA%3D%3D"

        response = requests.post(
            cratio_url,
            json=payload,
            headers={"Content-Type": "application/json"}
        )

        return jsonify({
            "status": response.status_code,
            "response": response.json()
        }), response.status_code

    except Exception as e:
        return jsonify({"status": 500, "error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
