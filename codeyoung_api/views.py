from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import logging

# Optional: For debug/info logs
logger = logging.getLogger(__name__)

class CodeyoungLeadAPIView(APIView):
    def post(self, request):
        try:
            # 1. Get JSON body from POST request
            lead_data = request.data

            # 2. Wrap it inside the required codeyoung format
            payload = {
                "records": [lead_data]
            }

            # 3. codeyoung endpoint with your API key
            codeyoung_url = (
                "https://apps.cratiocrm.com/api/apirequest.php"
                "?operation=insertRecords&formname=Leads"
                "&apikey=NF8xXzMwNTYkQDM5NSMjMjAyNC0xMi0yNyAxNTo0NTowMA%3D%3D"
            )

            # 4. Send POST request to codeyoung
            response = requests.post(
                codeyoung_url,
                json=payload,
                headers={"Content-Type": "application/json"}
            )

            # 5. Return codeyoung's response to the client
            return Response({
                "status": response.status_code,
                "response": response.json()
            }, status=response.status_code)

        except Exception as e:
            # Error handling
            logger.error(f"Error in codeyoung Lead Submission: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
