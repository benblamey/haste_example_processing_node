FROM python:3.6.3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

RUN git clone https://github.com/benblamey/HarmonicPE.git;cd /app/HarmonicPE;git checkout make_into_module;pip install -e .

# Checkout and install specific version of Haste Storage Client:
RUN git clone https://github.com/benblamey/HasteStorageClient.git;cd /app/HasteStorageClient;git checkout tags/v0.4;pip install -e .

# Make port 80 available to the world outside this container
EXPOSE 80

# Map the HASTE client config (file not needed until the container is run)
#VOLUME ["/haste_storage_client_config.json"]

# Run app.py when the container launch
#CMD ["python", "function.py"]