<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Projects Hub</title>
    <script src="https://cdn.tailwindcss.com"></script>
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
            /* Background image styles */
            background-image: url('https://placehold.co/1920x1080/e5e7eb/e5e7eb?text='); /* Light gray placeholder image */
            background-size: cover;
            background-position: center;
            background-attachment: fixed; /* Ensures the background covers the whole page even with scrolling */
        }
        header.site-header {
            display: none;
        }
    </style>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen p-4">
    <div class="w-full max-w-lg bg-white shadow-lg rounded-2xl p-8 text-center">
        <h1 class="text-4xl font-bold text-gray-800 mb-6">My Projects Hub</h1>
        <p class="text-lg text-gray-600 mb-8">Explore my various applications.</p>
        
        <div class="space-y-4">
            <a href="#" 
               class="inline-block w-full px-8 py-4 bg-blue-600 text-white font-bold text-xl rounded-xl hover:bg-blue-700 transition-all duration-300 shadow-lg transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-75">
                Number Guesser (Example)
            </a>

            <a href="#" 
               class="inline-block w-full px-8 py-4 bg-blue-600 text-white font-bold text-xl rounded-xl hover:bg-blue-700 transition-all duration-300 shadow-lg transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-75">
                Lotto Number Generator (Example)
            </a>

            <a href="https://vugbigeriuerr3.github.io/github.io/Counter" 
               class="inline-block w-full px-8 py-4 bg-blue-600 text-white font-bold text-xl rounded-xl hover:bg-blue-700 transition-all duration-300 shadow-lg transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-75">
                Go to Dynamic Counter Application
            </a>
        </div>
    </div>
</body>
</html>
