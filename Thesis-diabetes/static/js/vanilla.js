document.addEventListener('DOMContentLoaded', () => {
    appear();
});

window.onload = function() {
    const form = document.getElementById('form');
    form.addEventListener("input", () => {
        document.getElementById('btnCancel').disabled = false
        document.getElementById('btnSubmit').disabled = !form.checkValidity()
    });
    form.addEventListener("reset", () => {
        document.getElementById('btnCancel').disabled = true
        document.getElementById('btnSubmit').disabled = true
    });
}

function appear() {
    if (!document.getElementById('phrase').innerText.includes('%')) {
        document.getElementById('result').style.visibility = 'hidden';
        document.getElementById('titleText').innerText = "Заполните форму";
    } else {
        document.getElementById('form').style.visibility = 'hidden';
        document.getElementById('warning').style.visibility = 'hidden';
        document.getElementById('info').innerText = "Система носит конcультационный характер. \nВ случае возникновения сомнений, обратитесь к врачу!";
        document.getElementById('titleText').innerText = "Результаты";
    }
};

function hideRes() {
        document.getElementById('form').style.visibility = 'visible';
        document.getElementById('warning').style.visibility = 'visible';
        document.getElementById('result').style.visibility = 'hidden';
        document.getElementById('titleText').innerText = "Заполните форму";
};
