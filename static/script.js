async function askAgent() {

    const input = document.getElementById("message");
    const result = document.getElementById("result");
    const loading = document.getElementById("loading");

    const message = input.value.trim();

    if (!message) {
        result.innerText = "Please enter a weather question.";
        return;
    }

    loading.style.display = "flex";

    result.innerText = "Analyzing weather conditions...";

    try {

        const response = await fetch("/ask", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        const data = await response.json();


        if (!response.ok) {

            result.innerText =
                "❌ " + (data.error || "Something went wrong.");

            return;
        }


        /* WEATHER DATA */

        if (data.weather) {

            const weather = data.weather;

            document.getElementById("city").innerText =
                weather.city + ", " + weather.country;

            document.getElementById("temperature").innerText =
                weather.temperature;

            document.getElementById("description").innerText =
                weather.description;

            document.getElementById("humidity").innerText =
                weather.humidity + "%";

            document.getElementById("feelsLike").innerText =
                weather.feels_like + "°C";

            document.getElementById("wind").innerText =
                weather.wind + " m/s";

            document.getElementById("rain").innerText =
                weather.rain + " mm";

            setWeatherIcon(weather.main);
        }


        /* AI RESPONSE */

        result.innerText = data.answer;


    } catch (error) {

        console.error(error);

        result.innerText =
            "❌ Unable to connect to the AI agent.\n\n" +
            "Make sure Flask and Ollama are running.";

    } finally {

        loading.style.display = "none";

    }

}


/* WEATHER ICON */

function setWeatherIcon(condition) {

    const icon = document.getElementById("weatherIcon");

    const value = condition.toLowerCase();

    if (value.includes("rain")) {

        icon.innerText = "🌧️";

    } else if (value.includes("cloud")) {

        icon.innerText = "☁️";

    } else if (value.includes("clear")) {

        icon.innerText = "☀️";

    } else if (value.includes("snow")) {

        icon.innerText = "❄️";

    } else if (value.includes("thunder")) {

        icon.innerText = "⛈️";

    } else {

        icon.innerText = "🌤️";

    }

}


/* QUICK QUESTIONS */

function quickAsk(question) {

    document.getElementById("message").value = question;

    askAgent();

}


/* ENTER KEY */

document
    .getElementById("message")
    .addEventListener("keydown", function(event) {

        if (event.key === "Enter") {
            askAgent();
        }

    });sses