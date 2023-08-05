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
        const a = document.createElement("a")
        a.textContent = suggestion.suggestion_title;

        const value = suggestion.suggestion_url;
        const idPattern = /ln=\d+/; // Regular expression pattern to match 'ln=' followed by one or more digits
        const biblioPattern = /document.resultados\.codbiblio\.value='([^']+)'/; // Regular expression pattern to match 'document.resultados.codbiblio.value=' followed by the desired value between single quotes
        
        const idMatch = value.match(idPattern);
        const biblioMatch = value.match(biblioPattern);
        let recordId = ""
        let recordBiblioCode = ""

        if (idMatch && biblioMatch) {
          recordId = idMatch[0]; // The matched value will be stored in the first element of the match array
          recordBiblioCode = biblioMatch[1]
          console.log(recordId, recordBiblioCode); // Output: ln=206440727
        } else {
          console.log("No match found.");
        }

        // console.log(suggestion.suggestion_url.split(";"))

        a.href = `https://www.cnc.una.py/opac/cliente.cgi?codbiblio=${recordBiblioCode}&mode=full&cclquery=${recordId}`

        
        li.appendChild(a)
        suggestionsList.appendChild(li);
      });
  } else {
    return
  }

}