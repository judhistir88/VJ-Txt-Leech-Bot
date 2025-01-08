import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <center>
        <div class="header">
            <h1>All Set 👍✅!</h1>
            <p class="subheading">Made with 💕 in India</p>
        </div>
        <div class="copilot-hero">
            <canvas id="copilot-canvas"></canvas>
            <div class="hero-content">
                <h2>GitHub Copilot</h2>
                <p>Your AI pair programmer, always ready to help.</p>
            </div>
        </div>
    </center>
    <style>
        body {
            background: linear-gradient(to bottom, #6a11cb, #2575fc);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: 'Arial', sans-serif;
            color: white;
        }
        .header {
            text-align: center;
            animation: fadeIn 3s ease-out;
        }
        h1 {
            font-size: 4em;
            font-weight: bold;
            animation: slideIn 2s ease-out;
        }
        .subheading {
            font-size: 1.5em;
            margin-top: 10px;
            font-style: italic;
            color: #ffeb3b;
            animation: fadeInUp 2s ease-out;
        }
        .copilot-hero {
            position: relative;
            width: 100%;
            max-width: 800px;
            margin-top: 50px;
        }
        #copilot-canvas {
            width: 100%;
            height: 300px;
            background: radial-gradient(circle, #3b3b98, #1e1e50);
            border-radius: 15px;
        }
        .hero-content {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            color: white;
        }
        .hero-content h2 {
            font-size: 2.5em;
            margin: 0;
        }
        .hero-content p {
            font-size: 1.2em;
            margin-top: 10px;
        }

        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }

        @keyframes slideIn {
            0% { transform: translateY(-50px); opacity: 0; }
            100% { transform: translateY(0); opacity: 1; }
        }

        @keyframes fadeInUp {
            0% { transform: translateY(50px); opacity: 0; }
            100% { transform: translateY(0); opacity: 1; }
        }
    </style>
    <script>
        // Initialize canvas animation for the Copilot hero
        const canvas = document.getElementById('copilot-canvas');
        const ctx = canvas.getContext('2d');
        const particles = [];
        const particleCount = 100;

        canvas.width = canvas.clientWidth;
        canvas.height = canvas.clientHeight;

        // Particle Class
        class Particle {
            constructor(x, y) {
                this.x = x;
                this.y = y;
                this.vx = (Math.random() - 0.5) * 2;
                this.vy = (Math.random() - 0.5) * 2;
                this.radius = Math.random() * 3 + 1;
            }
            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
                ctx.fill();
            }
            update() {
                this.x += this.vx;
                this.y += this.vy;

                if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
                if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
            }
        }

        // Create particles
        for (let i = 0; i < particleCount; i++) {
            particles.push(new Particle(Math.random() * canvas.width, Math.random() * canvas.height));
        }

        // Animation loop
        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            particles.forEach(particle => {
                particle.update();
                particle.draw();
            });
            requestAnimationFrame(animate);
        }

        animate();
    </script>
    <footer>
        <p>Made with 💕 in India | <a href="#">Visit us</a></p>
    </footer>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
