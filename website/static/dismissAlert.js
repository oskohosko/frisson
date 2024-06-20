// Little bit of js to show an alert for a few seconds
document.addEventListener("DOMContentLoaded", () => {
    const alertElement = document.getElementById("auto-dismiss-alert");
    if (alertElement) {
        setTimeout( () => {
            alertElement.classList.remove("show");
            setTimeout( () => {
                alertElement.parentNode.removeChild(alertElement);
            }, 300);
        }, 1000)
    }
});