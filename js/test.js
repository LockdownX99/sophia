const count = document.getElementById("count");

const counter = document.getElementById("counter");

let p = 0;

//function increment(){
//p +=1;
//count.innerText=p;
//}
//increment()

counter.addEventListener("click",()=>count.innerText=p=p+1);

let result = document.getElementById("result");

function save(){
  console.log(p)
  display =p+" - ";
  
  result.innerText +=display;
}

save()

