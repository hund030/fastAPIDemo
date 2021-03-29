from fastapi import HTTPException

class Response:
    @staticmethod
    def ok(data=None):
        response = {
            'code': 200,
            'msg': 'success',
        }
        if data is not None:
            response['data'] = data
        return response
    
    @staticmethod
    def error(code, msg):
        raise HTTPException(code, msg)