import json.decoder
from requests import Response


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, \
            f"Cannot find cookie with name {cookie_name} in the last response"
        print()
        print('========================================================')
        print('cookie')
        print(response.cookies[cookie_name])
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, \
            f"Cannot find headers with the name {headers_name} in the last response"
        print()
        print('========================================================')
        print('headers_name')
        print(response.headers[headers_name])
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecoderError:
            assert False, \
                f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON does not have key '{name}'"
        print()
        print('========================================================')
        print('json')
        print(response_as_dict[name])
        return response_as_dict[name]

