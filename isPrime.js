function isPrime(input) {
    for (let i = 2; i <= Math.sqrt(input); i++) {
        if (input % i == 0) {
          return false;
        }
    }
    return true;
}   

function sumOfDivided(lst) {
  sum = [];
  max = Math.max(...(lst.map(a => Math.abs(a))));
  primes = [];
  
  
  for (let i = 2;i<=max;i++){
    if(isPrime(i)) {
      primes.push(i);
    }
  }

  for (let a of lst){
    for (let i=0;primes[i]<=Math.abs(a);i++){
      if(a % primes[i] == 0){
        sum[''+primes[i]] = sum[''+primes[i]]? sum[''+primes[i]]+a : a;
      }
    }
  }
  console.log(sum);
  let sumArray = [];
  for (key of Object.keys(sum)){
    //if (sum[key]>0)
    sumArray.push([parseInt(key),sum[key]]);
  }
  return sumArray;
}
