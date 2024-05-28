FROM mcr.microsoft.com/playwright:v1.40.0-jammy

RUN useradd -ms /bin/bash dev
RUN apt-get update && apt-get install -y make python3 python3-pip


USER dev

ADD ./main.py /home/dev
ADD ./requirements.txt /home/dev
ADD ./Makefile /home/dev

WORKDIR /home/dev

RUN make install

ENTRYPOINT ["python3", "main.py"]
CMD []

