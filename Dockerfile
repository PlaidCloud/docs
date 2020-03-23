FROM python:2.7-slim
COPY requirements.txt /tmp

RUN pip install --no-cache-dir -r /tmp/requirements.txt \
&& rm /tmp/requirements.txt

COPY web/ /web/
COPY docs/ /tmp/docs

RUN mkdir /docs \ 
 && sphinx-build /tmp/docs/source /web/docs \
 && ln -s /web/docs /web/docs/docs

CMD python /web/main.py