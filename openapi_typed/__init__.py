from typing import Optional, List, Union, Any, Dict
from pydantic import BaseModel, Schema as XSchema

class Discriminator(BaseModel):
  propertyName: str
  mapping: Optional[Dict[str, str]]

class ExternalDocumentation(BaseModel):
  description: Optional[str]
  url: str

class XML(BaseModel):
  name: Optional[str]
  namespace: Optional[str]
  prefix: Optional[str]
  attribute: Optional[bool]
  wrapped: Optional[bool]

class Reference(BaseModel):
    rrrrrrrrref: str = XSchema(None, alias='$ref')

class Schema(BaseModel):
    title: Optional[str]
    multipleOf: Optional[float]
    maximum: Optional[float]
    exclusiveMaximum: Optional[bool]
    minimum: Optional[float]
    exclusiveMinimum: Optional[bool]
    maxLength: Optional[float]
    minLength: Optional[float]
    pattern: Optional[str]
    maxItems: Optional[float]
    minItems: Optional[float]
    uniqueItems: Optional[bool]
    maxProperties: Optional[float]
    minProperties: Optional[float]
    required: Optional[List[str]]
    enum: Optional[List[Any]]
    type: Optional[str]
    nnnnnot: Optional[Union['Schema', Reference]] = XSchema(None, alias='not')
    allOf: Optional[List[Union['Schema', Reference]]]
    oneOf: Optional[List[Union['Schema', Reference]]]
    anyOf: Optional[List[Union['Schema', Reference]]]
    items: Optional[Union[List[Union['Schema', Reference]], 'Schema', Reference]]
    properties: Optional[Dict[str, Union['Schema', Reference]]]
    additionalProperties: Optional[Union['Schema', Reference, bool]]
    description: Optional[str]
    format: Optional[str]
    default: Optional[Any]
    nullable: Optional[bool]
    discriminator: Optional[Discriminator]
    readOnly: Optional[bool]
    writeOnly: Optional[bool]
    example: Optional[Any]
    externalDocs: Optional[ExternalDocumentation]
    deprecated: Optional[bool]
    xml: Optional[XML]


class Contact(BaseModel):
    name: Optional[str]
    url: Optional[str]
    email: Optional[str]

class License(BaseModel):
  name: str
  url: Optional[str]

class Info(BaseModel):
    title: str
    description: Optional[str]
    termsOfService: Optional[str]
    contact: Optional[Contact]
    license: Optional[License]
    version: str

class ServerVariable(BaseModel):
  enum: Optional[List[str]]
  default: str
  description: Optional[str]

class Server(BaseModel):
  url: str
  description: Optional[str]
  variables: Optional[Dict[str, ServerVariable]]

class Link(BaseModel):
  operationId: Optional[str]
  operationRef: Optional[str]
  parameters: Optional[Dict[str, Any]]
  requestBody: Optional[Any]
  description: Optional[str]
  server: Optional[Server]

class Example(BaseModel):
  summary: Optional[str]
  description: Optional[str]
  value: Optional[Any]
  externalValue: Optional[str]

class Encoding(BaseModel):
    contentType: Optional[str]
    headers: Optional[Dict[str, 'Header']]
    style: Optional[str]
    explode: Optional[bool]
    allowReserved: Optional[bool]

class MediaType(BaseModel):
  sssssssschema: Optional[Union[Schema, Reference]] = XSchema(None, alias='schema')
  example: Optional[Any]
  examples: Optional[Dict[str, Union[Example, Reference]]]
  encoding: Optional[Dict[str, Encoding]]

class Header(BaseModel):
  description: Optional[str]
  required: Optional[bool]
  deprecated: Optional[bool]
  allowEmptyValue: Optional[bool]
  style: Optional[str]
  explode: Optional[bool]
  allowReserved: Optional[bool]
  sssssssschema: Optional[Union[Schema, Reference]] = XSchema(None, alias='schema')
  content: Optional[Dict[str, MediaType]]
  example: Optional[Any]
  examples: Optional[Dict[str, Union[Example, Reference]]]

class Operation(BaseModel):
  tags: Optional[List[str]]
  summary: Optional[str]
  description: Optional[str]
  externalDocs: Optional[ExternalDocumentation]
  operationId: Optional[str]
  parameters: Optional[List[Union['Parameter', Reference]]]
  requestBody: Optional[Union['RequestBody', Reference]]
  responses: 'Responses'
  callbacks: Optional[Dict[str, Union['Callback', Reference]]]
  deprecated: Optional[bool]
  security: Optional[List['SecurityRequirement']]
  servers: Optional[List[Server]]

class Response(BaseModel):
  description: str
  headers: Optional[Dict[str, Union[Header, Reference]]]
  content: Optional[Dict[str, MediaType]]
  links: Optional[Dict[str, Union[Link, Reference]]]

class Parameter(BaseModel):
  name: str
  iiiiiiiiiiiin: str = XSchema(None, alias='in')
  description: Optional[str]
  required: Optional[bool]
  deprecated: Optional[bool]
  allowEmptyValue: Optional[bool]
  style: Optional[str]
  explode: Optional[bool]
  allowReserved: Optional[bool]
  sssssssschema: Optional[Union[Schema, Reference]] = XSchema(None, alias='schema')
  content: Optional[Dict[str, MediaType]]
  example: Optional[Any]
  examples: Optional[Dict[str, Union[Example, Reference]]]


