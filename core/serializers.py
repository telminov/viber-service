from rest_framework import serializers

from viber_devino.client import NORMAL_PRIORITY, CONTENT_TYPE_TEXT, CONTENT_TYPE_IMAGE, CONTENT_TYPE_BUTTON


class BaseSend(serializers.Serializer):
    subject = serializers.CharField()
    priority = serializers.CharField(default=NORMAL_PRIORITY)
    address = serializers.CharField()
    validity_viber = serializers.IntegerField(default=86400)
    sms_text = serializers.CharField(default=None)
    sms_src_address = serializers.CharField(default=None)
    resend_sms = serializers.BooleanField(default=False)
    comment = serializers.CharField(default=None)
    validity_sms = serializers.IntegerField(default=None)


class SendText(BaseSend):
    content_type = serializers.CharField(default=CONTENT_TYPE_TEXT)
    text = serializers.CharField()


class SendImage(BaseSend):
    content_type = serializers.CharField(default=CONTENT_TYPE_IMAGE)
    image = serializers.URLField()


class SendTextAndButton(BaseSend):
    content_type = serializers.CharField(default=CONTENT_TYPE_BUTTON)
    text = serializers.CharField()
    caption = serializers.CharField()
    action = serializers.URLField()
    image = serializers.URLField(default=None)


class CheckStatusMessages(serializers.Serializer):
    id_messages = serializers.ListField(child=serializers.CharField ())
