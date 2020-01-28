from typing import Sequence, Union, Any, Mapping
from typing_extensions import TypedDict

class _Discriminator(TypedDict):
  propertyName: str

class Discriminator(_Discriminator, total=False):
  mapping: Mapping[str, str]


class _ExternalDocumentation(TypedDict):
  url: str

class ExternalDocumentation(_ExternalDocumentation, total=False):
  description: str

class XML(TypedDict, total=False):
  name: str
  namespace: str
  prefix: str
  attribute: bool
  wrapped: bool

Reference = TypedDict('Reference', { '$ref': str })

Schema = TypedDict('Schema',
    {'title': str,
    'multipleOf': float,
    'maximum': float,
    'exclusiveMaximum': bool,
    'minimum': float,
    'exclusiveMinimum': bool,
    'maxLength': float,
    'minLength': float,
    'pattern': str,
    'maxItems': float,
    'minItems': float,
    'uniqueItems': bool,
    'maxProperties': float,
    'minProperties': float,
    'required': Sequence[str],
    'enum': Sequence[Any],
    'type': str,
    'not': Union['Schema', Reference],  # type: ignore  # Forward references don't work in the old class declaration syntax
    'allOf': Sequence[Union['Schema', Reference]],  # type: ignore
    'oneOf': Sequence[Union['Schema', Reference]],  # type: ignore
    'anyOf': Sequence[Union['Schema', Reference]],  # type: ignore
    'items': Union[List[Union['Schema', Reference]], 'Schema', Reference],  # type: ignore
    'properties': Mapping[str, Union['Schema', Reference]],  # type: ignore
    'additionalProperties': Union['Schema', Reference, bool],  # type: ignore
    'description': str,
    'format': str,
    'default': Any,
    'nullable': bool,
    'discriminator': Discriminator,
    'readOnly': bool,
    'writeOnly': bool,
    'example': Any,
    'externalDocs': ExternalDocumentation,
    'deprecated': bool,
    'xml': XML}, total=False)


class Contact(TypedDict, total=False):
    name: str
    url: str
    email: str

class _License(TypedDict):
  name: str

class License(_License, total = False):
  url: str

class _Info(TypedDict):
    title: str
    version: str

class Info(_Info, total=False):
    description: str
    termsOfService: str
    contact: Contact
    license: License

class _ServerVariable(TypedDict):
  default: str

class ServerVariable(_ServerVariable, total=False):
  enum: Sequence[str]
  description: str

class _Server(TypedDict):
  url: str

class Server(_Server, total=False):
  description: str
  variables: Mapping[str, ServerVariable]

class Link(TypedDict, total=False):
  operationId: str
  operationRef: str
  parameters: Mapping[str, Any]
  requestBody: Any
  description: str
  server: Server

class Example(TypedDict, total=False):
  summary: str
  description: str
  value: Any
  externalValue: str

class Encoding(TypedDict, total=False):
    contentType: str
    headers: Mapping[str, 'Header']
    style: str
    explode: bool
    allowReserved: bool

class MediaType(TypedDict, total=False):
  schema: Union[Schema, Reference]
  example: Any
  examples: Mapping[str, Union[Example, Reference]]
  encoding: Mapping[str, Encoding]

class Header(TypedDict, total=False):
  description: str
  required: bool
  deprecated: bool
  allowEmptyValue: bool
  style: str
  explode: bool
  allowReserved: bool
  schema: Union[Schema, Reference]
  content: Mapping[str, MediaType]
  example: Any
  examples: Mapping[str, Union[Example, Reference]]

class _Operation(TypedDict):
    responses: 'Responses'  # type: ignore

class Operation(_Operation, total=False):
  tags: Sequence[str]
  summary: str
  description: str
  externalDocs: ExternalDocumentation
  operationId: str
  parameters: Sequence[Union['Parameter', Reference]]
  requestBody: Union['RequestBody', Reference]
  callbacks: Mapping[str, Union['Callback', Reference]]
  deprecated: bool
  security: Sequence['SecurityRequirement']
  servers: Sequence[Server]

class _Response(TypedDict):
  description: str

class Response(_Response, total=False):
  headers: Mapping[str, Union[Header, Reference]]
  content: Mapping[str, MediaType]
  links: Mapping[str, Union[Link, Reference]]

