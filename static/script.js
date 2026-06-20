async function analyzePalm() {

    const file =
        document.getElementById(
            "imageInput"
        ).files[0];

    if (!file) {
        alert("Choose image");
        return;
    }

    const formData =
        new FormData();

    formData.append(
        "image",
        file
    );

    const response =
        await fetch(
            "/predict",
            {
                method: "POST",
                body: formData
            }
        );

    const data =
        await response.json();

    let html = "";

    html += `
    <div class="card">
        <h2>Palm Type</h2>
        <p>${data.palm_type}</p>
    </div>
    `;

    html += `
    <div class="card">
        <h2>Summary</h2>
        <p>${data.summary}</p>
    </div>
    `;

    html += `
    <div class="card">
        <h2>Scores</h2>
    `;

    for(let key in data.scores){

        html += `
        <p>
            ${key} :
            ${data.scores[key].toFixed(1)}
        </p>
        `;
    }

    html += "</div>";

    html += `
    <div class="card">
        <h2>Analysis</h2>
        <ul>
    `;

    data.analysis.analysis.forEach(item => {        html += `<li>${item}</li>`;
    });

    html += `
        </ul>
    </div>
    `;

    html += `
    <div class="card">
        <h2>Careers</h2>
        <ul>
    `;

    data.careers.forEach(item=>{
        html += `<li>${item}</li>`;
    });

    html += `
        </ul>
    </div>
    `;

    document.getElementById(
        "result"
    ).innerHTML = html;
}
