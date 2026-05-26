document.querySelectorAll(".post").forEach((post) => {
    post.addEventListener("click", () => {
        location.replace("/page/" + post.id)
    })
})