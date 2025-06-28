@app.route('/send-cratio-lead', methods=['POST'])
def send_cratio_lead():
    try:
        # Incoming JSON payload (single object)
        lead_data = request.get_json()

        # Wrap inside "records": [ ... ]
        payload = {
            "records": [lead_data]
        }

        # Cratio API endpoint
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
