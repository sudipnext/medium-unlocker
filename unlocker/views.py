from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from bs4 import BeautifulSoup
import re
import requests
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from html import unescape

from unlocker.utils import update_links_to_proxy


class UnlockerViewSet(viewsets.ViewSet):

    def retrieve_content(self, url: str, is_api: bool=False):
        validator = URLValidator()
        try:
            validator(url)
        except ValidationError:
            raise ValueError("Invalid URL format.")

        try:
            response = requests.get(f"http://webcache.googleusercontent.com/search?q=cache:{url}&strip=0&vwsrc=1&&hl=en&lr=lang_en")
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            pres = soup.find_all('pre')

            if not pres:
                raise ValueError("No Data found")

            text_data = unescape(pres[0].get_text())
            text_data = re.sub(r'<script[^>]*>.*?</script>', '', text_data).strip()
            return update_links_to_proxy(BeautifulSoup(text_data, 'html.parser'), is_api)

        except requests.RequestException:
            raise ValueError("Invalid URL or Request error")

    @swagger_auto_schema(
        operation_description="Unlock and render the page",
        manual_parameters=[
            openapi.Parameter('url', openapi.IN_QUERY, description="URL to retrieve content from", type=openapi.TYPE_STRING)
        ],
        responses={
            200: 'Rendered HTML content'
        }
    )
    def retrieve(self, request: HttpRequest):
        try:
            content = self.retrieve_content(request.GET.get('url', ''))
            return HttpResponse(str(content), content_type="text/html")
        except ValueError as e:
            return HttpResponse(str(e), status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    @swagger_auto_schema(
        operation_description="Unlock content and return as API response",
        manual_parameters=[
            openapi.Parameter('url', openapi.IN_QUERY, description="URL to retrieve content from", type=openapi.TYPE_STRING)
        ],
        responses={
            200: 'JSON Response containing the unlocked content'
        }
    )
    def api(self, request: HttpRequest):
        try:
            content = self.retrieve_content(request.GET.get('url', ''), is_api=True)
            return Response({"content": str(content)})
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
