# gRPC (Google Remote Procedure Call)

## Why?

- Better suited to handle communication between services than REST.

### Convenience

- Protocol buffers
- Code generation from `.proto` files.
- Strongly typed.
- Uses binary serialization.

### Performance

- Binary serialization
- Multiplexing
- Streaming

### HTTP/2

- Header compression
- Multiplexing
- Server push
- Prioritization
- Flow control
- Smaller message size
- Streaming

## Why not?

- Documentation
- Doesn't work well with browsers

## gRPC vs REST

- gRPC use protocol buffers, REST uses JSON.

- REST is better suited for public APIs.
- gRPC is better suited for internal APIs.
- gRPC is more efficient than REST.
- gRPC is more complex than REST.
- gRPC is more difficult to debug than REST.
- gRPC is more difficult to implement than REST.
- gRPC is more difficult to understand than REST.
- gRPC is more difficult to maintain than REST.
- gRPC is more difficult to scale than REST.
- gRPC is more difficult to secure than REST.
- gRPC is more difficult to test than REST.
- gRPC is more difficult to use than REST.

## How?

```python
# server.py
import grpc

class Greeter(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloReply(message='Hello, %s!' % request.name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
```

```python
# client.py
import grpc

channel = grpc.insecure_channel('localhost:50051')
stub = hello_pb2_grpc.GreeterStub(channel)
response = stub.SayHello(hello_pb2.HelloRequest(name='you'))
print("Greeter client received: " + response.message)
```

## Best Practices

- Keep it simple
- Self-describing
- Consistent
- Versioned

## Other API architectures

- SOAP: Complex XML-based protocol for exchanging structured information in a decentralized, distributed environment. Security, transactions, and more.
- GraphQL: Query language for APIs and a runtime for executing those queries by using a type system you define for your data. It was developed by Facebook in 2012 and released as an open-source project in 2015.
- WebSockets: Full-duplex communication channels over a single TCP connection. It is designed to be implemented in web browsers and web servers but it can be used by any client or server application.
- Webhooks: HTTP callbacks that POST data to a URL when an event occurs. They are a way for apps to get real-time information to other apps.
