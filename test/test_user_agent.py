from unittest import TestCase
from unittest.mock import patch

from saasus_sdk_python._user_agent import SDK_USER_AGENT, merge_headers
from saasus_sdk_python.client.auth_client import SignedAuthApiClient
from saasus_sdk_python.src.auth.api_client import ApiClient


class UserAgentTest(TestCase):
    def test_default_user_agent(self):
        self.assertEqual(merge_headers({}, None), {"User-Agent": SDK_USER_AGENT})

    def test_request_user_agent_takes_precedence_case_insensitively(self):
        defaults = {"User-Agent": "Default/1.0", "Accept": "application/json"}
        request = {"user-agent": "Example/1.0", "Authorization": "signature"}

        self.assertEqual(
            merge_headers(defaults, request),
            {
                "User-Agent": f"Example/1.0 {SDK_USER_AGENT}",
                "Accept": "application/json",
                "Authorization": "signature",
            },
        )

    def test_user_agent_is_not_duplicated(self):
        headers = {"User-Agent": f"Example/1.0 {SDK_USER_AGENT}"}
        self.assertEqual(merge_headers(headers, None), headers)

    def test_generated_client_has_sdk_default(self):
        self.assertEqual(ApiClient().user_agent, SDK_USER_AGENT)

    def test_signed_client_preserves_request_override(self):
        class StopRequest(Exception):
            pass

        client = SignedAuthApiClient(header_name="USER-AGENT", header_value="Default/1.0")
        with patch.object(client.client, "generate_signature", return_value={}):
            with patch.object(ApiClient, "request", side_effect=StopRequest) as request:
                with self.assertRaises(StopRequest):
                    client.call_api("/auth-info", "GET", header_params={"User-Agent": "Example/1.0"})

        headers = request.call_args.args[3]
        self.assertEqual(headers["User-Agent"], f"Example/1.0 {SDK_USER_AGENT}")
        self.assertNotIn("user-agent", headers)
