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

# Prepare application code
COPY . .

# Preload NLP modules to optimize startup
RUN python -c "import numpy; import pandas; import sklearn.neighbors; import sklearn.cluster; import scipy.sparse; \
    print('---> Successfully preloaded all ML dependencies')"

# Remove unnecessary files to reduce image size
RUN find /usr/local/lib/python${PYTHON_VERSION} -type d -name "tests" -o -name "examples" | xargs rm -rf && \
    find /usr/local -name '*.pyc' -delete && \
    find /app -type d -name __pycache__ -exec rm -rf {} +

# Final stage - switch to standard Python image for troubleshooting
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PORT=8080 \
    FUNCTION_TARGET=fetch_news \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH="/app:${PYTHONPATH}"

# Set working directory
WORKDIR /app

# Copy installed packages from builder stage
COPY --from=builder /usr/local /usr/local

# Copy pre-downloaded model
COPY --from=builder /app/model /app/model

# Copy application code
COPY --from=builder /app /app

# Create a symlink to address Cloud Run's specific path expectation
RUN ln -sf $(which python3) /app/python3 && \
    chmod +x /app/python3

RUN echo '#!/bin/bash\n\
echo "Starting application..."\n\
echo "Python version: $(python3 --version)"\n\
echo "Working directory: $(pwd)"\n\
echo "Files in /app: $(ls -la /app)"\n\
echo "Environment: $(printenv | sort)"\n\
\n\
# Start using startup.py instead of simple.py\n\
python3 /app/startup.py\n\
' > /app/run.sh && \
    chmod +x /app/run.sh

# Expose ports
EXPOSE 8080

# Use the shell script as entrypoint
ENTRYPOINT ["/app/run.sh"]