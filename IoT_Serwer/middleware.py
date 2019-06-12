from IoT_Serwer.weatherApi.weather import WeatherApiApp


class StartupMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        WeatherApiApp.start()
        from django.core.exceptions import MiddlewareNotUsed
        raise MiddlewareNotUsed()

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
