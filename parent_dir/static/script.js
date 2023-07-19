function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function changeWithDelay(delayMS, element) {
  await sleep(delayMS);
  element.innerText = `This element was changed after ${delayMS / 1000} seconds passed from the program start`;
}

document.querySelectorAll('.to-change').forEach((element) => {
    changeWithDelay(2000, element);
})

