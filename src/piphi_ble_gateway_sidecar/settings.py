from __future__ import annotations

import os

INTEGRATION_ID = "piphi-ble-gateway-sidecar"
INTEGRATION_NAME = "Piphi Ble Gateway Sidecar"
INTEGRATION_VERSION = "0.1.0"
PROJECT_KIND = "sidecar"
PROJECT_PRESET = "sidecar-worker"
PROJECT_DOMAIN = "sidecar-service"
DEFAULT_PORT = 4210


def runtime_port() -> int:
    raw_port = os.getenv("PORT", str(DEFAULT_PORT))
    try:
        return int(raw_port)
    except ValueError:
        return DEFAULT_PORT
