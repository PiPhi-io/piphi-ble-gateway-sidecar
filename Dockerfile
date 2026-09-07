FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml ./
COPY src ./src
RUN pip install --no-cache-dir .
EXPOSE 4210
CMD ["uvicorn", "piphi_ble_gateway_sidecar.main:app", "--host", "0.0.0.0", "--port", "4210"]
