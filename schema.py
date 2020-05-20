# ==============Section 1 hello aman==================
# import graphene
# import json
# class Query(graphene.ObjectType):
#     hello=graphene.String()


#     def resolve_hello(self,info):
#         return "aman"

# schema=graphene.Schema(query=Query)

# result=schema.execute(
#     '''
#     {
#         hello
#     }
#     '''
# )
# dictResult=dict(result.data.items())
# print(result.data.items())
# print(result.data['hello'])
# print(json.dumps(dictResult))
# print(json.dumps(dictResult,indent=2))


# line 16 ma { } ma sirf hello word hi print hoga
# ausky elava koi word nai print hoga


# ===================Section 2 snakecase vs camelcase====================

import graphene
import json
class Query(graphene.ObjectType):
    hello=graphene.String()
    is_admin = graphene.Boolean()


    def resolve_hello(self,info):
        return "aman"

    def resolve_is_admin(self,info):
        return True

schema=graphene.Schema(query=Query,auto_camelcase=False)

result=schema.execute(
    '''
    {
        # isAdmin
        is_admin
    }
    '''
)
dictResult=dict(result.data.items())
# print(result.data.items())
# print(result.data['hello'])
# print(json.dumps(dictResult))
print(json.dumps(dictResult,indent=2))

# jb ap result ki query ma kuch bi doge to hamesha
# camel case dena hoga under ma nai desakty 
# only camel case in acceptable
# or ager camel case ko hata ha to apko auto _camelcase=False karna hoga

# ======================Section 3 object types and arguments in Queries============
# import graphene
# import json
# from datetime import datetime 

# class User(graphene.ObjectType):
#     id = graphene.ID()
#     username = graphene.String()
#     created_at=graphene.DateTime()

# class Query(graphene.ObjectType):
#     users = graphene.List(User,Limit=graphene.Int())
#     hello=graphene.String()
#     is_admin = graphene.Boolean()


#     def resolve_hello(self,info):
#         return "aman"

#     def resolve_is_admin(self,info):
#         return True

#     def resolve_users(self,info,limit=None):
#         return [
#             User(id="1",username="Alan1", created_at=datetime.now()),
#             User(id="2",username="Alan2", created_at=datetime.now()),
#             User(id="3",username="Alan3", created_at=datetime.now())

#         ][:limit]
# schema = graphene.Schema(query=Query)

# result=schema.execute(
#     '''
#     {
#       users {
#         id
#         createdAt
#         username
#       }
#     }
#     '''
# )
# dictResult = dict(result.data.items())
# print(json.dumps(dictResult, indent=2))

# ====================Section Mutations default values================

# import graphene
# import json
# import uuid
# from datetime import datetime 

# class User(graphene.ObjectType):
#     id = graphene.ID(default_value=str(uuid.uuid4()))
#     username = graphene.String()
#     created_at=graphene.DateTime(default_value=datetime.now())

# class Query(graphene.ObjectType):
#     users = graphene.List(User,Limit=graphene.Int())
#     hello=graphene.String()
#     is_admin = graphene.Boolean()


#     def resolve_hello(self,info):
#         return "aman"

#     def resolve_is_admin(self,info):
#         return True

#     def resolve_users(self,info,limit=None):
#         return [
#             User(id="1",username="Alan1", created_at=datetime.now()),
#             User(id="2",username="Alan2", created_at=datetime.now()),
#             User(id="3",username="Alan3", created_at=datetime.now())

#         ][:limit]

# class CreateUser(graphene.Mutation):
#     user = graphene.Field(User)

#     class Arguments:
#         username = graphene.String()

#     def mutate(self,info,username):
#         user=User(username=username)
#         return CreateUser(user=user)

# class Mutation(graphene.ObjectType):
#     create_user = CreateUser.Field()

# schema = graphene.Schema(query=Query,mutation=Mutation)

