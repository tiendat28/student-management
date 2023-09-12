FROM python:3.8

WORKDIR /app/backend

# Install Poetry
RUN pip install urllib3==1.26.6
RUN pip install typing-extensions --upgrade
RUN pip install poetry
RUN cd /usr/local/bin
RUN ln -s /opt/poetry/bin/poetry
RUN poetry config virtualenvs.in-project true
