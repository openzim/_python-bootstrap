FROM python:3.11-bullseye
LABEL org.opencontainers.image.source https://github.com/openzim/great_project

# Install necessary packages
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends locales-all \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && python -m pip install --no-cache-dir -U pip hatch

# Copy code + associated artifacts
COPY src /src/src
COPY pyproject.toml install.sh *.md /src/

# Build + install + cleanup
RUN cd /src/ \
    && hatch build -t sdist \
    && ./install.sh \
    && rm -rf /src

CMD ["great-binary"]
