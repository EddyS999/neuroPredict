//Ce fichier va permettre d'ajouter chartsJS
function genererGraph(mois1, mois2, mois3, mois4) {

    const ctx = document.getElementById('myChart');
    const labels = ['Mois 1', 'Mois 2', 'Mois 3', 'Mois 4'];

    const data = {
        labels: labels,
        datasets: [
            {
                label: 'évolution score alsfrs',
                data: [mois1, mois2, mois3, mois4],
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
            }
        ]
    };

    new Chart(ctx, {
        type: 'line',
        data: data,
    })

}