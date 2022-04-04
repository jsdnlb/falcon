import json, falcon

class ObjectRequestClass:
    def on_get(self, req, res):
        data = {
            'name' : 'Daniel',
            'lastname': 'Buitrago',
            'role' : 'admin'
        }

        res.body = json.dumps(data)
        print('Run ObjectRequestClass...')


api = falcon.App()
api.add_route('/test', ObjectRequestClass())
