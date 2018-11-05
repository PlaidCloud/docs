FROM python:2.7

COPY docs /docs
COPY src /src

# Install sphinx and other dependencies
RUN pip install -r /docs/requirements.txt \
# Build our documentation
&& mkdir /www \ 
&& sphinx-build -c /src/sphinx /src /www

# Throw away plaid source before publishing cd

CMD python /docs/web/main.py --port 80