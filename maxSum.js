function maxSum(root) {
  if(!root){
    return 0;
  }
  return Math.max(maxSum(root.left),maxSum(root.right))+ root.value;
}