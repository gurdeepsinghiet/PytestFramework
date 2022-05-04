var getFailedTd=document.querySelectorAll("table tr>td:nth-child(8)")
getFailedTd.forEach((item)=>{
   if(item.innerText == 'Failed'){
       item.parentNode.style.background="red";
       item.parentNode.style.color="#fff";
   }
})
console.log(getFailedTd)
