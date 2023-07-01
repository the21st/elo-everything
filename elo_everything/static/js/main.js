```javascript
document.addEventListener('DOMContentLoaded', function() {
    loadConcepts();
    document.getElementById('vote-button').addEventListener('click', vote);
});

function loadConcepts() {
    fetch('/get_concepts')
    .then(response => response.json())
    .then(data => {
        document.getElementById('concept1').textContent = data.concept1.name;
        document.getElementById('concept1-img').src = data.concept1.image;
        document.getElementById('concept2').textContent = data.concept2.name;
        document.getElementById('concept2-img').src = data.concept2.image;
    });
}

function vote() {
    const selectedConcept = document.querySelector('input[name="concept"]:checked').value;
    fetch('/vote', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ concept: selectedConcept })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            loadConcepts();
            updateLeaderboard();
        } else {
            alert('Something went wrong. Please try again.');
        }
    });
}

function updateLeaderboard() {
    fetch('/get_leaderboard')
    .then(response => response.json())
    .then(data => {
        const leaderboardTable = document.getElementById('leaderboard-table');
        leaderboardTable.innerHTML = '';
        data.forEach(concept => {
            const row = document.createElement('tr');
            const nameCell = document.createElement('td');
            nameCell.textContent = concept.name;
            const scoreCell = document.createElement('td');
            scoreCell.textContent = concept.score;
            row.appendChild(nameCell);
            row.appendChild(scoreCell);
            leaderboardTable.appendChild(row);
        });
    });
}
```