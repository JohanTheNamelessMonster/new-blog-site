function checkPrime(num) {
    if ((2 ^ num % num) === 2) {
        return true;
    }
}

const encrypt = (key) => {
    let keyShift = 0

    for (let i = 0; i < key.length; i++) {
        keyShift += key.charCodeAt(i)
    }

    while (!checkPrime(keyShift)) {
        keyShift += 1
    }

    let checkValue = ""

    for (let i = 0; i < key.length; i++) {
        let newVal = (keyShift + key.charCodeAt(i)) % 126

        while (newVal > 126 || newVal < 33) {
            if (newVal > 126) {
                newVal = (newVal % 126) + 33
            } else {
                newVal = newVal + 55
            }
        }

        checkValue += String.fromCharCode(newVal)
    }

    return checkValue
}

document.querySelector("#submit").addEventListener("click", async (e) => {
    console.log("Submit clicked")
    var action = ""
    document.querySelectorAll(".command").forEach((command) => {
        if (command.checked) {
            action = command.value;
        }
    })

    var postPage = ""
    document.querySelectorAll(".postPage").forEach(page => {
        if (page.checked) {
            postPage = page.value
        }
    })

    if (postPage == "" || action == "" || document.querySelector("#title").value == "" || document.querySelector("#bodyText").value == "" || document.querySelector("#password").value == "") {
        alert("Invalid input as some field is missing")
        return 0
    }

    data = {
        title: document.querySelector("#titleText").value,
        body: document.querySelector("#bodyText").value,
        command: action,
        password: encrypt(document.querySelector("#password").value),
        oid: document.querySelector("#oid").value,
        page: postPage,
    }

    console.log(JSON.stringify({data}))

    const res = await fetch("/admin", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ data }),
    }).catch((e) => {
        console.log(e)
    }).then(reply => {
            if (reply.redirected) {
                window.location = reply.url
            } else if (reply.text() == "Invalid Password") {
                alert("Invalid Password")
            } else {
                console.log("There was a boo boo")
            }
        })
})