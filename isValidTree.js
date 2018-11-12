function isValidTree(tree){
  if(!tree) return true;
  if(tree.ornament!=='star') return false;
  return isValidSubTree(tree.left) && isValidSubTree(tree.right);
}

function isValidSubTree(root){
  if(!root) return true;
  if(!root.left && !root.right && root.color!=='blue') return false;
  if((root.left || root.righ) && root.color!=='red') return false;
  return isValidSubTree(root.left) && isValidSubTree(root.right);
}