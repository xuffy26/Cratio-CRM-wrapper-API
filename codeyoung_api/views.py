from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import logging

logger = logging.getLogger(__name__)

class CodeyoungLeadAPIView(APIView):
    def post(self, request):
        try:
            # 1. Get JSON body from POST request
            lead_data = request.data
            print("🟡 Incoming request data:", lead_data)

            # 2. Wrap it inside the required Cratio format
            payload = {
                "records": [lead_data]
            }
            print("🟡 Payload to Cratio:", payload)

            # 3. Cratio API URL with API key
            codeyoung_url = (
                "https://apps.cratiocrm.com/api/apirequest.php"
                "?operation=insertRecords&formname=Leads"
                "&apikey=NF8xXzMwNTYkQDM5NSMjMjAyNC0xMi0yNyAxNTo0NTowMA%3D%3D"
            )

            # 4. Send POST request to Cratio
            response = requests.post(
                codeyoung_url,
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            print("🟢 Cratio Response (raw text):", response.text)

            # 5. Return Cratio's response to client
            return Response({
                "status": response.status_code,
                "response": response.json()
            }, status=response.status_code)

        except Exception as e:
            logger.error(f"❌ Error in codeyoung Lead Submission: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
