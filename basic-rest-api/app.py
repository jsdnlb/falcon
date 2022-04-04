import json
import falcon


class ObjectRequestClass:
    def on_get(self, req, res):
        res.status = falcon.HTTP_200

        data = json.loads(req.stream.read())

        content = {
            'name': 'Daniel',
            'lastname': 'Buitrago',
            'role': 'admin'
        }

        output = {}
        if 'method' not in data:
            res.status = falcon.HTTP_501
            output['error'] = 'Error: none method found'
        else:

            if data['method'] == 'get-name':
                output['name'] = content['name']
            else:
                res.status = falcon.HTTP_400
                output['name'] = None

        res.media = output
        print('Run ObjectRequestClass...')


api = falcon.App()
api.add_route('/test', ObjectRequestClass())
