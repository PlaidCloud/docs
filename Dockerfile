FROM python:2.7

WORKDIR /

# Install sphinx and other dependencies
RUN pip install \
sphinx --upgrade \
sphinxcontrib-fulltoc \
recommonmark \
sphinxcontrib.httpdomain

# Build our documentation
RUN cd /docs/ \
&& sphinx-build source build

# Throw away plaid source before publishing 