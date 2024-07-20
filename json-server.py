import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status

from views import list_orders, single_order, new_order,remove_order

class JSONServer(HandleRequests):

    def do_GET(self):

        response_body = ""
        url = self.parse_url(self.path)

        if url["requested_resource"] == "orders":
            if url["pk"] != 0:
                response_body = single_order(url["pk"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)
            
            response_body = list_orders()
            return self.response(response_body,  status.HTTP_200_SUCCESS.value)
        

    def do_POST(self):

        url = self.parse_url(self.path)

        if url["requested_resource"] == "orders":
            content_len = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_len)
            order_data = json.loads(post_data)

            success = new_order(order_data)

            if success:
                self.send_response(201)
                self.send_header('Content-Type','application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Order was created successfully!'}))

            else:
                self.send_response(500)
                self.send_header('Content-Type','application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Failed to create order'}))


    def do_DELETE(self):

        url = self.parse_url(self.path)
        pk = url["pk"]

        if url["requested_resource"] == "orders":
            if pk != 0:
                successfully_deleted = remove_order(pk)
                if successfully_deleted:
                    return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
                return self.response("Requested resource was not found", status.HTTP_400_CLIENT_ERROR_BAD_REQUEST_DATA)


        














    






def main():
    host = ''
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()

if __name__ == "__main__":
    main()