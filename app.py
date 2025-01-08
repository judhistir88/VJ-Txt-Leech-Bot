import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <center>
    <div class="header">
        <h1></h1>
        <p class="subheading"></p>
    </div>
    <div class="copilot-hero">
        <canvas id="copilot-canvas"></canvas>
        <div class="hero-content">
            <h2>All Set 👍✅!</h2>
            <p>✅✅✅✅✅🟨🟧🟧🟧🟧.</p>
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
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r148/three.min.js"></script>
<script>
    // GitHub Copilot Animated Avatar using Three.js

    const canvas = document.getElementById('copilot-canvas');
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, canvas.clientWidth / canvas.clientHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ canvas: canvas });
    renderer.setSize(canvas.clientWidth, canvas.clientHeight);

    // Add a basic sphere to represent the avatar
    const geometry = new THREE.SphereGeometry(1, 32, 32);
    const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
    const sphere = new THREE.Mesh(geometry, material);
    scene.add(sphere);

    camera.position.z = 5;

    // Function to resize the canvas and camera
    function onResize() {
        const width = canvas.clientWidth;
        const height = canvas.clientHeight;
        renderer.setSize(width, height);
        camera.aspect = width / height;
        camera.updateProjectionMatrix();
    }

    // Update size when the window is resized
    window.addEventListener('resize', onResize);

    // Animation loop
    function animate() {
        requestAnimationFrame(animate);

        // Rotate the sphere to simulate movement
        sphere.rotation.x += 0.01;
        sphere.rotation.y += 0.01;

        renderer.render(scene, camera);
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
