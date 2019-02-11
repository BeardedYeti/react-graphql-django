# File: ./backend/todo/schema.py

import graphene
import json
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

class CreateMessage(graphene.Mutation):
    class Arguments:
        message = graphene.String()

    status = graphene.Int()
    formErrors = graphene.String()
    message = graphene.Field(MessageType)

    @staticmethod
    def mutate(self, info, **kwargs):
        if not info.context.user.is_authenticated:
            return CreateMessage(status=403)
        message = kwargs.get('message', '').strip()
        # Here we would usually use Django forms to validate the input
        if not message:
            return CreateMessage(
                status=400,
                formErrors=json.dumps(
                    {'message': ['Please enter a message.']}))
        obj = models.Message.objects.create(
            user=info.context.user, message=message
        )
        return CreateMessage(status=200, message=obj)

class Mutation(object):
    create_message = CreateMessage.Field()
