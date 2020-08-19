FROM python:3.7-slim
COPY requirements.txt /tmp

RUN apt-get update && apt-get install -y gcc libffi-dev libssl-dev libmagic-dev

RUN pip install --no-cache-dir -r /tmp/requirements.txt \
&& rm /tmp/requirements.txt

COPY web/ /web/
COPY docs/ /tmp/docs
COPY plaid /src

RUN sphinx-build -W /tmp/docs/source /web/docs \
 && rm -rf /src

CMD python /web/main.py
