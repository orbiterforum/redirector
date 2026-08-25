FROM python:3.14-slim

RUN apt-get update && apt-get upgrade \
    && apt-get purge -y curl && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml README.md ./
COPY redirector ./redirector
RUN pip install --no-cache-dir .

COPY entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh


ENTRYPOINT ["./entrypoint.sh"]
