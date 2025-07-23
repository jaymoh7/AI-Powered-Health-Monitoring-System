document.getElementById('healthForm').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent form from reloading the page

    const heartRate = document.getElementById('heartRate').value;
    const temperature = document.getElementById('temperature').value;
    const oxygenLevel = document.getElementById('oxygenLevel').value;

    fetch('http://127.0.0.1:5000/api/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            heart_rate: parseFloat(heartRate),
            temperature: parseFloat(temperature),
            oxygen_level: parseFloat(oxygenLevel)
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = 'Health Status: ' + data.result;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error occurred. Check console.';
    });
});
