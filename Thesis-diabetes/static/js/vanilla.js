const advisory = "The system is advisory in nature. \nIn case of doubt, consult a doctor!"

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
        showTitleAndHideResult();
    } else {
        document.getElementById('form').style.visibility = 'hidden';
        document.getElementById('warning').style.visibility = 'hidden';
        document.getElementById('info').innerText = advisory;
        document.getElementById('titleText').innerText = "Results";
    }
};

function hideRes() {
        document.getElementById('form').style.visibility = 'visible';
        document.getElementById('warning').style.visibility = 'visible';
        showTitleAndHideResult();

};

function showTitleAndHideResult() {
        document.getElementById('result').style.visibility = 'hidden';
        document.getElementById('titleText').innerText = "Fill out the form";
}