_Parameter = TypedDict('_Parameter', {
  'name': str,
  'in':str
})

class Parameter(_Parameter, total=False):
  description: str
  required: bool
  deprecated: bool
  allowEmptyValue: bool
  style: str
  explode: bool
  allowReserved: bool
  schema: Union[Schema, Reference]
  content: Mapping[str, MediaType]
  example: Any
  examples: Mapping[str, Union[Example, Reference]]




class _RequestBody(TypedDict):
  content: Mapping[str, MediaType]

class RequestBody(_RequestBody, total=False):
  description: str
  required: bool

_APIKeySecurityScheme = TypedDict('APIKeySecurityScheme', {
  'type': str,
  'name': str,
  'in': str
})

class APIKeySecurityScheme(_APIKeySecurityScheme, total=False):
  description: str

class _HTTPSecurityScheme(TypedDict):
  scheme: str
  type: str

class HTTPSecurityScheme(_HTTPSecurityScheme, total=False):
  bearerFormat: str
  description: str

class _ImplicitOAuthFlow(TypedDict):
  authorizationUrl: str
  scopes: Mapping[str, str]

class ImplicitOAuthFlow(_ImplicitOAuthFlow, total=False):
    refreshUrl: str

class _OAuthFlow(TypedDict):
    tokenUrl: str

class PasswordOAuthFlow(_OAuthFlow, total=False):
  refreshUrl: str
  scopes: Mapping[str, str]

class ClientCredentialsFlow(_OAuthFlow, total=False):
  refreshUrl: str
  scopes: Mapping[str, str]

class _AuthorizationCodeOAuthFlow(_OAuthFlow):
    authorizationUrl: str

class AuthorizationCodeOAuthFlow(_AuthorizationCodeOAuthFlow, total=False):     
  refreshUrl: str
  scopes: Mapping[str, str]

class OAuthFlows(TypedDict, total=False):
  implicit: ImplicitOAuthFlow
  password: PasswordOAuthFlow
  clientCredentials: ClientCredentialsFlow
  authorizationCode: AuthorizationCodeOAuthFlow

class _OAuth2SecurityScheme(TypedDict):
    type: str
    flows: OAuthFlows

class OAuth2SecurityScheme(_OAuth2SecurityScheme, total=False):
  description: str

class _OpenIdConnectSecurityScheme(TypedDict):
  type: str
  openIdConnectUrl: str

class OpenIdConnectSecurityScheme(_OpenIdConnectSecurityScheme, total=False):   
  description: str

SecurityScheme = Union[APIKeySecurityScheme, HTTPSecurityScheme, OAuth2SecurityScheme, OpenIdConnectSecurityScheme, str]

Responses = Mapping[str, Union[Response, Reference]]
SecurityRequirement = Mapping[str, Sequence[str]]

PathItem = TypedDict('PathItem', {
  '$ref': str,
  'summary': str,
  'description': str,
  'servers': Sequence[Server],
  'parameters': Sequence[Union[Parameter, Reference]],
  'get': Operation,
  'put': Operation,
  'post': Operation,
  'delete': Operation,
  'options': Operation,
  'head': Operation,
  'patch': Operation,
  'trace': Operation,
}, total=False)

Callback = Mapping[str, PathItem]

class Components(TypedDict, total=False):
  schemas: Mapping[str, Union[Schema, Reference]]
  responses: Mapping[str, Union[Response, Reference]]
  parameters: Mapping[str, Union[Parameter, Reference]]
  examples: Mapping[str, Union[Example, Reference]]
  requestBodies: Mapping[str, Union[RequestBody, Reference]]
  headers: Mapping[str, Union[Header, Reference]]
  securitySchemes: Mapping[str, Union[SecurityScheme, Reference]]
  links: Mapping[str, Union[Link, Reference]]
  callbacks: Mapping[str, Union[Callback, Reference]]

Paths = Mapping[str, PathItem]

class _Tag(TypedDict):
  name: str

class Tag(_Tag, total=False):
  description: str
  externalDocs: ExternalDocumentation

class _OpenAPIObject(TypedDict):
  openapi: str
  info: Info
  paths: Paths

class OpenAPIObject(_OpenAPIObject, total=False):
  externalDocs: ExternalDocumentation
  servers: Sequence[Server]
  security: Sequence[SecurityRequirement]
  tags: Sequence[Tag]
  components: Components
