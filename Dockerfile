FROM python:3
WORKDIR /user/scr/app
COPY basicstatistics.py .
COPY CheckIsCompressed.py .
COPY Choosefiledialog.py .
COPY filterfastq.py .
COPY fqgui_support.py .
COPY fqgui.py .
COPY graphgeneration.py .
COPY merge_subtract.py .
COPY savefiledialog.py .
COPY searchsequence.py .
COPY test.py .
COPY trimprimer.py .
COPY trimquality.py .
COPY validatefastq.py .
COPY test.fastq
COPY requirments.txt .
RUN pip install --no-cache-dir -r requirments.txt
CMD ["python","./fqgui.py"]