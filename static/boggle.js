function makeBoard() {
  // Make a request to the backend to generate a random board
  // and receive the board data in the response.
  // You can use Axios or other libraries for making the request.
  // Example using Axios:

  return axios.get('/make-board')
  .then(response => {
    // Extract the board data from the response
    const baord = response.data.board;
    // Return the board to be used in the frontend
    return board;
  })
  .catch(error => {
    console.error('Error making board:', error)
  });
}

function checkWord(word) {
  // Make a request to the backend to check the validity of the word
  // and receive the response in the JSON format.
  // Example using Axios:

  return axios.get('/check-word', { params: { word } })
  .then(response => {
    // Extract the response data
    const isValid = response.data.response;
    // Return the validity of the word
    return isValid;
  })
  .catch(error => {
    console.error('Error checking word:', error)
  });
}

function postScore(score) {
// Make a POST request to the backend to submit the score
// and receive the response in the JSON format.
// Example using Axios:
    return axios.post('/post-score', { score })
        .then(response => {
        // Extract the response data
        const brokeRecord = response.data.brokeRecord;
        // Return whether the score broke the high score record
        return brokeRecord;
        })
        .catch(error => {
        console.error('Error posting score:', error);
        });
}

// Export the functions to be used in other parts of the code
export { makeBoard, checkWord, postScore };
