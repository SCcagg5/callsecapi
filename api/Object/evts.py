import requests

class evts:
    def check_method(method):
        auth = ["put", "delete", "patch", "post", "head", "options", "get"]
        for i in auth:
            if i == str(method):
                return [True, None, None]
        return [False, "invalid method " + str(method), 401]

    def call(url, method, data = None):
        auth={  "put" : [requests.put, (url)],
                "delete": [requests.delete, (url)],
                "patch": [requests.patch, (url)],
                "post": [requests.post, (url, {"data": data})],
                "head": [requests.head, (url)],
                "options": [requests.options, (url)],
                "get": [requests.get, {"params": data}]
        }
        try:
            r = auth[method][0](url, **auth[method][1])
        except:
            return [False, "Invalid url" , 401]
        return [True, {"data": r.text, "status": r.status_code}, 200]

if __name__ == '__main__':
    print(evts.call("http://google.com", "get")[1])
