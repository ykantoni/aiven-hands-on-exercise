import os
import unittest

import aivenhandson

ENV_VARS = ("OPENSEARCH_URL", "OPENSEARCH_USERNAME", "OPENSEARCH_PASSWORD")
EXPECTED_VERSION = "3.3.2"


def env_configured() -> bool:
    return all(os.environ.get(name) for name in ENV_VARS)


@unittest.skipUnless(env_configured(), "OpenSearch environment variables not set")
class TestOpenSearchConnection(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = aivenhandson.get_client()

    def test_connection_succeeds(self) -> None:
        info = self.client.info()
        self.assertIn("version", info)
        self.assertIn("cluster_name", info)

    def test_cluster_version(self) -> None:
        info = self.client.info()
        self.assertEqual(info["version"]["number"], EXPECTED_VERSION)
