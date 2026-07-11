# RESTful API

## 0. Basics of HTTP/HTTPS

### HTTP vs HTTPS

HTTP, or Hypertext Transfer Protocol, is the protocol used by clients and
servers to exchange resources on the web. Data sent with HTTP is not encrypted,
so someone observing the network can read or modify the traffic.

HTTPS, or Hypertext Transfer Protocol Secure, uses HTTP with SSL/TLS
encryption. This protects the communication between the client and server by
encrypting the data, verifying the server's identity with certificates, and
helping prevent tampering during transmission.

Main differences:

- HTTP sends data in plain text, while HTTPS encrypts the data.
- HTTP usually uses port 80, while HTTPS usually uses port 443.
- HTTPS uses SSL/TLS certificates to help prove the server's identity.
- HTTPS is preferred for logins, payments, personal data, APIs, and modern
  websites in general.

### HTTP Request Structure

An HTTP request is sent by a client to ask a server for an action.

Example outline:

```http
GET /users/42 HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: application/json

```

Common parts of a request:

- Request line: contains the method, path, and HTTP version.
- Headers: provide metadata such as host, content type, authentication, or
  accepted response format.
- Body: optional data sent with the request, commonly used with methods like
  POST, PUT, or PATCH.

### HTTP Response Structure

An HTTP response is sent by a server back to the client.

Example outline:

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 31

{"id": 42, "name": "John"}
```

Common parts of a response:

- Status line: contains the HTTP version, status code, and status message.
- Headers: provide metadata such as content type, cache rules, cookies, or
  content length.
- Body: optional content returned by the server, such as HTML, JSON, XML, or
  an error message.

### Common HTTP Methods

- GET: retrieves data from the server. Use case: fetching a web page or reading
  a list of users from an API.
- POST: sends new data to the server. Use case: creating a new account or
  submitting a form.
- PUT: replaces an existing resource with new data. Use case: updating all
  fields of a user profile.
- PATCH: partially updates an existing resource. Use case: changing only a
  user's email address.
- DELETE: removes a resource from the server. Use case: deleting a blog post or
  removing an item from a database.

### Common HTTP Status Codes

- 200 OK: the request succeeded. Scenario: a page or API resource was returned
  successfully.
- 201 Created: a new resource was created. Scenario: a POST request created a
  new user account.
- 301 Moved Permanently: the resource has a new permanent URL. Scenario: a site
  redirects from `http://example.com` to `https://example.com`.
- 400 Bad Request: the server could not understand the request. Scenario: an API
  receives invalid JSON or missing required fields.
- 401 Unauthorized: authentication is required or invalid. Scenario: a request
  tries to access a protected API without a valid token.
- 403 Forbidden: the server understood the request but refuses access.
  Scenario: a logged-in user tries to access an admin-only resource.
- 404 Not Found: the requested resource does not exist. Scenario: a page URL or
  API endpoint is wrong.
- 500 Internal Server Error: the server encountered an unexpected problem.
  Scenario: application code crashes while processing the request.
