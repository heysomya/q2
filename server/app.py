import grpc
from concurrent import futures
import time

# Import the generated classes
import login_pb2
import login_pb2_grpc


class LoginService(login_pb2_grpc.LoginServicer):

    def login(self, request, context):
        # Business logic for login
        if request.userName == "admin" and request.passWord == "password":
            return login_pb2.ApiResponse(responseMessage="Login successful", responseCode=200)
        else:
            return login_pb2.ApiResponse(responseMessage="Invalid credentials", responseCode=401)

    def logout(self, request, context):
        # Business logic for logout
        return login_pb2.ApiResponse(responseMessage="Logout successful", responseCode=200)


# Create a gRPC server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    login_pb2_grpc.add_LoginServicer_to_server(LoginService(), server)

    # Listen on port 50051
    print("Server starting on port 50051...")
    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(86400)  # Keep the server alive for one day
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
