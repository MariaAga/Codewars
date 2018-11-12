function getWeight(number){
  number = number.split("");
  return number.reduce((total, digit) => {return total+parseInt(digit)},0);
}

function orderWeight(strng) {
    let arr = strng.split(" ");

    arr= arr.sort((a,b)=>{
      if(getWeight(a) === getWeight(b)){
        return a<b? -1:1;
      }
      return getWeight(a) - getWeight(b);
    });

    return arr.join(' ');
}