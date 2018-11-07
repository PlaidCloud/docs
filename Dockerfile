FROM python:2.7

COPY docs /docs
COPY src /src

# Install sphinx and other dependencies
RUN pip install -r /docs/requirements.txt \
&& pip install -e /src/plaid/ \
# Build our documentation
&& mkdir /www \ 
&& sphinx-build -n /docs/docs/source /www 

CMD python /docs/web/main.py