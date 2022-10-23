// This fetch.js is used in fetch.html

const fetchButton = document.getElementById('fetchButton');
const inputField = document.getElementById('inputField');
const resDiv = document.getElementById('resultDiv');
const queryApi = "https://api.datamuse.com/words"

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
  const queryWord = inputField.value;
  const queryType = 'sl';
  const queryString = queryType + '=' + queryWord;
  const queryEndpoint = queryApi + '?' + queryString;

  fetch(queryEndpoint)
    .then(response => {
      if (response.ok) {
        return response.json();
      }

      throw Error('Request failed!');
    }, networkError => {
      console.log(networkError.message);
    })
    .then(jsonResponse => {
      // resDiv.innerHTML = 'Response: <br><br>\n\n' + jsonResponse;
      formatResponse(jsonResponse);
    })

  //resDiv.innerHTML = 'Query Endpoint: ' + queryEndpoint;

};


fetchButton.addEventListener('click', getData);


