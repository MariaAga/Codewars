function humanReadable(seconds) {
  const secs = seconds%60;
  seconds = (seconds - secs)/60;
  const mins = seconds%60;
  seconds = (seconds - mins)/60;
  const hours = seconds;
  return `${hours>9 ? hours:'0'+hours}:${mins>9? mins:'0'+mins}:${secs>9? secs:'0'+secs}`;
}