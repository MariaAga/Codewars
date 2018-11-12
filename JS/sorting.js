function sorting(obj, item) {
  if (!obj[item]) {
    obj[item] = 0;
  }
  obj[item]++;
  return obj;
}

function scramble(str1, str2) {
  if(str1.len<str2.len) return false;
  str1 = str1.split('');
  str2 = str2.split('');
  
  txt1 = str1.reduce(sorting, {});
  txt2 = str2.reduce(sorting, {});
  for (let key in txt2) {
    if(!txt1[key]) return false;
    if(txt2[key]>txt1[key])  return false;
  }
  return true;
}
