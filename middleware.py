# - *- coding: utf- 8 - *-
__author__ = 'alexaled'

from my_bio.models import HttpRequestSave


class HttpRequestMiddleware(object):
    def process_request(self, request):
        new_http_req = HttpRequestSave()
        new_http_req.http_request = request.path_info
        new_http_req.remote_addr = request.META['REMOTE_ADDR']
        new_http_req.save()
