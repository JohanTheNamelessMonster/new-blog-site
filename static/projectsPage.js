document.querySelectorAll(".cardClick").forEach(element => {
    element.addEventListener("click", (e) => {
        if (element.classList.contains("GithubCard")) {
            location.replace("https://github.com/JohanTheNamelessMonster/" + element.id)
        } else if (element.classList.contains("NotesCard")) {
            location.replace("/page/" + element.id)
        }
    })
})