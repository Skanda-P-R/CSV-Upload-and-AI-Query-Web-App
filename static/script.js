let csvData = '';

document.getElementById('csv-upload').addEventListener('change', function (e) {
    const file = e.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function (event) {
        csvData = event.target.result;
        // console.log('CSV Data as string:\n', csvData);
    };
    reader.readAsText(file);
});

document.getElementById('csv-upload').addEventListener('change', function (e) {
    const file = e.target.files[0];
    if (!file) return;

    document.getElementById('file-name').textContent = file.name;

    const reader = new FileReader();
    reader.onload = function (event) {
        csvData = event.target.result;
        console.log('CSV Data loaded.');
    };
    reader.readAsText(file);
});

async function sendQuery() {
    const query = document.getElementById('query-editor').value;

    const responseContainer = document.getElementById('response-container');
    responseContainer.textContent = 'Processing...';

    try {
        const res = await fetch('/get_response', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                csvData: csvData,
                query: query
            })
        });

        const data = await res.json();
        responseContainer.innerHTML = marked.parse(data.response);
    } catch (err) {
        console.error(err);
        responseContainer.textContent = 'Error retrieving response.';
    }
}