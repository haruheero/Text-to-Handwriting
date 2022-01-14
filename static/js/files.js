document.querySelector('#myfile').onchange=function(){
    document.getElementById('demo').innerHTML='File Uploaded';
}

var elem=document.getElementById('file-upload');
if(elem)
{
    let elem=document.getElementsByClassName('remove');
    for(let i=0;i<elem.length;i++)
    {
        elem[i].remove();
    }
    document.getElementsByClassName('clickbutton')[0].remove();
}

const checkbox=document.getElementById('checkbox');
checkbox.addEventListener('change',()=>{
    document.body.classList.toggle('dark');
});