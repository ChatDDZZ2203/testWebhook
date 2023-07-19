function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function changeWithDelay(delayMS, element) {
  await sleep(delayMS);
  console.log('Is it going to appear?')
  element.innerText = `Can the phrase "different people are celebrating differently" be the excuse for my kind of not healthy celebration of THIS SHIT STARTING TO WORK?`;
}

document.querySelectorAll('.to-change').forEach((element) => {
    changeWithDelay(2000, element);
})

