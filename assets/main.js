var getFailedTd=document.querySelectorAll("table tr>td:nth-child(8)")
var getTestcaseHeader=document.getElementById('testSummaryheader')
getFailedTd.forEach((item)=>{
   if(item.innerText == 'Failed'){
       item.parentNode.style.background="#FF7F7F";
       item.parentNode.style.color="#fff";
       getTestcaseHeader.style.background="#FF7F7F";
   }
})


var summaryReportHeader=document.querySelectorAll("table tr>td:nth-child(2)")
summaryReportHeader.forEach((item)=>{
   if(item.innerText == 'Failed'){
       item.parentNode.style.background="#FF7F7F";
       item.parentNode.style.color="#fff";

   }
})
