const counter = document.querySelector(".counter-number");

async function updateCounter() {
    try {
        let response = await fetch("https://6ol75zpfqjqeondxwoe4omeghe0htkee.lambda-url.us-east-2.on.aws/");
        let data = await response.json();
        counter.innerHTML = `Views: ${data.views}`;
    } catch (error) {
        console.error('Error updating counter:', error);
        counter.innerHTML = 'Couldn\'t read views';
    }
}

updateCounter();
