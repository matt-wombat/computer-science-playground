// Import module first (needs type="module" in <script> tag in HTML file)
import { toggleDisplay, setRandomBackground } from "./app-modules.js";

const act1button = document.getElementById('action1button');
const act1button2 = document.getElementById('action1button2');

act1button.addEventListener('click', () => {
  toggleDisplay(act1button2);
  setRandomBackground(act1button2);
});