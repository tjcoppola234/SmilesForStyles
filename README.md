# SmilesForStyles
WPI CS 539 - A facial expression recognition model for analyzing product favorability

## Facial Emotion Recognition Setup
1. (Optional) Set up a virtual python environment for package management following these steps:
    - Create the virtual environemnt: `python -m venv virtualenv`
    - Activate the environment:
        - `./virtualenv/Scripts/activate.bat` OR `./virtualenv/Scripts/Activate.ps1` on Windows
        - `source virtualenv/bin/activate` on mac/linux
    - install required packages through pip: <a href="https://pytorch.org/get-started/locally/">PyTorch</a>, <a href="https://docs.fast.ai/">Fastai</a>
2. Install OpenCV via `pip install opencv-contrib-python`
3. Install Deepface via `pip install deepface`

## Clothing Attribute Prediction Setup
1. Download img.zip from the DeepFashion Category and Attribute Prediction Benchmark <a href="https://drive.google.com/file/d/0B7EVK8r0v71pa2EyNEJ0dE9zbU0/view?usp=drive_link&resourcekey=0-CPiKS-AiE8IDonk54WJ5_w">Link Here</a>
2. Extract img.zip into the deepfashion directory and remove the redundant img directory (it should look like deepfashion/img/2-in-1_Space_Dye_Athletic_Tank, not deepfashion/img/img/2-in-1_Space_Dye_Athletic_Tank)
3. Download multilabel-test.csv and multilabel-train.csv from <a href="https://github.com/tsennikova/fashion-ai/tree/main/clothes-categories">tsennikova/fashionai/clothes-categories</a>
4. Place multilabel-test.csv and multilabel-train.csv in the fashion_ai directory
5. Step through the jupyter notebook
