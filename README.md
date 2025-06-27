<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Projects Hub</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        body {
            font-family: 'Inter', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
            box-sizing: border-box;
            transition: background-color 0.3s ease;
        }

        .main-card {
            transition: background-color 0.3s ease, color 0.3s ease;
            position: relative;
            z-index: 20; /* Ensure main card is above the overlay */
        }

        header.site-header, .site-header {
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
            overflow: hidden !important;
        }

        #github-pages-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            /* background-color will be set by JS */
            z-index: 10; /* Lower than fixed elements (z-50) and main-card (z-20) */
            pointer-events: none; /* Allows clicks to pass through to elements beneath */
            display: block; /* Always visible to cover content */
            transition: background-color 0.3s ease; /* Smooth transition for overlay color */
        }

        .modal {
            max-height: 90vh;
            overflow-y: auto;
            -webkit-overflow-scrolling: touch;
            /* New: Ensure modals are on top of other content */
            z-index: 60; /* Set a higher z-index for modals */
        }

        /* Ensure fixed elements are on top of the overlay but below modals */
        .fixed {
            z-index: 50;
            position: fixed; /* Explicitly fixed position as Tailwind fixed applies it */
        }
    </style>
</head>
<body class="flex items-center justify-center min-h-screen p-4">
    <div id="github-pages-overlay"></div>

    <div class="fixed top-4 right-4 z-50 flex items-center space-x-2 bg-white rounded-full py-2 px-4 shadow-md transition-colors duration-300">
        <span id="user-name-display" class="text-lg font-medium text-blue-600">Guest</span>
        <button id="edit-name-btn" class="text-gray-500 hover:text-gray-700 transition-colors duration-200 focus:outline-none">
            <i class="fas fa-pencil-alt text-base"></i>
        </button>
    </div>

    <div class="fixed top-4 left-4 z-50">
        <button id="configure-display-btn" class="px-4 py-2 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition-colors duration-300 shadow-md focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-opacity-75 text-sm md:text-base">
            <i class="fas fa-palette mr-2"></i>Configure Display
        </button>
    </div>

    <div id="main-content-card" class="w-full max-w-lg shadow-lg rounded-2xl p-8 text-center main-card">
        <h1 class="text-4xl font-bold mb-6">The Projects Hub</h1>
        <p class="text-lg mb-8">Explore my various applications.</p>
        
        <div class="space-y-4">
            <a href="https://vugbigeriuerr3.github.io/github.io/random%20number%20guesser" 
               class="inline-block w-full px-8 py-4 bg-blue-600 text-white font-bold text-xl rounded-xl hover:bg-blue-700 transition-all duration-300 shadow-lg transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-75">
                Number Guesser
            </a>

            <a href="https://vugbigeriuerr3.github.io/github.io/lotto" 
               class="inline-block w-full px-8 py-4 bg-blue-600 text-white font-bold text-xl rounded-xl hover:bg-blue-700 transition-all duration-300 shadow-lg transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-75">
                Lotto
            </a>

            <a href="https://vugbigeriuerr3.github.io/github.io/Update_log" 
               class="inline-block w-full px-8 py-4 bg-blue-600 text-white font-bold text-xl rounded-xl hover:bg-blue-700 transition-all duration-300 shadow-lg transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-75">
                Update Log
            </a>

            <a href="https://vugbigeriuerr3.github.io/github.io/About.html"
               class="inline-block w-full px-8 py-4 bg-blue-600 text-white font-bold text-xl rounded-xl hover:bg-blue-700 transition-all duration-300 shadow-lg transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-75">
                About.
            </a>
        </div>
    </div>

    <div id="name-edit-modal" class="modal fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 hidden">
        <div class="bg-white rounded-2xl shadow-xl p-8 w-full max-w-md transform transition-all duration-300 scale-100 opacity-100">
            <h2 class="text-3xl font-bold text-gray-800 mb-6 text-center">Change Your Name</h2>
            <div class="mb-6">
                <label for="name-edit-user-input" class="block text-gray-700 text-sm font-semibold mb-2">Your Name:</label>
                <input type="text" id="name-edit-user-input" placeholder="Enter your name" 
                        class="shadow-sm appearance-none border rounded-xl w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-blue-400 focus:border-transparent transition-all duration-200">
            </div>
            <button id="save-name-only-btn" 
                    class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-75 transition-all duration-300 shadow-lg">Save Name</button>
        </div>
    </div>

    <div id="display-settings-modal" class="modal fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 hidden">
        <div class="bg-white rounded-2xl shadow-xl p-8 w-full max-w-md transform transition-all duration-300 scale-100 opacity-100">
            <h2 class="text-3xl font-bold text-gray-800 mb-6 text-center">Display Settings</h2>
            
            <div class="mb-6">
                <label class="block text-gray-700 text-sm font-semibold mb-2">Theme:</label>
                <div class="flex flex-col space-y-2">
                    <label class="inline-flex items-center">
                        <input type="radio" name="theme" value="light" class="form-radio text-blue-600" checked>
                        <span class="ml-2 text-gray-700">Light Mode</span>
                    </label>
                    <label class="inline-flex items-center">
                        <input type="radio" name="theme" value="dark" class="form-radio text-blue-600">
                        <span class="ml-2 text-gray-700">Dark Mode</span>
                    </label>
                    <label class="inline-flex items-center">
                        <input type="radio" name="theme" value="custom" class="form-radio text-blue-600">
                        <span class="ml-2 text-gray-700">Custom Colors</span>
                    </label>
                </div>
            </div>

            <div id="custom-color-inputs" class="space-y-4 mb-6 hidden">
                <div>
                    <label for="custom-body-bg-color" class="block text-gray-700 text-sm font-semibold mb-2">Body Background Color:</label>
                    <input type="color" id="custom-body-bg-color" value="#f3f4f6"
                            class="w-full h-10 border rounded-lg p-1">
                </div>
                <div>
                    <label for="custom-card-bg-color" class="block text-gray-700 text-sm font-semibold mb-2">Card Background Color:</label>
                    <input type="color" id="custom-card-bg-color" value="#ffffff"
                            class="w-full h-10 border rounded-lg p-1">
                </div>
            </div>

            <button id="save-display-settings-btn" 
                    class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-75 transition-all duration-300 shadow-lg">Save Display Settings</button>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const userNameDisplay = document.getElementById('user-name-display');
            const editNameBtn = document.getElementById('edit-name-btn');
            const configureDisplayBtn = document.getElementById('configure-display-btn');
            const mainContentCard = document.getElementById('main-content-card');
            const githubPagesOverlay = document.getElementById('github-pages-overlay');

            const nameEditModal = document.getElementById('name-edit-modal');
            const nameEditUserInput = document.getElementById('name-edit-user-input');
            const saveNameOnlyBtn = document.getElementById('save-name-only-btn');

            const displaySettingsModal = document.getElementById('display-settings-modal');
            const themeRadios = document.querySelectorAll('input[name="theme"]');
            const customColorInputsDiv = document.getElementById('custom-color-inputs');
            const customBodyBgColorInput = document.getElementById('custom-body-bg-color');
            const customCardBgColorInput = document.getElementById('custom-card-bg-color');
            const saveDisplaySettingsBtn = document.getElementById('save-display-settings-btn');

            let appState = {
                userName: '',
                displaySettings: {
                    theme: 'light',
                    customBodyBg: '#f3f4f6',
                    customCardBg: '#ffffff'
                },
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

            const applyDisplaySettings = () => {
                const { theme, customBodyBg, customCardBg } = appState.displaySettings;

                // Clear body classes and inline styles first to ensure proper application
                document.body.classList.remove('bg-gray-100', 'dark-mode');
                document.body.style.backgroundColor = '';
                document.body.style.backgroundImage = '';
                
                mainContentCard.classList.remove('bg-white', 'bg-gray-800');
                mainContentCard.style.backgroundColor = '';

                mainContentCard.querySelector('h1').style.color = '';
                mainContentCard.querySelector('p').style.color = '';

                const userNameBox = document.querySelector('.fixed.top-4.right-4');
                userNameBox.classList.remove('bg-white', 'bg-gray-900');
                userNameBox.querySelector('span').style.color = '';
                userNameBox.querySelector('button').style.color = '';

                // Apply theme styles
                if (theme === 'dark') {
                    document.body.classList.add('dark-mode');
                    document.body.style.backgroundImage = 'url("https://placehold.co/1920x1080/2d3748/2d3748?text=")';
                    document.body.style.backgroundColor = '#1a202c';
                    githubPagesOverlay.style.backgroundColor = '#1a202c'; // Overlay matches dark theme
                    
                    mainContentCard.classList.add('bg-gray-800');
                    mainContentCard.querySelector('h1').style.color = '#e2e8f0';
                    mainContentCard.querySelector('p').style.color = '#cbd5e0';

                    userNameBox.classList.add('bg-gray-900');
                    userNameBox.querySelector('span').style.color = '#90cdf4';
                    userNameBox.querySelector('button').style.color = '#a0aec0';

                } else if (theme === 'custom') {
                    document.body.style.backgroundColor = customBodyBg;
                    document.body.style.backgroundImage = 'none';
                    githubPagesOverlay.style.backgroundColor = customBodyBg; // Overlay matches custom body color
                    
                    mainContentCard.style.backgroundColor = customCardBg;
                    
                    const isDark = (color) => {
                        if (!color) return false;
                        const rgb = parseInt(color.replace('#', ''), 16);
                        const r = (rgb >> 16) & 0xff;
                        const g = (rgb >> 8) & 0xff;
                        const b = (rgb >> 0) & 0xff;
                        return (0.2126 * r + 0.7152 * g + 0.0722 * b) < 128;
                    };

                    if (isDark(customBodyBg)) {
                        mainContentCard.querySelector('h1').style.color = '#e2e8f0';
                        mainContentCard.querySelector('p').style.color = '#cbd5e0';
                        userNameBox.classList.add('bg-gray-900');
                        userNameBox.querySelector('span').style.color = '#90cdf4';
                        userNameBox.querySelector('button').style.color = '#a0aec0';
                    } else {
                        mainContentCard.querySelector('h1').style.color = '#1a202c';
                        mainContentCard.querySelector('p').style.color = '#4a5568';
                        userNameBox.classList.add('bg-white');
                        userNameBox.querySelector('span').style.color = '#3182ce';
                        userNameBox.querySelector('button').style.color = '#a0aec0';
                    }
                    if (isDark(customCardBg)) {
                            mainContentCard.querySelector('h1').style.color = '#e2e8f0';
                            mainContentCard.querySelector('p').style.color = '#cbd5e0';
                    } else {
                        mainContentCard.querySelector('h1').style.color = '#1a202c';
                        mainContentCard.querySelector('p').style.color = '#4a5568';
                    }

                } else { // 'light' theme (default)
                    document.body.classList.add('bg-gray-100');
                    document.body.style.backgroundImage = 'url("https://placehold.co/1920x1080/e5e7eb/e5e7eb?text=")';
                    githubPagesOverlay.style.backgroundColor = '#f3f4f6'; // Overlay matches light theme
                    mainContentCard.classList.add('bg-white');
                    userNameBox.classList.add('bg-white');
                }
            };


            const renderUserName = () => {
                userNameDisplay.textContent = appState.userName || 'Guest';
                if (!appState.userName && !sessionStorage.getItem('nameEditModalShown')) {
                    nameEditModal.classList.remove('hidden');
                    sessionStorage.setItem('nameEditModalShown', 'true');
                } else if (appState.userName) {
                    nameEditModal.classList.add('hidden');
                }
            };

            saveNameOnlyBtn.addEventListener('click', () => {
                const newUserName = nameEditUserInput.value.trim();
                if (newUserName) {
                    const loadedCookieData = getCookie('appState');
                    let currentAppState = {};
                    if (loadedCookieData) {
                        try {
                            currentAppState = JSON.parse(loadedCookieData);
                        } catch (e) {
                            console.error('Error parsing existing appState cookie:', e);
                        }
                    }
                    currentAppState.userName = newUserName; 
                    appState.userName = newUserName; 

                    setCookie('appState', JSON.stringify(currentAppState), 365);
                    renderUserName();
                    nameEditModal.classList.add('hidden');
                } else {
                    let messageElement = saveNameOnlyBtn.parentElement.querySelector('.temp-error-message');
                    if (!messageElement) {
                        messageElement = document.createElement('p');
                        messageElement.className = 'text-red-500 text-sm mt-2 text-center temp-error-message';
                        saveNameOnlyBtn.parentElement.insertBefore(messageElement, saveNameOnlyBtn);
                    }
                    messageElement.textContent = 'Please enter a name.';
                    setTimeout(() => {
                        messageElement.remove();
                    }, 2000);
                }
            });

            editNameBtn.addEventListener('click', () => {
                nameEditUserInput.value = appState.userName;
                nameEditModal.classList.remove('hidden');
                const existingMessage = saveNameOnlyBtn.parentElement.querySelector('.temp-error-message');
                if (existingMessage) existingMessage.remove();
            });

            configureDisplayBtn.addEventListener('click', () => {
                themeRadios.forEach(radio => {
                    radio.checked = (radio.value === appState.displaySettings.theme);
                });

                if (appState.displaySettings.theme === 'custom') {
                    customColorInputsDiv.classList.remove('hidden');
                    customBodyBgColorInput.value = appState.displaySettings.customBodyBg;
                    customCardBgColorInput.value = appState.displaySettings.customCardBg;
                } else {
                    customColorInputsDiv.classList.add('hidden');
                }

                displaySettingsModal.classList.remove('hidden');
            });

            themeRadios.forEach(radio => {
                radio.addEventListener('change', () => {
                    if (radio.value === 'custom') {
                        customColorInputsDiv.classList.remove('hidden');
                    } else {
                        customColorInputsDiv.classList.add('hidden');
                    }
                });
            });

            saveDisplaySettingsBtn.addEventListener('click', () => {
                const selectedTheme = document.querySelector('input[name="theme"]:checked').value;
                const newCustomBodyBg = customBodyBgColorInput.value;
                const newCustomCardBg = customCardBgColorInput.value;

                const loadedCookieData = getCookie('appState');
                let currentAppState = {};
                if (loadedCookieData) {
                    try {
                        currentAppState = JSON.parse(loadedCookieData);
                    } catch (e) {
                        console.error('Error parsing existing appState cookie:', e);
                    }
                }

                currentAppState.displaySettings = {
                    theme: selectedTheme,
                    customBodyBg: newCustomBodyBg,
                    customCardBg: newCustomCardBg
                };
                
                appState.displaySettings = currentAppState.displaySettings;

                setCookie('appState', JSON.stringify(currentAppState), 365);
                applyDisplaySettings();
                displaySettingsModal.classList.add('hidden');
            });

            const init = () => {
                const loadedCookieData = getCookie('appState');
                if (loadedCookieData) {
                    try {
                        const parsedState = JSON.parse(loadedCookieData);
                        appState.userName = parsedState.userName || '';
                        if (parsedState.displaySettings) {
                            appState.displaySettings.theme = parsedState.displaySettings.theme || 'light';
                            appState.displaySettings.customBodyBg = parsedState.displaySettings.customBodyBg || '#f3f4f6';
                            appState.displaySettings.customCardBg = parsedState.displaySettings.customCardBg || '#ffffff';
                        }
                        appState = { ...parsedState, ...appState };
                    } catch (e) {
                        console.error('Error parsing appState cookie on init:', e);
                        deleteCookie('appState');
                    }
                }
                renderUserName();
                applyDisplaySettings();
            };

            init();
        });
    </script>
</body>
</html>
