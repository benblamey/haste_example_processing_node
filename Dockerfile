# HIO requires python 3.
FROM python:3.6.3

# Set the working directory to /app
WORKDIR /app

# Checkout and install Harmonic PE:
RUN git clone https://github.com/benblamey/HarmonicPE.git;cd /app/HarmonicPE;git checkout master;pip install .

# Checkout and install the Haste Storage Client:
RUN git clone https://github.com/benblamey/HasteStorageClient.git;cd /app/HasteStorageClient;git checkout v0.4;pip install .


# Make port 80 available (required for the listening daemon)
EXPOSE 80



# Add the example sript (change this to your own:)
ADD . /app

CMD ["python", "function.py"]
