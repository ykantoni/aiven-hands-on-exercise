import os
from urllib.parse import urlparse

from opensearchpy import OpenSearch


def validate_opensearch_env() -> tuple[str, str, str]:
    url = os.environ["OPENSEARCH_URL"]
    username = os.environ["OPENSEARCH_USERNAME"]
    password = os.environ["OPENSEARCH_PASSWORD"]

    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise ValueError(
            "OPENSEARCH_URL must be a well-formed HTTP or HTTPS URL"
        )

    if not username.strip():
        raise ValueError("OPENSEARCH_USERNAME must not be empty")

    if not password:
        raise ValueError("OPENSEARCH_PASSWORD must not be empty")
    if len(password) < 8:
        raise ValueError("OPENSEARCH_PASSWORD must be at least 8 characters")

    return url, username, password


def get_client() -> OpenSearch:
    url, username, password = validate_opensearch_env()

    return OpenSearch(
        hosts=[url],
        http_auth=(username, password),
        use_ssl=True,
        verify_certs=True,
    )


def main() -> None:
    info = get_client().info()
    print(info["version"]["number"])


if __name__ == "__main__":
    main()
