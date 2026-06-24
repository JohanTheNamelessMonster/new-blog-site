document.querySelectorAll("#infoBox").forEach((element) => {
    element.addEventListener("click", (event) => {
        if (element.classList.contains("Github")) {
            location.replace("https://github.com/JohanTheNamelessMonster")
        } else if (element.classList.contains("Discord")) {
            navigator.clipboard.write("therealshaqoatmeal")
        } else if (element.classList.contains("GMail")) {
            location.replace("mailto:gouthamnair23@gmail.com")
        }
    })
})