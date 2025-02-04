### ProcessCopilot

### Create a virtual environment
```
 python3 -m venv venv
```
### Activate it 
```
source venv/bin/activate
```

### Install the required packages in root folder
```
pip install -r requirements.txt
```

### install tesserect-ocr in your laptop or machine 
```
  sudo apt install -y tesseract-ocr
```
### install german language tesserect-ocr 
```
  sudo apt-get install tesseract-ocr-deu
```
### add it to your path 
```
 export TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata
```
 
### Navigate to the backend folder
```
 cd backend
```
### Run the backend 
```
 uvicorn main:app --reload
```

### Navigate to the frontend folder in separete terminal 
 cd frontend
### run the frontend 
```
  streamlit run main.py
```  








