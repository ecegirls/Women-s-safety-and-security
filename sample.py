<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Women's Safety & Support</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color:rgb(163, 163, 193);
            color: #333;
            margin: 0;
            padding: 0;
        }
        header {
            background-color:rgb(35, 28, 90);
            color: green;
            padding: 10px 20px;
            text-align: center;
        }
        h1 {
            margin: 0;
        }
        .container {
            padding: 20px;
        }
        .button {
            background-color:rgb(78, 54, 65);
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            font-size: 16px;
            margin: 10px 0;
        }
        .button:hover {
            background-color:rgb(142, 72, 72);
        }
        .section {
            margin-bottom: 20px;
        }
        .important {
            color: #e84393;
        }
        .emergency-btn {
            background-color: #ff7675;
            font-weight: bold;
            font-size: 18px;
        }
        .emergency-btn:hover {
            background-color: #d63031;
        }
    </style>
</head>
<body>

<header>
    <h1>Women's Safety & Support</h1>
    <p>Providing help and resources for women facing abuse</p>
</header>

<div class="container">

    <!-- Emergency Button -->
    <div class="section">
        <a href="#" class="button emergency-btn" onclick="alert('Emergency services contacted')">
            Emergency Help
        </a>
        <p>Quick access to emergency services in case of immediate danger.</p>
    </div>

    <!-- Location-based Resources -->
    <div class="section">
        <h2>Find Nearby Support</h2>
        <p>Click below to get resources near you:</p>
        <button class="button" onclick="alert('Fetching location-based resources')">
            Find Local Lawyers & Shelters
        </button>
    </div>

    <!-- Lawyer Assistance -->
    <div class="section">
        <h2>Legal Assistance</h2>
        <p>Find trusted lawyers specializing in domestic and online abuse:</p>
        <button class="button" onclick="alert('Showing trusted lawyers')">
            Find Lawyers
        </button>
    </div>

    <!-- Upload Proof Section -->
    <div class="section">
        <h2>Add Proof (Optional)</h2>
        <p>Upload screenshots, texts, or any other evidence securely.</p>
        <button class="button" onclick="alert('Secure file upload interface')">
            Upload Evidence
        </button>
    </div>

    <!-- Cyber Cell Contact -->
    <div class="section">
        <h2>Contact Cyber Cell</h2>
        <p>If the abuse is online, connect with the Cyber Crime Cell:</p>
        <button class="button" onclick="alert('Redirecting to Cyber Cell contact page')">
            Contact Cyber Cell
        </button>
    </div>

    <!-- Privacy Considerations -->
    <div class="section important">
        <h2>Privacy & Safety</h2>
        <p>Your privacy is our top priority. No personal information will be stored or shared without your consent.</p>
        <p>You can safely exit this page at any time by clicking the button below:</p>
        <button class="button" onclick="window.location.href='about:blank';">
            Exit Quickly
        </button>
    </div>

</div>

</body>
</html>
