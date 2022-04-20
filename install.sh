wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
sudo md5sum Miniconda3-latest-Linux-armv7l.sh
sudo /bin/bash Miniconda3-latest-Linux-armv7l.sh
source ~/.bashrc

conda create -n DioviEnv python=3.6
source activate DioviEnv
pip install -r requirements.txt
bash weights/download_weights.sh
mv yolov3.weights weights/
python deteccion_video.py
