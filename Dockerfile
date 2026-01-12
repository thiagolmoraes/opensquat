FROM astral/uv:python3.14-bookworm-slim

# Metadata
LABEL maintainer="openSquat Team"
LABEL description="Domain squatting and phishing detection tool"
LABEL version="2.1.2"

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive

# Create working directory
WORKDIR /app

# Copy configuration files
# using setup.py for production installation
# but if you want to develop, would nice to create a Dockerfile.dev
COPY uv.lock pyproject.toml setup.py ./

# Copy the opensquat package
COPY opensquat/ ./opensquat/

# Copy examples (optional, but useful for tests)
COPY examples/ ./examples/

# Install the package and dependencies using uv sync
# --frozen ensures exact versions from uv.lock are used
RUN uv sync --frozen --no-dev

# install setup
RUN uv run python setup.py install

# Add venv to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Create directories for results and input
RUN mkdir -p /app/results /app/input

# Volumes for data persistence
VOLUME ["/app/results", "/app/input"]

# Default working directory
WORKDIR /app

# run 4ever
ENTRYPOINT ["opensquat"]

# Default command (shows help)
CMD ["-h"]