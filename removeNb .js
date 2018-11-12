function removeNb (n) {
  let a;
  let arr =[];
  for(let b=1;b<=n;b++){
    a = ((n*(n+1))/2 -b)/(b+1);
    if (a === Math.floor(a) && a<=n)
      arr.push([b,a]);
  }
  return arr;
}