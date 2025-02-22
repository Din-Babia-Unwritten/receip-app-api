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
	apk add --update --no-cache postgresql-client && \
	# Install Postgresql excess packages (but will be removed in the next commands)
	apk add --update --no-cache --virtual .tmp-build-deps \
		build-base postgresql-dev musl-dev && \
	/py/bin/pip install -r /tmp/requirements.txt && \
	if [ $DEV = "true" ]; \
		then /py/bin/pip install -r /tmp/requirements.dev.txt; \
	fi && \
	# Remove temp packages and folders
	rm -rf /tmp && \
	apk del .tmp-build-deps && \
	adduser \
		--disabled-password \
		--no-create-home \
		django-user

ENV PATH="/py/bin:$PATH"

USER django-user
