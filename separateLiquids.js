function separateLiquids(glass) {
  height = glass.length;
  if (height <1) return [];
  width = glass[0].length;
  table = {'H':0,'W':0,'A':0,'O':0};
  for (arr of glass){
    for(item of arr){
      table[item]++;
    }
  }
  newGlassArr=[]
  newGlassMatrix=[]
  for(key in table){
    newGlassArr.push(...(key.repeat(table[key]).split("")));
  }
  for(i=0;i<height;i++){
    newGlassMatrix.push((newGlassArr.slice(i*width,(i+1)*width)).reverse());
  }
  
  return newGlassMatrix.reverse();
}
