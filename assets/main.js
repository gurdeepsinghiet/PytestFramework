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

document.addEventListener("DOMContentLoaded", function(event) {
    const getPassedTestcase=Number(document.getElementById("pass").textContent);
    const getFailedTestcase=Number(document.getElementById("fail").textContent);
    const getTotalTestcase=Number(document.getElementById("total").textContent);
    passFailed=[getPassedTestcase,getFailedTestcase];
    passPercentage=(getPassedTestcase/getTotalTestcase*100).toFixed(2);
    failPercentage=(getFailedTestcase/getTotalTestcase*100).toFixed(2);
    passFailpercentage=[passPercentage,failPercentage];
    color=["green","red"];
    passFailStatus=["Passed","Failed"]
    console.log(passFailed)
  var example={};
  example.id="pie1";
  example.radius=150;
  example.segments=[];
  example.persegments=[];
  for(i=0;i<2;i++){
     var item={};
     var peritem={};
    item.value=passFailed[i];
    item.color=color[i];
    peritem.value=passFailpercentage[i];
    peritem.status=passFailStatus[i];
    example.segments.push(item);
    example.persegments.push(peritem);
   }
   console.log(example)

   pie(example);

});


function pie(data){
  // set size of <svg> element
  var b = document.getElementById("pie1");
  b.setAttribute("width", 5*data.radius);
  b.setAttribute("height", 2*data.radius);
  // calculate sum of values
  var sum=0;
  var radius=data.radius;
  for(var e=0; e<data.segments.length; e++){
    sum+=data.segments[e].value;
  }
  // generate proportional pie for all segments
  var startAngle=0, endAngle=0;
  for(var i=0; i<data.segments.length; i++){

    var element=data.segments[i];
     var angle=element.value * 2 * Math.PI / sum;
    endAngle+=angle;
    if(element.value != 0 && element.value != sum){

    var pathStr=
        "M "+(radius)+","+(radius)+" "+
        "L "+(Math.cos(startAngle)*radius+radius)+","+
             (Math.sin(startAngle)*radius+radius)+" "+
        "A "+(radius)+","+(radius)+
             " 0 "+(angle<Math.PI?"0":"1")+" 1 "+
             (Math.cos(endAngle)*radius+radius)+","+
             (Math.sin(endAngle)*radius+radius)+" "+
        "Z";

    console.log(pathStr)
    var svgPath=makeSVG('path',{d: pathStr, fill: element.color});
    b.append(svgPath);
    startAngle+=angle;

  }else{

  if(element.value == sum && data.persegments[i].status == "Passed"){
         console.log(element.value);
          console.log(data.persegments[i].status);
          var svgPath1=makeSVG('circle',{cx: 150,cy:150,r:150, fill: element.color});


        b.append(svgPath1);
  }else if(element.value == sum  && data.persegments[i].status == "Failed"){
          console.log(element.value);
          console.log(data.persegments[i].status);
          var svgPath1=makeSVG('circle',{cx: 150,cy:150,r:150, fill: element.color});


        b.append(svgPath1);

  }

  }
}
  var startAngle=0, endAngle=0;
  for(var i=0; i<data.persegments.length; i++){
    var element=data.persegments[i];
    var element1=data.segments[i];
    if(element1.value != 0 && element1.value != sum){
    var angle=element.value * 2 * Math.PI / 100;
    var el= document.createElementNS('http://www.w3.org/2000/svg', 'text');
    console.log(Math.sin(startAngle)*radius+radius)
     el.setAttribute("x", 150+Math.cos(startAngle) * radius/2+20)
     el.setAttribute("y", 150+Math.sin(startAngle) * radius/2+20)
     el.setAttribute("stroke","none")
     el.setAttribute("fill","#fff")
     el.setAttribute("text-anchor","start")
     const textNode = document.createTextNode(element.value+"%");
     el.appendChild(textNode);
     b.append(el);
     startAngle+=angle;

     }else{

     if(element1.value == sum && data.persegments[i].status == "Passed"){

     var el= document.createElementNS('http://www.w3.org/2000/svg', 'text');
     el.setAttribute("x", 150)
     el.setAttribute("y", 150)
     el.setAttribute("stroke","none")
     el.setAttribute("fill","#fff")
     el.setAttribute("text-anchor","start")
     const textNode = document.createTextNode(element.value+"%");
     el.appendChild(textNode);
     b.append(el);

     }else if(element1.value == sum  && data.persegments[i].status == "Failed"){

     var el= document.createElementNS('http://www.w3.org/2000/svg', 'text');
     el.setAttribute("x", 150)
     el.setAttribute("y", 150)
     el.setAttribute("stroke","none")
     el.setAttribute("fill","#fff")
     el.setAttribute("text-anchor","start")
     const textNode = document.createTextNode(element.value+"%");
     el.appendChild(textNode);
     b.append(el);
     }

  }
  }

};

// SVG Maker - to draw SVG by script
function makeSVG(tag, attrs) {
  var el= document.createElementNS('http://www.w3.org/2000/svg', tag);
  for (var k in attrs)
    el.setAttribute(k, attrs[k]);
  return el;
} //SVG Maker
