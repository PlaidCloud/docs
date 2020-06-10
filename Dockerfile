FROM python:2.7-slim
COPY requirements.txt /tmp

RUN pip install --no-cache-dir -r /tmp/requirements.txt \
&& rm /tmp/requirements.txt

COPY web/ /web/
COPY docs/ /tmp/docs
COPY plaid /src

RUN sphinx-build /tmp/docs/source /web/docs \
 && rm -rf /src

CMD python /web/main.py
