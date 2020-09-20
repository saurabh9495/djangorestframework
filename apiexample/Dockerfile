FROM python:3

COPY . /home/test/

RUN pip3 install -r /home/test/requirements.txt

RUN ls -l /home/test

ENTRYPOINT ["python3", "/home/test/manage.py", "runserver", "--insecure", "--noreload", "0.0.0.0:80"]