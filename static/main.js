const searchInput = document.getElementById('searchInput');
const suggestionsList = document.getElementById('suggestionsList');

searchInput.addEventListener('input', () => {
  const query = searchInput.value;

  fetch(`http://127.0.0.1:5000/api/suggestions?query=${query}`)
    .then(response => response.json())
    .then(suggestions => {
      displaySuggestions(suggestions);
    });
});

function displaySuggestions(suggestions) {
  suggestionsList.innerHTML = '';

  if (suggestions.length > 0) {
      suggestions.forEach(suggestion => {
        const li = document.createElement('li');
        li.textContent = suggestion;
        suggestionsList.appendChild(li);
      });
  } else {
    return
  }

}