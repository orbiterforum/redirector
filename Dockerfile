FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./redirector /code/redirector

EXPOSE 8000

CMD ["uvicorn", "redirector.main:app", "--host", "0.0.0.0", "--use-colors", "--port", "8000"]
