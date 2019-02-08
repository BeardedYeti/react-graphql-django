# File: ./backend/backend/schema.py

import graphene

import todo.schema

class Queries(
    todo.schema.Query,
    graphene.ObjectType
):
    dummy = graphene.String()

schema = graphene.Schema(query=Queries)
