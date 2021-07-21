FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/services/flaskapp/src
# We copy the requirements.txt file first to avoid cache invalidations
COPY requirements.txt /opt/services/flaskapp/src/
WORKDIR /opt/services/flaskapp/src
RUN pip install -r requirements.txt
COPY . /opt/services/flaskapp/src
EXPOSE 5090
ENV FLASK_APP=app_factory.py
ENV FLASK_ENV=production
CMD flask run -h 0.0.0.0 -p 5000
#CMD python --version
#&& flask run -h 0.0.0.0 -p 5000
