first install 

py --version
uv --version

add the fastapi[standard]

uv add fastapi[standard]

then activate the virtual enviroment 

by run this command 

.venv/Scripts/activate

now run the file throw this command

uv run uvicorn main:app --reload  