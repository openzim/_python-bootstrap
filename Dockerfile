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

# Copy code + associated artifacts
COPY src /src/src
COPY pyproject.toml *.md /src/

# Install + cleanup
RUN pip install --no-cache-dir /src \
 && rm -rf /src

CMD ["great-binary", "--help"]
