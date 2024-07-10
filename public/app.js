document.addEventListener("DOMContentLoaded", () => { 

   
    statusDiv = document.getElementById('status_div');
    snapButton = document.getElementById('snap_button'); 
    onButton = document.getElementById('on_button'); 
    offButton = document.getElementById('off_button'); 

  

    snapButton.addEventListener("click", ()=>{
        
        fetch('/enable/snap_state') 
        .then(response=>response.json()) 
        .then(function(response) { 
            statusDiv.innerHTML=response;
        });

    });

    onButton.addEventListener("click", ()=>{
        fetch('/enable/machine_state') 
        .then(response=>response.json()) 
        .then(function(response) { 
            statusDiv.innerHTML=response;
        }); 
    });

    offButton.addEventListener("click",()=>{
        fetch('/disable/machine_state') 
        .then(response=>response.json()) 
        .then(function(response) { 
            statusDiv.innerHTML=response;
        }); 
    });
   
});