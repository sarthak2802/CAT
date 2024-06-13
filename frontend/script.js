document.getElementById('question-form').addEventListener('submit', async function (event) {
    event.preventDefault();
    const questionInput = document.getElementById('question').value;
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = 'Loading...';

    try {
        const response = await fetch('http://localhost:5000/solve-question', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question: questionInput })
        });
        const data = await response.json();
        resultDiv.innerHTML = `<pre>${data.answer}</pre>`;
    } catch (error) {
        resultDiv.innerHTML = 'An error occurred. Please try again.';
    }
});