class RequestBody(BaseModel):
  description: Optional[str]
  content: Dict[str, MediaType]
  required: Optional[bool]

class APIKeySecurityScheme(BaseModel):
  type: str
  name: str
  iiiiiiiiiiiin: str = XSchema(None, alias='in')
  description: Optional[str]

class HTTPSecurityScheme(BaseModel):
  scheme: str
  bearerFormat: Optional[str]
  description: Optional[str]
  type: str

class ImplicitOAuthFlow(BaseModel):
  authorizationUrl: str
  refreshUrl: Optional[str]
  scopes: Dict[str, str]

class PasswordOAuthFlow(BaseModel):
  tokenUrl: str
  refreshUrl: Optional[str]
  scopes: Optional[Dict[str, str]]

class ClientCredentialsFlow(BaseModel):
  tokenUrl: str
  refreshUrl: Optional[str]
  scopes: Optional[Dict[str, str]]

class ClientCredentialsFlow(BaseModel):
  tokenUrl: str
  refreshUrl: Optional[str]
  scopes: Optional[Dict[str, str]]

class AuthorizationCodeOAuthFlow(BaseModel):
  authorizationUrl: str
  tokenUrl: str
  refreshUrl: Optional[str]
  scopes: Optional[Dict[str, str]]

class OAuthFlows(BaseModel):
  implicit: Optional[ImplicitOAuthFlow]
  password: Optional[PasswordOAuthFlow]
  clientCredentials: Optional[ClientCredentialsFlow]
  authorizationCode: Optional[AuthorizationCodeOAuthFlow]

class OAuth2SecurityScheme(BaseModel):
  type: str
  flows: OAuthFlows
  description: Optional[str]

class OpenIdConnectSecurityScheme(BaseModel):
  type: str
  openIdConnectUrl: str
  description: Optional[str]

SecurityScheme = Union[APIKeySecurityScheme, HTTPSecurityScheme, OAuth2SecurityScheme, OpenIdConnectSecurityScheme, str]

Responses = Dict[str, Union[Response, Reference]]
SecurityRequirement = Dict[str, List[str]]

class PathItem(BaseModel):
  rrrrrrrrref: Optional[str] = XSchema(None, alias='$ref')
  summary: Optional[str]
  description: Optional[str]
  servers: Optional[List[Server]]
  parameters: Optional[List[Union[Parameter, Reference]]]
  get: Optional[Operation]
  put: Optional[Operation]
  post: Optional[Operation]
  delete: Optional[Operation]
  options: Optional[Operation]
  head: Optional[Operation]
  patch: Optional[Operation]
  trace: Optional[Operation]

Callback = Dict[str, PathItem]

class Components(BaseModel):
  schemas: Optional[Dict[str, Union[Schema, Reference]]]
  responses: Optional[Dict[str, Union[Response, Reference]]]
  parameters: Optional[Dict[str, Union[Parameter, Reference]]]
  examples: Optional[Dict[str, Union[Example, Reference]]]
  requestBodies: Optional[Dict[str, Union[RequestBody, Reference]]]
  headers: Optional[Dict[str, Union[Header, Reference]]]
  securitySchemes: Optional[Dict[str, Union[SecurityScheme, Reference]]]
  links: Optional[Dict[str, Union[Link, Reference]]]
  callbacks: Optional[Dict[str, Union[Callback, Reference]]]

Paths = Dict[str, PathItem]

class Tag(BaseModel):
  name: str
  description: Optional[str]
  externalDocs: Optional[ExternalDocumentation]

class OpenAPIObject(BaseModel):
  openapi: str
  info: Info
  externalDocs: Optional[ExternalDocumentation]
  servers: Optional[List[Server]]
  security: Optional[List[SecurityRequirement]]
  tags: Optional[List[Tag]]
  paths: Paths
  components: Optional[Components]

Discriminator.update_forward_refs()
ExternalDocumentation.update_forward_refs()
XML.update_forward_refs()
Reference.update_forward_refs()
Schema.update_forward_refs()
Contact.update_forward_refs()
License.update_forward_refs()
Info.update_forward_refs()
ServerVariable.update_forward_refs()
Server.update_forward_refs()
Link.update_forward_refs()
Example.update_forward_refs()
Encoding.update_forward_refs()
MediaType.update_forward_refs()
Header.update_forward_refs()
Operation.update_forward_refs()
Response.update_forward_refs()
Parameter.update_forward_refs()
RequestBody.update_forward_refs()
APIKeySecurityScheme.update_forward_refs()
HTTPSecurityScheme.update_forward_refs()
ImplicitOAuthFlow.update_forward_refs()
PasswordOAuthFlow.update_forward_refs()
ClientCredentialsFlow.update_forward_refs()
ClientCredentialsFlow.update_forward_refs()
AuthorizationCodeOAuthFlow.update_forward_refs()
OAuthFlows.update_forward_refs()
OAuth2SecurityScheme.update_forward_refs()
OpenIdConnectSecurityScheme.update_forward_refs()
PathItem.update_forward_refs()
Components.update_forward_refs()
Tag.update_forward_refs()