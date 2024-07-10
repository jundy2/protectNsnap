from fastapi import FastAPI
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.staticfiles import StaticFiles   # Used for serving static files
import uvicorn
import pathlib

states={ 

    "machine_state":False,
    "snap_state":False
}

def set_state(a_state_key, a_state):  
    global states 
    if states.get(a_state_key) is not None: states[a_state_key]=a_state 

def get_state(a_state_key): 
    global states 
    return states[a_state_key]

app = FastAPI()
app.mount("/public", StaticFiles(directory=str(pathlib.Path(__file__).resolve().parent) +"\\public"), name="public") 

@app.get("/", response_class=HTMLResponse)
def get_main_page() -> HTMLResponse:
    with open(str(pathlib.Path(__file__).resolve().parent)+"\\app.html") as html:
        
        return HTMLResponse(content=html.read()) 

@app.get("/get_{variable}", response_class=JSONResponse)
def get_machine_state(variable : str) -> JSONResponse:   
    
    the_state=get_state(variable)
    
    return JSONResponse(f"{variable}_on") if the_state else JSONResponse(f"{variable}_off")

@app.get ("/{status}/{variable}")
def change_machine_state(status : str, variable : str): 
    
    the_state=True if status=="enable" else False
    set_state(variable, the_state) 

    return JSONResponse(f"{variable} has been set to {str(the_state)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6543)
