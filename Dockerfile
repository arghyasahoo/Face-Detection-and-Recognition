FROM python:3.8.10
ADD requirements.txt /requirements.txt 
ADD app.py /app.py
ADD okteto-stack.yaml /okteto-stack.yaml
RUN pip install -r requirements.txt
EXPOSE 8080
COPY ./model model
COPY ./upload upload
COPY ./results results
CMD ["python","app.py"]