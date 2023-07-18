function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function changeWithDelay(delayMS, element) {
  await sleep(delayMS);
  element.innerText = `I WAS CHANGED AFTER ${delayMS / 1000} seconds!`;
}

document.querySelectorAll('.manipulative').forEach((element) => {
    changeWithDelay(3000, element);
})

