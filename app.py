<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Animated Avatar</title>
    <style>
        /* Keyframe animation for smooth movement */
        @keyframes bounce {
            0% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0); }
        }

        /* Avatar container */
        .avatar {
            width: 50px;
            height: 50px;
            background-color: #0d6efd;
            border-radius: 50%;
            animation: bounce 1s infinite;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: Arial, sans-serif;
            color: white;
            font-size: 20px;
        }
    </style>
</head>
<body>
    <!-- Avatar Element -->
    <div class="avatar">
        AI
    </div>
</body>
</html>
