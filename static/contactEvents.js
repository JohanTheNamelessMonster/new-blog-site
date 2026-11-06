document.querySelectorAll("#infoBox").forEach((element) => {
    element.addEventListener("click", (event) => {
        if (element.classList.contains("Github")) {
            location.replace("https://github.com/JohanTheNamelessMonster")
        } else if (element.classList.contains("Discord")) {
	    alert("Discord usertag copied to clipboard!!")
            navigator.clipboard.writeText("therealshaqoatmeal")
        } else if (element.classList.contains("GMail")) {
            location.replace("mailto:gouthamnair23@gmail.com")
        }else if (element.classList.contains("LinkedIn")) {
            location.replace("https://www.linkedin.com/in/goutham-nair-728558441?utm_source=share_via&utm_content=profile")
        }
    })
})
