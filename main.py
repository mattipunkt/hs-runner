from fastapi import FastAPI
from fastapi import HTTPException
import subprocess
import re

app = FastAPI()


def remove_trailing_newline(input_string):
    if input_string.endswith('\n'):
        return input_string[:-1]
    return input_string


@app.get("/")
async def root():
    return {"message": "Ping!"}


@app.post("/run/")
async def run_haskell_command(data: dict):
    try:
        declaration = data.get("declaration", "")
        test_expression = data.get("test_expression", "")
        if not declaration:
            raise HTTPException(status_code=400, detail="No declarations provided")
        if not test_expression:
            raise HTTPException(status_code=400, detail="No test expressions provided.")
        else:
            haskell_command = "ghci -e '"+declaration+"' -e '"+test_expression+"'"
            process = subprocess.Popen([haskell_command], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
            stdout, stderr = process.communicate()
            stdout_output = remove_trailing_newline(stdout)
            stderr_output = remove_trailing_newline(stderr)
            process.kill()
            return {"output": stdout_output,
                    "stderr": stderr_output
                    }
        # return {"status": "success", "processed_message": message.upper()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))