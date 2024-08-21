<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Main Menu and Number Guessing Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .container {
            text-align: center;
            border: 1px solid #ccc;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
        }
        .hidden {
            display: none;
        }
        .status {
            margin-top: 10px;
            font-weight: bold;
        }
        .status.close {
            color: green;
        }
        .status.far {
            color: red;
        }
        .status.invalid {
            color: orange;
        }
    </style>
</head>
<body>
    <div class="container" id="mainMenu">
        <h1>Main Menu</h1>
        <label for="gameSelect">Select Game:</label>
        <select id="gameSelect">
            <option value="NumberGuessingGame">Number Guessing Game</option>
        </select>
        <br><br>
        <label for="nameSelect">Select Your Name:</label>
        <select id="nameSelect" disabled>
            <option value="Zoe">Zoe</option>
            <option value="Rafferty">Rafferty</option>
            <option value="Carl">Carl</option>
            <option value="Woody">Woody</option>
            <option value="othermember">othermember</option>
        </select>
        <br><br>
        <button id="applyButton">Apply</button>
        <button id="loadButton" class="hidden">Load</button>
        <button id="changeUserButton" class="hidden">Change User</button>
    </div>

    <div class="container hidden" id="gameContainer">
        <h1>Number Guessing Game</h1>
        <p>Guess a number between 1 and 100:</p>
        <input type="number" id="guessField" min="1" max="100">
        <br><br>
        <button id="redoButton" class="hidden">Redo It</button>
        <button id="swapUserButton">Swap User</button>
        <p id="statusLabel" class="status">A new number has been selected. Make your guess!</p>
    </div>

    <script>
        let targetNumber;

        document.getElementById('applyButton').addEventListener('click', () => {
            document.getElementById('nameSelect').disabled = false;
            document.getElementById('loadButton').classList.remove('hidden');
            document.getElementById('changeUserButton').classList.remove('hidden');
        });

        document.getElementById('loadButton').addEventListener('click', () => {
            const selectedName = document.getElementById('nameSelect').value;
            if (confirm('Do you want to load in?')) {
                alert(`Welcome, ${selectedName}!`);
                document.getElementById('mainMenu').classList.add('hidden');
                document.getElementById('gameContainer').classList.remove('hidden');
                generateNewNumber();
            }
        });

        document.getElementById('changeUserButton').addEventListener('click', () => {
            document.getElementById('gameContainer').classList.add('hidden');
            document.getElementById('mainMenu').classList.remove('hidden');
        });

        document.getElementById('redoButton').addEventListener('click', generateNewNumber);

        document.getElementById('guessField').addEventListener('input', evaluateGuess);

        document.getElementById('swapUserButton').addEventListener('click', () => {
            document.getElementById('gameContainer').classList.add('hidden');
            document.getElementById('mainMenu').classList.remove('hidden');
        });

        function generateNewNumber() {
            targetNumber = Math.floor(Math.random() * 100) + 1;
            document.getElementById('statusLabel').textContent = 'A new number has been selected. Make your guess!';
            document.getElementById('guessField').value = '';
            document.getElementById('redoButton').classList.add('hidden');
            document.getElementById('statusLabel').className = 'status';
        }

        function evaluateGuess() {
            const guessField = document.getElementById('guessField');
            const guessText = guessField.value;
            const statusLabel = document.getElementById('statusLabel');

            if (guessText === '') {
                statusLabel.textContent = 'Please enter a number.';
                statusLabel.className = 'status invalid';
                return;
            }

            const guess = parseInt(guessText, 10);
            if (isNaN(guess) || guess < 1 || guess > 100) {
                statusLabel.textContent = 'Invalid input. Please enter a number between 1 and 100.';
                statusLabel.className = 'status invalid';
                return;
            }

            if (guess === targetNumber) {
                statusLabel.textContent = 'You got it!';
                statusLabel.className = 'status close';
                document.getElementById('redoButton').classList.remove('hidden');
            } else if (Math.abs(targetNumber - guess) <= 10) {
                statusLabel.textContent = 'Close';
                statusLabel.className = 'status close';
            } else {
                statusLabel.textContent = 'Far';
                statusLabel.className = 'status far';
            }
        }
    </script>
</body>
</html>
