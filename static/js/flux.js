    const dialogeE = document.querySelector(".dialogeE");
    const dialogeD = document.querySelector(".dialogeD");
    const dialogeS = document.querySelector(".dialogeS");
    const dialogeupdE = document.querySelector(".dialogeupdE");
    const dialogeupdD = document.querySelector(".dialogeupdD");
    const dialogeviewD = document.querySelector(".dialogeviewD");
    const dialogeviewE = document.querySelector(".dialogeviewE");
    const OpenDialogeE = document.querySelector("#btn-dialogeE");
    const OpenDialogeD = document.querySelector("#btn-dialogeD");
    const OpenDialogeS = document.querySelector("#btn-dialogeS");
    const OpenDialogeupdE = document.querySelector("#btn-upddialogeE");
    const OpenDialogeupdD = document.querySelector("#btn-upddialogeD");
    const OpenDialogeviewD = document.querySelector("#btn-dialogeviewD");
    const OpenDialogeviewE = document.querySelector("#btn-dialogeviewE");
    const closedialogE = document.querySelector(".dialogcloseE button");
    const closedialogS = document.querySelector(".dialogcloseS button");
    const closedialogupdD = document.querySelector(".dialogcloseupdD button");
    const closedialogupdE = document.querySelector(".dialogcloseupdE button");
    const closedialogD = document.querySelector(".dialogcloseD button");
    const closedialogviewE = document.querySelector(".dialogcloseviewE button");
    const closedialogviewD = document.querySelector(".dialogcloseviewD button");
    OpenDialogeviewE.addEventListener('click', () => {
        dialogeviewE.style.display = 'flex'
    })
    OpenDialogeviewD.addEventListener('click', () => {
        dialogeviewD.style.display = 'flex'
    })
    OpenDialogeupdD.addEventListener('click', () => {
        dialogeupdD.style.display = 'flex'
    })
    OpenDialogeupdE.addEventListener('click', () => {
        dialogeupdE.style.display = 'flex'
    })
    OpenDialogeE.addEventListener('click', () => {
        dialogeE.style.display = 'flex'
    })
    OpenDialogeD.addEventListener('click', () => {
        dialogeD.style.display = 'flex'
    })
    OpenDialogeS.addEventListener('click', () => {
        dialogeS.style.display = 'flex'
    })
    closedialogviewE.addEventListener('click', () => {
        dialogeviewE.style.display = 'none'
    })
    closedialogviewD.addEventListener('click', () => {
        dialogeviewD.style.display = 'none'
    })
    closedialogE.addEventListener('click', () => {
        dialogeE.style.display = 'none'
    })
    closedialogD.addEventListener('click', () => {
        dialogeD.style.display = 'none'
    })
    closedialogS.addEventListener('click', () => {
        dialogeS.style.display = 'none'
    })
    closedialogupdD.addEventListener('click', () => {
        dialogeupdD.style.display = 'none'
    })
    closedialogupdE.addEventListener('click', () => {
        dialogeupdE.style.display = 'none'
    })


    var xValues = ['lun', 'mar', 'mer', 'jeu', 'ven', 'sam']
    new Chart("chart", {
        type: "line",
        data: {
            labels: xValues,
            datasets: [{
                data: [860, 1140, 10160, 1060, 8000, 1110],
                borderColor: "#695CFE",
                tension: 0.25,
                label: 'Encaissement',
                fill: false
            }, {
                data: [1600, 1700, 11060, 1900, 2000, 5700],
                tension: 0.25,
                label: 'Decaissement',
                borderColor: "rgb(75, 192, 192)",
                fill: false
            }]
        },
        options: {
            legend: { display: false }
        }
    });
