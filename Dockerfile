FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-devel
ENV DEBIAN_FRONTEND=noninteractive

# System dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /workspace/DDI-VO

COPY . .

RUN git submodule update --init --recursive
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -e ./glue-factory
RUN pip install --no-cache-dir -e ./TimeSformer
RUN chmod +x download_weights.sh && ./download_weights.sh

CMD ["/bin/bash"]