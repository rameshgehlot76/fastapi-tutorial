# uvicorn index:app --reload
"""
Compare FastAPI with Other APIs
"Flask is simpler but lacks built-in validation and async.
Django is too heavy for just serving models.
FastAPI hits the sweet spot — fast, async-native,
auto-validates inputs with Pydantic, and generates docs automatically.
That's why the ML community has adopted it as the standard."

Define FastAPI
"FastAPI is a modern, fast, Python web framework for building REST APIs
with automatic data validation,auto-generated documentation, and native async support
— making it the standard choice for serving machine learning models in production."

Q: What is FastAPI?
FastAPI is a modern, high-performance Python web framework used to build APIs quickly and efficiently.
It is built on top of Starlette (for web handling) and Pydantic (for data validation),
and uses Python's type hints to automatically validate request and response data.

Q: What are the key features of FastAPI?

1. High Performance FastAPI is one of the fastest Python frameworks available, comparable to Node.js and Go in benchmarks.
This is because it is built on Starlette which uses asynchronous programming (async/await) internally.

2. Automatic Data Validation FastAPI uses Pydantic models to automatically validate incoming request data.
If a client sends wrong or missing data, FastAPI returns a clear error response without any extra code from the developer.

3. Auto-generated Documentation FastAPI automatically generates interactive API documentation using:

* Swagger UI at /docs
* ReDoc at /redoc
No manual documentation writing is needed.

4. Async Support FastAPI natively supports async def route functions,
allowing the server to handle multiple requests simultaneously without blocking
— especially useful when calling external APIs like OpenAI or querying databases.

5. Type Hint Based FastAPI relies heavily on Python type hints.
These hints are not just for readability — they are used by the framework
to validate data, generate docs, and enforce structure.

Q: What is FastAPI built on?
FastAPI is built on two core libraries:
* Starlette — handles the web server layer, routing, middleware, and async support
* Pydantic — handles data validation and serialization using Python type hints


Q: What is uvicorn in FastAPI?
Uvicorn is an ASGI (Asynchronous Server Gateway Interface) server used to run FastAPI applications.
Since FastAPI is an async framework, it needs an ASGI server instead of a traditional WSGI server like Gunicorn.
Uvicorn handles incoming HTTP requests and passes them to the FastAPI application.


One-line definition for any interview:
"FastAPI is a modern, fast, Python web framework for building REST APIs with
automatic data validation, auto-generated documentation, and native async support
— making it the standard choice for serving machine learning models in production."

This covers almost every angle an interviewer can ask from FastAPI at your level.
"""


