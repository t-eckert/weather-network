export async function get() {
    let locations = {}

    const response = await fetch("http://localhost:5000", {
        mode: "no-cors",
        headers: {
            "Content-Type": "application/json"
        },
    })

    if (response.ok) {
        const data = await response.json()
        locations = data
    }

    return {
        status: 200,
        body: {
            locations
        }
    }
}