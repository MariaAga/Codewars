
function pad(num){
  return num>9? num:'0'+num;
}
function humanReadable(seconds) {
  const secs = seconds%60;
  const mins = ((seconds-secs)/60)%60;
  const hours = ((seconds-secs-(mins*60))/3600);
  return `${pad(hours)}:${pad(mins)}:${pad(secs)}`;
}