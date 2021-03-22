FROM python:3.8

WORKDIR /transfer

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt


EXPOSE 8501

COPY . /transfer

ENTRYPOINT ["streamlit", "run"]

CMD ["transfer.py"]

