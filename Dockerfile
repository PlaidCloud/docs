FROM python:2.7-slim
COPY docs /docs
COPY src /src

# Install sphinx and other dependencies
RUN pip install -r /docs/requirements.txt \
# Build our documentation
&& mkdir /www \ 
&& sphinx-build /docs/docs/source /www \
&& rm -rf /src

CMD python /docs/web/main.py