export function convertTime(duration) {
  let minutes = Math.floor(duration / 60);
  const seconds = duration - (minutes * 60);
  if (minutes > 60) {
    const hours = Math.floor(minutes / 60);
    minutes = minutes - (hours * 60);
    return `${hours}:${minutes}:${seconds}`;
  } else if (minutes > 0) {
    return `${minutes}:${seconds}`;
  }

  return `${seconds}`;
}

export function dateUtils(date) {
  return new Date(date).toLocaleDateString("ru-RU", {day: "numeric", month: "long"});
}
