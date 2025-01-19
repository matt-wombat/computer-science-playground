// This fetch.js is used in fetch.html

const fetchButton = document.getElementById('fetchButton');
const inputField = document.getElementById('inputField');
const resDiv = document.getElementById('resultDiv');
const queryApi = "https://api.datamuse.com/words";

let queryWord = '';
let queryType = '';
let queryString = '';
let queryEndpoint = '';
let asyncType = '';

const formatResponse = jsonData => {
  if (!jsonData.length) {
    resDiv.innerHTML = 'Error: No data<br><br>\n\n';
    return;
  };

  let words = [];
  let maxNum = Math.min(jsonData.length, 10);
  for(let i = 0; i < maxNum; i++){
    words.push(`<li>${jsonData[i].word}</li>`);
  }
  words = words.join("");

  // Manipulates responseField to render the modified response
  resDiv.innerHTML = '<p>Found words: </p><ol>' + words + '</ol>';
  return;
};

const getData = () => {
  queryWord = inputField.value;
  queryType = document.querySelector('input[name="query_type"]:checked').id;
  queryString = queryType + '=' + queryWord;
  queryEndpoint = queryApi + '?' + queryString;
  asyncType = document.querySelector('input[name="async_type"]:checked').id;

  switch (asyncType) {
    case 'promise':
      getDataPromise();
      break;

    case 'asyncawait':
      getDataAsync();
      break;
  }
};

const getDataPromise = () => {
  fetch(queryEndpoint)
  .then(response => {
    if (response.ok) {
      return response.json();
    };
  
    throw Error('Request failed!');
  }, networkError => {
    console.log(networkError.message);
  })
  .then(jsonResponse => {
    formatResponse(jsonResponse);
  })
}

const getDataAsync = async () => {
  try {
    const response = await fetch(queryEndpoint);
    if (response.ok) {
      const jsonResponse = await response.json();
      formatResponse(jsonResponse);
    };

  } catch(error) {
    console.log(error);
  };
}



fetchButton.addEventListener('click', getData);


