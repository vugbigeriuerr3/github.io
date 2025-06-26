<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Projects Hub</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f3f4f6;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
            box-sizing: border-box;
            background-image: url('https://placehold.co/1920x1080/e5e7eb/e5e7eb?text=');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        header.site-header {
            display: none;
        }
        .modal {
            max-height: 90vh;
            overflow-y: auto;
            -webkit-overflow-scrolling: touch;
        }
    </style>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen p-4">
    <div class="fixed top-4 right-4 z-50 flex items-center space-x-2 bg-white rounded-full py-2 px-4 shadow-md">
        <span id="user-name-display" class="text-lg font-medium text-blue-600">Guest</span>
        <button id="edit-user-name-btn" class="text-gray-500 hover:text-gray-700 transition-colors duration-200 focus:outline-none">
            <i class="fas fa-pencil-alt text-base"></i>
        </button>
    </div>

    <div class="w-full max-w-lg bg-white shadow-lg rounded-2xl p-8 text-center">
        <h1 class="text-4xl font-bold text-gray-800 mb-6">My Projects Hub</h1>
        <p class="text-lg text-gray-600 mb-8">Explore my various applications.</p>
        
        <div class="space-y-4">
            <a href="https://vugbigeriuerr3.github.io/github.io/random%20number%20guesser.html" 
               class="inline-block w-full px-8 py-4 bg-blue-600 text-white font-bold text-xl rounded-xl hover:bg-blue-700 transition-all duration-300 shadow-lg transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-75">
                Random Number Guesser
            </a>

            <a href="https://vugbigeriuerr3.github.io/github.io/lotto%20.html" 
               class="inline-block w-full px-8 py-4 bg-blue-600 text-white font-bold text-xl rounded-xl hover:bg-blue-700 transition-all duration-300 shadow-lg transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-75">
                Lotto Number Generator
            </a>

            <a href="https://vugbigeriuerr3.github.io/github.io/Counter" 
               class="inline-block w-full px-8 py-4 bg-blue-600 text-white font-bold text-xl rounded-xl hover:bg-blue-700 transition-all duration-300 shadow-lg transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-75">
                Dynamic Counter Application
            </a>
        </div>
    </div>

    <div id="name-setup-modal" class="modal fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50 hidden">
        <div class="bg-white rounded-2xl shadow-xl p-8 w-full max-w-md transform transition-all duration-300 scale-100 opacity-100">
            <h2 class="text-3xl font-bold text-gray-800 mb-6 text-center">What's your name?</h2>
            <div class="mb-6">
                <label for="modal-user-name-input" class="block text-gray-700 text-sm font-semibold mb-2">Your Name:</label>
                <input type="text" id="modal-user-name-input" placeholder="Enter your name" class="shadow-sm appearance-none border rounded-xl w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-transparent transition-all duration-200">
            </div>
            <button id="save-name-btn" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-75 transition-all duration-300 shadow-lg">Save Name</button>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const userNameDisplay = document.getElementById('user-name-display');
            const editUserNameBtn = document.getElementById('edit-user-name-btn');
            const nameSetupModal = document.getElementById('name-setup-modal');
            const modalUserNameInput = document.getElementById('modal-user-name-input');
            const saveNameBtn = document.getElementById('save-name-btn');

            let appState = {
                userName: '',
                websiteTitle: '',
                counters: []
            };

            const setCookie = (name, value, days) => {
                let expires = '';
                if (days) {
                    const date = new Date();
                    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
                    expires = '; expires=' + date.toUTCString();
                }
                document.cookie = name + '=' + (value || '') + expires + '; path=/; SameSite=Lax';
            };

            const getCookie = (name) => {
                const nameEQ = name + '=';
                const ca = document.cookie.split(';');
                for (let i = 0; i < ca.length; i++) {
                    let c = ca[i];
                    while (c.charAt(0) === ' ') c = c.substring(1, c.length);
                    if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
                }
                return null;
            };

            const deleteCookie = (name) => {
                document.cookie = name + '=; Max-Age=-99999999; path=/; SameSite=Lax';
            };

            const renderUserName = () => {
                userNameDisplay.textContent = appState.userName || 'Guest';
                if (appState.userName) {
                    nameSetupModal.classList.add('hidden');
                } else {
                    nameSetupModal.classList.remove('hidden');
                }
            };

            saveNameBtn.addEventListener('click', () => {
                const newName = modalUserNameInput.value.trim();
                if (newName) {
                    appState.userName = newName;
                    setCookie('appState', JSON.stringify(appState), 365);
                    renderUserName();
                } else {
                    const existingMessage = saveNameBtn.parentElement.querySelector('.temp-error-message');
                    if (existingMessage) existingMessage.remove();

                    let messageElement = document.createElement('p');
                    messageElement.textContent = 'Please enter a name.';
                    messageElement.className = 'text-red-500 text-sm mt-2 text-center temp-error-message';
                    saveNameBtn.parentElement.insertBefore(messageElement, saveNameBtn);
                    setTimeout(() => {
                        messageElement.remove();
                    }, 2000);
                }
            });

            editUserNameBtn.addEventListener('click', () => {
                modalUserNameInput.value = appState.userName;
                nameSetupModal.classList.remove('hidden');
                const existingMessage = saveNameBtn.parentElement.querySelector('.temp-error-message');
                if (existingMessage) existingMessage.remove();
            });

            const init = () => {
                const loadedCookieData = getCookie('appState');
                if (loadedCookieData) {
                    try {
                        const parsedState = JSON.parse(loadedCookieData);
                        appState = { ...appState, ...parsedState };
                        if (typeof appState.userName === 'undefined') {
                            appState.userName = '';
                        }
                    } catch (e) {
                        console.error('Error parsing appState cookie on homepage:', e);
                        deleteCookie('appState');
                    }
                }
                renderUserName();
            };

            init();
        });
    </script>
</body>
</html>
