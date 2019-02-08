# File: ./backend/todo/schema.py

import graphene
from graphene_django.types import DjangoObjectType
from graphql_relay.node.node import from_global_id

from . import models

class MessageType(DjangoObjectType):
    class Meta:
        model = models.Message
        interfaces = (graphene.Node, )

class Query(object):
    all_messages = graphene.List(MessageType)
    message = graphene.Field(MessageType, id=graphene.ID())

    def resolve_all_messages(self, info, **kwargs):
        return models.Message.objects.all()
    
    def resolve_message(self, info, **kwargs):
        rid = from_global_id(kwargs.get('id'))
        # rid is a tuple: ('MessageType', '1')
        return models.Message.objects.get(pk=rid[1])
