function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function changeWithDelay(delayMS, element) {
  await sleep(delayMS);
  element.innerText = `This element was changed after ${delayMS / 1000} seconds`;
}

document.querySelectorAll('.manipulative').forEach((element) => {
    changeWithDelay(2000, element);
})

