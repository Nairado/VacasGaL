FROM python:${PYTHON_VERSION}

WORKDIR ${BCK_WORKDIR}

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE ${BCK_PORT}