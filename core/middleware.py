

class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)  # استدعاء الاستجابة
        response['X-H'] = "Woroud"  # تعديل الهيدر
        return response
