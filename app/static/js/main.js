const quoteElem = document.getElementById('quote');

function getNewQuote() {
    fetch('/quote')
        .then(response => response.json())
        .then(data => {
            quoteElem.innerText = data.quote;
        })
        .catch(error => console.error(error));
}
