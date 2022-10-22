// Import module via named import syntax (needs type="module" in <script> tag in HTML file, or browser will raise an error "not a module")
import { toggleDisplay, setRandomBackground } from "./app-modules.js";

const act1button = document.getElementById('action1button');
const act1paragraph = document.getElementById('action1paragraph');

act1button.addEventListener('click', () => {
  toggleDisplay(act1paragraph);
  setRandomBackground(act1paragraph);
});