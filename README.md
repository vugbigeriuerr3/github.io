<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Homepage</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4; /* Grey background */
        }
        /* This will cover the top banner and doctype with the same grey color */
        .cover {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100px; /* Adjusted height to fully cover the <!DOCTYPE html> */
            background-color: #f4f4f4; /* Same grey as the body background */
            z-index: 9999;
        }
        .header {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 15px 0;
            position: relative;
            z-index: 1; /* Ensure header is above the cover */
        }
        .header h1 {
            margin: 0;
        }
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 80vh;
        }
        .box {
            background-color: #000;
            color: #fff;
            padding: 20px;
            margin: 10px;
            width: 200px;
            text-align: center;
            text-decoration: none;
            font-size: 18px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: background-color 0.3s, box-shadow 0.3s;
        }
        .box:hover {
            background-color: #555;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        }
    </style>
</head>
<body>
    <!-- Covering element to hide unwanted elements -->
    <div class="cover"></div>
    
    <div class="header">
        <h1>HTML to Java</h1>
    </div>
    <div class="container">
        <a href="https://vugbigeriuerr3.github.io/github.io/random%20number%20guesser.html" class="box">Number Guesser</a>
        <a href="https://vugbigeriuerr3.github.io/github.io/lotto .html" class="box">Lotto Number Generator</a>
    </div>
</body>
</html>
