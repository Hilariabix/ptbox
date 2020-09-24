FROM python:3.5-alpine
ADD *.py ~/
ENTRYPOINT [ "/usr/local/bin/python", "~/main.py" ]
