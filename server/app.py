import grpc
from concurrent import futures
import time

import login_pb2
import login_pb2_grpc


class LoginService(login_pb2_grpc.LoginServicer):

    def login(self, request, context):
        if request.userName == "somya" and request.passWord == "somya@123":
            return login_pb2.ApiResponse(responseMessage="Login successful", responseCode=200)
        else:
            return login_pb2.ApiResponse(responseMessage="Invalid credentials", responseCode=401)

    def logout(self, request, context):
        return login_pb2.ApiResponse(responseMessage="Logout successful", responseCode=200)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    login_pb2_grpc.add_LoginServicer_to_server(LoginService(), server)

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
