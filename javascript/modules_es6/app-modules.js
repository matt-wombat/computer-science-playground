// Variant 1: Use export keyword in front of function definition
export const toggleDisplay = (domElem) => {
  if (domElem.style.display === 'none') {
    domElem.style.display = 'block';
  } else {
    domElem.style.display = 'none';
  }
}

const setRandomBackground = (domElem) => {
  const red = Math.random() * 255;
  const green = Math.random() * 255;
  const blue = Math.random() * 255;

  domElem.style.background = `rgb(${red}, ${green}, ${blue})`
}

// Variant 2: Use named export syntax to export function definitions
export { setRandomBackground };
