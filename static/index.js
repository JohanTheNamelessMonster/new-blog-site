document.querySelectorAll(".post").forEach((post) => {
    post.addEventListener("click", () => {
        location.replace("/page/" + post.id)
    })
})

document.querySelectorAll("#discord_tag").forEach(e => {
    e.addEventListener("click", () => {
        navigator.clipboard.write("therealshaqoatmeal")
        alert("Username has been copied to clipboard!!")
    })
})