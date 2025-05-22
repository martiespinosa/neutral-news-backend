# Build stage for dependencies
ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-slim AS builder

# Set working directory and configure PATH
WORKDIR /app
ENV PATH="/usr/local/bin:$PATH"

# Install build dependencies and clean up in a single layer
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install all Python dependencies in a single layer
RUN pip install --upgrade pip && \
    pip install --no-cache-dir lxml lxml_html_clean newspaper3k==0.2.8 && \
    python -c "from newspaper import Article; print('Newspaper import successful')" && \
    pip install --no-cache-dir functions-framework && \
    which functions-framework && \
    functions-framework --help && \
    rm -rf ~/.cache/pip

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir --default-timeout=1000 torch>=1.9.0 --extra-index-url https://download.pytorch.org/whl/cpu && \
    pip install --no-cache-dir --default-timeout=1000 -r requirements.txt && \
    rm -rf ~/.cache/pip

# Download and cache the model in a separate step (kept separate for better caching)
RUN mkdir -p /app/model && \
    python -c "from sentence_transformers import SentenceTransformer; \
    model_name = 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'; \
    print('---> Downloading model ' + model_name); \
    model = SentenceTransformer(model_name); \
    model.save('/app/model'); \
    print('---> Model downloaded and saved to /app/model')"

# Create a health check Python script since shell scripts can't be used in distroless
RUN echo 'import http.server, socketserver\n\
class HealthHandler(http.server.BaseHTTPRequestHandler):\n\
    def do_GET(self):\n\
        if self.path == "/_ah/health":\n\
            self.send_response(200)\n\
            self.send_header("Content-type", "text/plain")\n\
            self.end_headers()\n\
            self.wfile.write(b"Healthy")\n\
\n\
def start_health_server():\n\
    import threading\n\
    def run_server():\n\
        with socketserver.TCPServer(("", 8081), HealthHandler) as httpd:\n\
            httpd.serve_forever()\n\
    t = threading.Thread(target=run_server, daemon=True)\n\
    t.start()\n\
' > /app/health_check.py

# Prepare application code
COPY . .

# Remove unnecessary files to reduce image size
RUN find /usr/local/lib/python${PYTHON_VERSION} -type d -name "tests" -o -name "examples" | xargs rm -rf && \
    find /usr/local -name '*.pyc' -delete && \
    find /app -type d -name __pycache__ -exec rm -rf {} +

# Final stage with distroless Python
FROM gcr.io/distroless/python3:nonroot

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PORT=8080 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH="/app:${PYTHONPATH}"

# Set working directory
WORKDIR /app

# Copy installed packages from builder stage
COPY --from=builder /usr/local /usr/local

# Copy pre-downloaded model
COPY --from=builder /app/model /app/model

# Copy application code and health check
COPY --from=builder /app /app

# Expose ports (main app and health check)
EXPOSE 8080 8081

# Health check using Python HTTP request instead of curl (distroless has no curl)
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD ["python3", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8080/_ah/health')"]

# Set entrypoint (must use exec form for distroless)
CMD ["python3", "-m", "functions_framework", "--target=fetch_news", "--port=8080"]