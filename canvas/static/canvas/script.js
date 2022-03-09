document.addEventListener('DOMContentLoaded', function(){
    document.querySelector("#title").addEventListener('click',function(){
        window.location = '/';
    })
    if(document.querySelector("#canvas")){
        document.querySelector("#share").value = window.location.href;
        canvas = document.querySelector("#canvas");
        if (window.innerWidth < window.innerHeight){
            canvas.style.width = (window.innerWidth*0.7)+"px";
            canvas.style.height = canvas.style.width;
        }else{
            canvas.style.height = (window.innerHeight*0.7)+"px";
            canvas.style.width = canvas.style.height;
        }
        for (let i = 0; i < 100; i++){
            divCreate = document.createElement('div');
            divCreate.id = 'sq'+i;
            divCreate.className = "sq";
            divCreate.addEventListener('click', function(){
                change('sq'+i)
            });
            canvas.append(divCreate);
        }
        update();
        setInterval(function(){ 
            update();
        }, 1000);
    }
})

window.addEventListener("resize", function(){
    if(document.querySelector("#canvas")){
        canvas = document.querySelector("#canvas");
        if (window.innerWidth < window.innerHeight){
            canvas.style.width = (window.innerWidth*0.7)+"px";
            canvas.style.height = canvas.style.width;
        }else{
            canvas.style.height = (window.innerHeight*0.7)+"px";
            canvas.style.width = canvas.style.height;
        }
    }
});

function update(){
    const canvasName = document.querySelector("#name").innerHTML;
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    fetch('/update',{
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        mode: 'same-origin',
        body: JSON.stringify({
            canvasName: canvasName
        })
    })
    .then(response => response.json())
    .then(output => {
        for(key in output){
            selector = "#"+key;
            document.querySelector(selector).style.backgroundColor = color(output[key]);
        }
    });
    return false;
}

function change(sqId){
    const canvasName = document.querySelector("#name").innerHTML;
    const value = parseInt(document.querySelector("#color").value);
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch('/change',{
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        mode: 'same-origin',
        body: JSON.stringify({
            canvasName: canvasName,
            value:value,
            sqId:sqId
        })
    })
    .then(()=>update());
} 

function color(n){
    switch(n){
        case 0:
            return '#FFFFFF';
        case 1:
            return '#000000';
        case 2:
            return '#585858';
        case 3:
            return '#c4c4c4';
        case 4:
            return '#f54242';
        case 5:
            return '#f5a442';
        case 6:
            return '#f5e642';
        case 7:
            return '#42f54e';
        case 8:
            return '#6342f5';
        case 9:
            return '#e542f5';
        

    }
}

function copy() {
    /* https://www.w3schools.com/howto/howto_js_copy_clipboard.asp */
    /* Get the text field */
    var copyText = document.querySelector("#share");
  
    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* For mobile devices */
  
     /* Copy the text inside the text field */
    navigator.clipboard.writeText(copyText.value);
  
    return false;
  } 

function downloadImg(){
    /* using https://cdnjs.com/libraries/dom-to-image */
    var select = document.querySelector('#content');

    imgName = document.querySelector('#name').innerHTML;
    filename = imgName+".png";

    domtoimage.toPng(select)
        .then(function (dataUrl){
            let img = new Image();
            img.src = dataUrl;
            downloadGen(dataUrl, filename)
        })
        .catch(function(error){
            console.error('error',error);
        })
}

function downloadGen(url, name){
    let link = document.createElement("a");
    link.download = name;
    link.href = url;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    delete link;
}