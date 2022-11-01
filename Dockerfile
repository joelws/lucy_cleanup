FROM python:3.9.4
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python", "-m", "lucy_sfdc_cleanup.main"]