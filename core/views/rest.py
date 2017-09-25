import json

from django.conf import settings
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

from viber_devino.client import DevinoClient
from viber_devino.client import DevinoException

from core import models
from core import consts
from core import serializers


class BaseDevino(views.APIView):
    api_resource = None
    serializer = None
    api_resource_lib = None

    def devino_request(self, serializer=None):
        serializer.is_valid(raise_exception=True)

        json_data = json.dumps(
            serializer.validated_data
        )
        devino_request = models.DevinoRequest.objects.create(api_resource=self.api_resource, data=json_data)

        try:
            answer = self.api_resource_lib(**serializer.validated_data)

            models.DevinoAnswer.objects.create(
                status=answer.status,
                result=answer.result,
                request=devino_request,
            )
            return Response({'status': answer.status, 'result': answer.result},
                            status=status.HTTP_200_OK)

        except DevinoException as ex:
            error = models.DevinoAnswer.objects.create(
                status=ex.http_status if ex.http_status else status.HTTP_500_INTERNAL_SERVER_ERROR,
                request=devino_request,
                is_fail=True,
            )
            return Response({'code': error.code, 'description': error.description}, status=ex.http_status)

    def post(self, request):
        serializer = self.serializer
        serializer = serializer(data=request.data)
        response = self.devino_request(serializer)
        return response


class SendText(BaseDevino):
    api_resource = consts.SEND_TEXT
    serializer = serializers.SendText
    api_resource_lib = DevinoClient(settings.DEVINO_LOGIN, settings.DEVINO_PASSWORD).send_text
    http_method_names = ['post', ]


class SendImage(BaseDevino):
    api_resource = consts.SEND_IMAGE
    serializer = serializers.SendImage
    api_resource_lib = DevinoClient(settings.DEVINO_LOGIN, settings.DEVINO_PASSWORD).send_image
    http_method_names = ['post', ]


class SendTextAndButton(BaseDevino):
    api_resource = consts.SEND_TEXT_AND_BUTTON
    serializer = serializers.SendTextAndButton
    api_resource_lib = DevinoClient(settings.DEVINO_LOGIN, settings.DEVINO_PASSWORD).send_text_and_button
    http_method_names = ['post', ]


class CheckStatusMessages(BaseDevino):
    api_resource = consts.CHECK_STATUS_MESSAGES
    serializer = serializers.CheckStatusMessages
    api_resource_lib = DevinoClient(settings.DEVINO_LOGIN, settings.DEVINO_PASSWORD).check_status_messages
    http_method_names = ['post', ]
