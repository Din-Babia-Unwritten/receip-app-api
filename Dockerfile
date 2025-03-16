FROM python:3.9-alpine3.13

LABEL maintainer="Din"

# No need to buffer the output
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app

WORKDIR /app
EXPOSE 8000

# In default, we are not running in development mode
ARG DEV=false
RUN python -m venv /py && \
  /py/bin/pip install --upgrade pip && \
  # Install Postgresql required
  # jpeg-dev -> dependency for images (Python-Pillow)
  apk add --update --no-cache postgresql-client jpeg-dev && \
  # Install Postgresql excess packages (but will be removed in the next commands)
  apk add --update --no-cache --virtual .tmp-build-deps \
  # zlib, zlib-dev -> dependency for image (Python-Pillow)
  build-base postgresql-dev musl-dev zlib zlib-dev && \
  /py/bin/pip install -r /tmp/requirements.txt && \
  if [ $DEV = "true" ]; \
  then /py/bin/pip install -r /tmp/requirements.dev.txt; \
  fi && \
  # Remove temp packages and folders
  rm -rf /tmp && \
  apk del .tmp-build-deps && \
  # Add media and static directories for volumes
  adduser \
  --disabled-password \
  --no-create-home \
  django-user && \
  # Set django-user ownership, mode, and permissions to /vol -R 'recursive'
  mkdir -p /vol/web/media && \
  mkdir -p /vol/web/static && \
  chown -R django-user:django-user /vol && \
  chmod -R 755 /vol

ENV PATH="/py/bin:$PATH"

USER django-user
