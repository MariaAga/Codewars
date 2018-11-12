function allLeavesAtSameLevel(node) {
  if(!node) return true;
  let l =[]
  function levelCount(node,lvl){
    if(!node.left && !node.right){
      l.push(lvl);
      return;
    }
    if(node.left) levelCount(node.left,lvl+1);  
    if(node.right) levelCount(node.right,lvl+1); 
  }
  levelCount(node,0);
  for(let i=0;i<l.length-1;i++){
    if(l[i]!==l[i+1]) return false;
  }
  return true;
}

