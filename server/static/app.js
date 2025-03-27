async function getData() {
	el = document.querySelector('#data');
	const url = "/data";
	try {
		const response = await fetch(url);
		if (!response.ok) {
			throw new Error(`Response status: ${response.status}`);
		}

		const json = await response.json();
		const str = JSON.stringify(json, null, 2);
		// console.log(str);
		el.innerHTML = str;
		// el.textContent = str;
	} catch (error) {
		console.error(error.message);
	}
}

int = setInterval(getData, 1000);
window.addEventListener('beforeunload', () => clearInterval(int));