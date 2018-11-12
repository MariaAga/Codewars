function diamond(n){
  if (n<3) return null;
  diam = []
  for(let i= n%2===2 ? 0:1;i<n;i+=2){
    diam.push(" ".repeat((n-i)/2) + "*".repeat(i));
  }
  //diam.push("*".repeat(n));
  for(let i= n;i>0;i-=2){
    diam.push(" ".repeat((n-i)/2) +"*".repeat(i));
  }
  diam.push("");
  return diam.join('\n');
}



' *\n***\n *\n'
' *\n***\n***\n *\n'