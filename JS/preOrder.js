/*
A Node has the following properties:
var data; // A number or string.
Node left; // Undefined if there is no left child.
Node right; // Undefined if there is no right child.
*/

// 1.) Root node, 2.) traverse left subtree, 3.) traverse right subtree.
function preOrder(node)
{
  var s = [];
  preOrderRec(node);
  function preOrderRec(node)
  {
    if(!node){
      return;
    }
    s.push(node.data);
    preOrderRec(node.left);
    preOrderRec(node.right);
  }
  return s;
  
}

// 1.) Traverse left subtree, 2.) root node, 3.) traverse right subtree.
function inOrder(node)
{
  var s = [];
  inOrderRec(node);
  function inOrderRec(node)
  {
    if(!node){
      return;
    }
    inOrderRec(node.left);
    s.push(node.data);
    inOrderRec(node.right);
  }
  return s;
}

// 1.) Traverse left subtree, 2.) traverse right subtree, 3.) root node.
function postOrder(node)
{
  var s = [];
  inOrderRec(node);
  function inOrderRec(node)
  {
    if(!node){
      return;
    }
    inOrderRec(node.left);
    inOrderRec(node.right);
    s.push(node.data);
  }
  return s;
}