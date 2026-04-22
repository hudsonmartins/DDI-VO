# DDI-VO

DDI-VO is a visual odometry model. This repository contains the code for training, testing, and running the model.

## Installation

### 1. Clone the repository

This repository uses Git submodules (such as `glue-factory` and others). To clone it properly, use the `--recursive` flag:

```bash
git clone --recursive <repository_url>
cd DDI-VO
```

If you have already cloned the repository without the submodules, you can initialize them by running:

```bash
git submodule update --init --recursive
```

### 2. Install dependencies

It is recommended to use a virtual environment (e.g., Python venv or Conda). Install the required Python packages with:

```bash
pip install -r requirements.txt
```

*(Note: Ensure you have PyTorch and Torchvision installed properly according to your CUDA version prior to installing the remaining requirements if needed).*

### 3. Download Model Weights

To download the required pre-trained weights (e.g., for LightGlue / SuperPoint), run the provided shell script:

```bash
chmod +x download_weights.sh
./download_weights.sh
```

## Usage

### Testing / Inference

You can run the inference/testing script using `test.py`. An example command looks like:

```bash
python test.py \
    --dataset_config configs/ddi_vo.yaml \
    --model_config configs/ddi_vo_model.yaml \
    --model_path checkpoints/best_model.tar \
    --output_path results \
    --trajectory_file traj.txt 
```
*(Make sure to adjust the config and checkpoint paths according to your local files).*

### Training

To train the model on datasets like KITTI, Queenscamp, or TartanAir, use the `train.py` script:

```bash
python train.py ddi_vo_experiment --config configs/train_example.yaml --use_cuda
```
