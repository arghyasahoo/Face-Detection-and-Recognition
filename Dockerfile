FROM python:3.8.10
ADD requirements.txt /requirements.txt 
ADD api/app.py /app.py
ADD okteto-stack.yaml /okteto-stack.yaml
RUN pip install -r requirements.txt
EXPOSE 8080
COPY api/model model
COPY api/upload upload
COPY api/results results
CMD ["python","app.py"]