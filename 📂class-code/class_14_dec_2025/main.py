from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def main():
    return {
        'name': 'FastAPI Application',
        'version': '1.0.0'
        
    }