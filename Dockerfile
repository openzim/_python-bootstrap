FROM python:3.11-slim-bookworm
LABEL org.opencontainers.image.source https://github.com/openzim/_python-bootstrap

# Install necessary packages
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      # locales required if tool has any i18n support
      locales-all \
 && rm -rf /var/lib/apt/lists/* \
 && python -m pip install --no-cache-dir -U \
      pip

# Copy pyproject.toml and its dependencies
COPY pyproject.toml README.md /src/
COPY src/great_project/__about__.py /src/src/great_project/__about__.py

# Install Python dependencies
RUN pip install --no-cache-dir /src

# Copy code + associated artifacts
COPY src /src/src
COPY *.md /src/

# Install + cleanup
RUN pip install --no-cache-dir /src \
 && rm -rf /src

CMD ["great-binary", "--help"]
