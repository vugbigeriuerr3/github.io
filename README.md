<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Projects Hub</title>
    <!-- Tailwind CSS CDN for modern styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Import the 'Inter' font for a clean, modern typography */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f3f4f6; /* Light gray background, consistent with counter app */
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh; /* Ensure body takes full viewport height */
            margin: 0;
            padding: 20px; /* Add some padding around the main container */
            box-sizing: border-box; /* Include padding in element's total width and height */
        }
    </style>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen p-4">
    <div class="w-full max-w-lg bg-white shadow-lg rounded-2xl p-8 text-center">
        <h1 class="text-4xl font-bold text-gray-800 mb-6">My Projects Hub</h1>
        <p class="text-lg text-gray-600 mb-8">Explore my various applications.</p>
        
        <div class="space-y-4">
            <!-- Original button 1 (Example, assuming this was "Number Guesser") -->
            <a href="#" 
               class="inline-block w-full px-8 py-4 bg-gray-800 text-white font-bold text-xl rounded-xl hover:bg-gray-900 transition-all duration-300 shadow-lg transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-gray-700 focus:ring-opacity-75">
                Number Guesser (Example)
            </a>

            <!-- Original button 2 (Example, assuming this was "Lotto Number Generator") -->
            <a href="#" 
               class="inline-block w-full px-8 py-4 bg-gray-800 text-white font-bold text-xl rounded-xl hover:bg-gray-900 transition-all duration-300 shadow-lg transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-gray-700 focus:ring-opacity-75">
                Lotto Number Generator (Example)
            </a>

            <!-- New button for Dynamic Counter Application -->
            <a href="https://vugbigeriuerr3.github.io/github.io/Counter" 
               class="inline-block w-full px-8 py-4 bg-blue-600 text-white font-bold text-xl rounded-xl hover:bg-blue-700 transition-all duration-300 shadow-lg transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-75">
                Go to Dynamic Counter Application
            </a>
        </div>
    </div>
</body>
</html>
