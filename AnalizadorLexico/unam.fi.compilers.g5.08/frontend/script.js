// Función para alternar entre modo claro y oscuro y guardar la preferencia
function toggleTheme() {
    const body = document.body;
    if (body.classList.contains("dark-mode")) {
        body.classList.remove("dark-mode");
        body.classList.add("light-mode");
        localStorage.setItem("theme", "light-mode");
    } else {
        body.classList.remove("light-mode");
        body.classList.add("dark-mode");
        localStorage.setItem("theme", "dark-mode");
    }
}



// Aplicar el tema guardado al cargar la página
document.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("theme") || "dark-mode";
    document.body.classList.add(savedTheme);
});

// Función para analizar el código ingresado
async function analyzeCode(code = null) {
    if (!code) {
        code = document.getElementById("codeInput").value;
    }

    const outputDiv = document.getElementById("output");
    const loadingDiv = document.getElementById("loading");
    
    outputDiv.innerHTML = "";
    loadingDiv.classList.remove("hidden"); // Mostrar el spinner

    try {
        const response = await fetch("http://localhost:5000/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code })
        });

        const data = await response.json();
        loadingDiv.classList.add("hidden"); // Ocultar el spinner

        if (response.ok) {
            outputDiv.innerHTML = `<h2 class='text-lg font-bold mb-2'>Tokens reconocidos:</h2>`;
            
            Object.entries(data.tokens).forEach(([category, values]) => {
                outputDiv.innerHTML += `
                    <p><strong>${category} (${values.length}):</strong> 
                    ${values.length ? values.join(", ") : "<span class='text-yellow-400'>⚠ No se encontraron tokens.</span>"}
                    </p>`;
            });

            outputDiv.innerHTML += `<p class="mt-2"><strong>Total de tokens:</strong> ${data.total_tokens}</p>`;
        } else {
            outputDiv.innerHTML = `<p class='text-red-500'>Error: ${data.error}</p>`;
        }
    } catch (error) {
        loadingDiv.classList.add("hidden");
        outputDiv.innerHTML = `<p class='text-red-500'>⚠ Error de conexión con el backend.</p>`;
    }
}

// Cargar archivo y mostrar su contenido en el textarea
document.getElementById("fileInput").addEventListener("change", function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById("codeInput").value = e.target.result;
        };
        reader.readAsText(file);
    }
});

// Función para cargar un código de ejemplo
function loadExample() {
    document.getElementById("codeInput").value = 
`def suma(a, b):
    return a + b

print(suma(5, 10))`;
}

particlesJS({
    "particles": {
        "number": {
            "value": 30,
            "density": {
                "enable": true,
                "value_area": 800
            }
        },
        "color": {
            "value": "#ffffff"
        },
        "shape": {
            "type": "image",
            "stroke": {
                "width": 0,
                "color": "#000000"
            },
            "polygon": {
                "nb_sides": 5
            },
            "image": {
                "src": "./images/Solano.jpg",
                "width": 100,
                "height": 100
            }
        },
        "opacity": {
            "value": 0.4088700755207083,
            "random": true,
            "anim": {
                "enable": true,
                "speed": 1,
                "opacity_min": 0,
                "sync": false
            }
        },
        "size": {
            "value": 90,
            "random": true,
            "anim": {
                "enable": false,
                "speed": 0.2,
                "size_min": 0.3,
                "sync": false
            }
        },
        "line_linked": {
            "enable": true,
            "distance": 4.13648243462092,
            "color": "#ffffff",
            "opacity": 0.6493818846505367,
            "width": 1
        },
        "move": {
            "enable": true,
            "speed": 2.3,
            "direction": "none",
            "random": true,
            "straight": false,
            "out_mode": "out",
            "bounce": false,
            "attract": {
                "enable": false,
                "rotateX": 600,
                "rotateY": 600
            }
        }
    },
    "interactivity": {
        "detect_on": "canvas",
        "events": {
            "onhover": {
                "enable": true,
                "mode": "repulse"
            },
            "onclick": {
                "enable": true,
                "mode": "repulse"
            },
            "resize": true
        },
        "modes": {
            "grab": {
                "distance": 400,
                "line_linked": {
                    "opacity": 1
                }
            },
            "bubble": {
                "distance": 250,
                "size": 0,
                "duration": 2,
                "opacity": 0,
                "speed": 3
            },
            "repulse": {
                "distance": 200,
                "duration": 0.2
            },
            "push": {
                "particles_nb": 4
            },
            "remove": {
                "particles_nb": 2
            }
        }
    },
    "retina_detect": true
}
);