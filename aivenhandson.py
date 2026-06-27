import os

from opensearchpy import OpenSearch


def get_client() -> OpenSearch:
    url = os.environ["OPENSEARCH_URL"]
    username = os.environ["OPENSEARCH_USERNAME"]
    password = os.environ["OPENSEARCH_PASSWORD"]

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
