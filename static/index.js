document.querySelectorAll(".post").forEach((post) => {
    post.addEventListener("click", () => {
        location.replace("/page/" + post.id)
    })
})

document.querySelector("#discord_tag").addEventListener("click", () => {
    navigator.clipboard.write("therealshaqoatmeal")
    alert("Username has been copied to clipboard!!")
})