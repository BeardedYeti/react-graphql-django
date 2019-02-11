# File: ./backend/backend/schema.py

import graphene

import todo.schema

class Queries(
    todo.schema.Query,
    graphene.ObjectType
):
    dummy = graphene.String()

class Mutations(
    todo.schema.Mutation,
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Queries, mutation=Mutations)