# result=schema.execute(
#     '''
#     mutation {
#         createUser(username:"aman"){
#             user {
#                 id
#                 username
#                 createdAt
#             }
#         }
#     }
#     '''
# )
# dictResult = dict(result.data.items())
# print(json.dumps(dictResult, indent=2))

# ====================Section Variables in Queries_Mutations================

# import graphene
# import json
# import uuid
# from datetime import datetime 

# class User(graphene.ObjectType):
#     id = graphene.ID(default_value=str(uuid.uuid4()))
#     username = graphene.String()
#     created_at = graphene.DateTime(default_value=datetime.now())

# class Query(graphene.ObjectType):
#     users = graphene.List(User,Limit=graphene.Int())
#     hello=graphene.String()
#     is_admin = graphene.Boolean()


#     def resolve_hello(self,info):
#         return "aman"

#     def resolve_is_admin(self,info):
#         return True

#     def resolve_users(self,info,limit=None):
#         return [
#             User(id="1",username="Alan1", created_at=datetime.now()),
#             User(id="2",username="Alan2", created_at=datetime.now()),
#             User(id="3",username="Alan3", created_at=datetime.now())

#         ][:limit]

# class CreateUser(graphene.Mutation):
#     user = graphene.Field(User)

#     class Arguments:
#         username = graphene.String()

#     def mutate(self,info,username):
#         user=User(username=username)
#         return CreateUser(user=user)

# class Mutation(graphene.ObjectType):
#     create_user = CreateUser.Field()

# schema = graphene.Schema(query=Query,mutation=Mutation)

# result=schema.execute(
#     '''
#     query getUsersQuery ($limit: Int) {
#         users(limit: $limit){
#             id
#             username
#             createdAt
#         }
#     }
#     ''',
#     variable_values={ 'limit': 1 }
# )
# dictResult = dict(result.data.items())
# print(json.dumps(dictResult, indent=2))

# =====================Section Self and info values==============

import graphene
import json
import uuid
from datetime import datetime 

class Post(graphene.ObjectType):
    title = graphene.String()
    content = graphene.String()


class User(graphene.ObjectType):
    id = graphene.ID(default_value=str(uuid.uuid4()))
    username = graphene.String()
    created_at = graphene.DateTime(default_value=datetime.now())
    avatar_url = graphene.String()

    def resolve_avatar_url(self, info):
        return 'https://cloudinary.com/{}/{}'.format(self.username, self.id)


class Query(graphene.ObjectType):
    users = graphene.List(User,Limit=graphene.Int())
    hello=graphene.String()
    is_admin = graphene.Boolean()


    def resolve_hello(self,info):
        return "aman"

    def resolve_is_admin(self,info):
        return True

    def resolve_users(self,info,limit=None):
        return [
            User(id="1",username="Alan1", created_at=datetime.now()),
            User(id="2",username="Alan2", created_at=datetime.now()),
            User(id="3",username="Alan3", created_at=datetime.now())

        ][:limit]

class CreateUser(graphene.Mutation):
    user = graphene.Field(User)

    class Arguments:
        username = graphene.String()

    def mutate(self,info,username):
        user=User(username=username)
        return CreateUser(user=user)

class CreatePost(graphene.Mutation):
    post = graphene.Field(Post)

    class Arguments:
        title = graphene.String()
        content = graphene.String()

    def mutate(self, info, title, content):
        if info.context.get('is_anonymous'):
            raise Exception('Not authenticated!')
        post = Post(title=title, content=content)
        return CreatePost(post=post)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_post = CreatePost.Field()


schema = graphene.Schema(query=Query,mutation=Mutation)


result = schema.execute(
    '''
    {
      users {
        id
        createdAt
        username
        avatarUrl
      }
    }
    ''',
    context={'is_anonymous': True},
    variable_values={'limit': 1}
)
dictResult = dict(result.data.items())
print(json.dumps(dictResult, indent=2))
