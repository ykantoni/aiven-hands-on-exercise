# Aiven OpenSearch hands-on

Small Python script that connects to an Aiven OpenSearch service and prints the cluster version.

## Prerequisites

- Python 3.9+
- An Aiven OpenSearch service with connection details from the Aiven console (Service URI, username, password)

## Install dependencies

From the project directory:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

On Linux or macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Set environment variables

The app reads these variables:

| Variable | Description |
| --- | --- |
| `OPENSEARCH_URL` | Service URI, e.g. `https://os-handson-ykantoni-9e92.h.aivencloud.com:10028` |
| `OPENSEARCH_USERNAME` | OpenSearch username, usually `avnadmin` |
| `OPENSEARCH_PASSWORD` | OpenSearch password from the Aiven console |

### Windows (PowerShell)

```powershell
$env:OPENSEARCH_URL = "https://os-handson-ykantoni-9e92.h.aivencloud.com:10028"
$env:OPENSEARCH_USERNAME = "avnadmin"
$env:OPENSEARCH_PASSWORD = "<put password here>"
```

### Windows (Command Prompt)

```cmd
set OPENSEARCH_URL=https://os-handson-ykantoni-9e92.h.aivencloud.com:10028
set OPENSEARCH_USERNAME=avnadmin
set OPENSEARCH_PASSWORD=<put password here>
```

### Linux / macOS (bash)

```bash
export OPENSEARCH_URL="https://os-handson-ykantoni-9e92.h.aivencloud.com:10028"
export OPENSEARCH_USERNAME="avnadmin"
export OPENSEARCH_PASSWORD=<put password here>
```

## Run the app

With the virtual environment activated and environment variables set:

```powershell
python aivenhandson.py
```

Expected output is the OpenSearch cluster version, for example:

```text
3.3.2
```

## Run module tests

The tests in `test_aivenhandson.py` connect to your OpenSearch cluster and verify that:

- the connection succeeds
- the cluster version is `3.3.2`

With the virtual environment activated and the same environment variables set as above:

```powershell
python -m unittest test_aivenhandson.py -v
```

On Linux or macOS, use the same command after activating the virtual environment.

If any of the three OpenSearch environment variables is missing, the tests are skipped rather than failing.

## Troubleshooting

- **Missing environment variable**: Python raises `KeyError` if any of the three variables is not set. Set all of them before running the script.
- **Connection errors**: Check that `OPENSEARCH_URL` matches the Service URI in the Aiven console and that your service is running.
