FROM python:2.7

COPY docs /docs
COPY src /src

# Install sphinx and other dependencies
RUN pip install -r /docs/requirements.txt

# Build our documentation
RUN cd /docs/docs && sphinx-build source build

# Throw away plaid source before publishing cd

CMD python /docs/web/main.py --port 80