Create environment:

```
conda create -n wineq python=3.8 -y
conda create -n wineq python=3.8 -y
conda activate wineq
```

Create requirements.txt:

```
touch requirements.txt

dvc
dvc[gdrive]
scikit-learn
pandas
pytest
tox
flake8

pip install -r requirements.txt

```

Execute template.py
```
python template.py
```

```
copy winequality.csv to data_given folder
```