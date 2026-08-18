const color =["red","green", "blue","white","brown"]

const tbtn =document.getElementById("tbtn");

function changeColor(){
  const randomIndex=Math.floor(Math.random()*color.length);
  document.body.style.color= color[randomIndex];
}

tbtn.addEventListener("click",changeColor);


console.log("hello");