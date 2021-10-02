console.log("This is main.js");

window.onload = () => {
    window.fetch("public/scaler.pkl")
        .then(async function (res) {
            window.scaler = await res.arrayBuffer();
        })
        .then(main());
};


async function main() {
    let pyodide = await loadPyodide({
        indexURL: "https://cdn.jsdelivr.net/pyodide/v0.18.1/full/",
    });

    let output = document.getElementById("output")
    output.value = "loading\n"

    await pyodide.loadPackage("numpy");
    await pyodide.loadPackage("scikit-learn");

    console.log("Pyodide is ready.");
    output.value += "Pyodide is ready\n";

    await pyodide.runPython(`
    import js
    import pickle
    import pyodide
    import numpy as np 

    py_buffer = js.scaler.to_py()

    scaler = pickle.loads(py_buffer)
    print(scaler.transform(np.array([[1, 2, 3, 4, 5]]))),

    `);
}

