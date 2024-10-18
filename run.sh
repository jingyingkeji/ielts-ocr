#!/bin/sh

#uvicorn main:app --host 0.0.0.0 --port 9003 --reload
nohup uvicorn main:app --host 0.0.0.0 --port 9003 --reload 2>/tmp/ielts-ocr.log 1>&2 &