from ._version import VERSION


SDK_USER_AGENT = "SaaSus-SDK-python/" + VERSION


class UserAgentMixin:
    def __init__(self, configuration=None, header_name=None, header_value=None, *args, **kwargs):
        super().__init__(configuration, header_name, header_value, *args, **kwargs)
        if header_name is not None and header_name.lower() == "user-agent":
            self.default_headers.pop(header_name, None)
            self.user_agent = header_value

    def set_default_header(self, header_name, header_value):
        if header_name.lower() == "user-agent":
            header_name = "User-Agent"
        super().set_default_header(header_name, header_value)

    def call_api(self, resource_path, method, path_params=None, query_params=None,
                 header_params=None, *args, **kwargs):
        # The generated client merges defaults by exact header name.
        # Keep a request override under lowercase until the final merge.
        if header_params:
            header_params = {
                "user-agent" if name.lower() == "user-agent" else name: value
                for name, value in header_params.items()
            }
        return super().call_api(
            resource_path, method, path_params, query_params, header_params, *args, **kwargs
        )

    def request(self, method, url, query_params=None, headers=None, *args, **kwargs):
        override = None
        if headers is not None and "user-agent" in headers:
            override = {"User-Agent": headers["user-agent"]}
        return super().request(
            method, url, query_params, merge_headers(headers or {}, override), *args, **kwargs
        )


def merge_headers(default_headers, request_headers):
    headers = dict(request_headers or {})
    headers.update(default_headers)
    user_agent = None
    for source in (default_headers, request_headers or {}):
        for name, value in source.items():
            if name.lower() == "user-agent":
                headers.pop(name, None)
                user_agent = value
    user_agent = user_agent or ""
    if SDK_USER_AGENT not in user_agent.split():
        user_agent = f"{user_agent} {SDK_USER_AGENT}".strip()
    headers["User-Agent"] = user_agent
    return headers
