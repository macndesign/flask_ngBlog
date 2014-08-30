# coding: utf-8
from __future__ import unicode_literals, absolute_import

from marshmallow import Serializer, fields


class UserSerializer(Serializer):
    class Meta:
        fields = ("id", "email")


class PostSerializer(Serializer):
    user = fields.Nested(UserSerializer)

    class Meta:
        fields = ("id", "title", "body", "user", "created_at")


class SimpleTokenSerializer(Serializer):
    class Meta:
        fields = ("token",)
