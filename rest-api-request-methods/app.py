import json
import falcon


class ObjectRequestMethodsClass:
    def on_get(self, req, res):
        res.status = falcon.HTTP_200

        data = json.loads(req.stream.read())

        output = {
            'msg': 'Hello {0}'.format(data['name'])
        }
        res.media = output

    def on_post(self, req, res):
        res.status = falcon.HTTP_200

        data = json.loads(req.stream.read())

        sum = int(data['x']) + int(data['y'])
        subtraction = int(data['x']) - int(data['y'])
        multiplication = int(data['x']) * int(data['y'])
        output = {
            'sum': 'x:{x} + y:{y} is equal to :{total}'.format(x=data['x'], y=data['y'], total=sum),
            'subtraction': 'x:{x} - y:{y} is equal to :{total}'.format(x=data['x'], y=data['y'], total=subtraction),
            'multiplication': 'x:{x} * y:{y} is equal to :{total}'.format(x=data['x'], y=data['y'], total=multiplication),
        }
        res.media = output

    def on_put(self, req, res):
        res.status = falcon.HTTP_200
        output = {
            'msg': 'put is not supported for now'
        }

        res.media = output

    def on_delete(self, req, res):
        res.status = falcon.HTTP_200
        output = {
            'msg': 'delete is not supported for now'
        }

        res.media = output


api = falcon.App()
api.add_route('/demo', ObjectRequestMethodsClass())
