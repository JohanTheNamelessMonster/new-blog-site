const stylesInject = (target, stylesList, condition) => {
    condition = (condition) || ""
    document.querySelectorAll(target).forEach((t) => {
        stylesList.forEach(element => {
            t.classList.add(condition + element)
        });
    });
}

const stylesExtract = (target, styleList, condition) => {
    condition = condition || ""
    document.querySelectorAll(target).forEach((t) => {
        styleList.forEach(element => {
            t.classList.remove(element)
        })
    })
}

document.querySelector("#menuButtonBox").addEventListener("click", () => {
    stylesInject("#screen", ["blur-lg", "disabledScreen"])
    stylesExtract("#menuList", ["hidden"])
    stylesExtract("#titleBox", ["w-1/2"])
    stylesInject("#titleBox", ["w-full"])
    stylesInject("#menuList", ["block"])
    stylesInject("#hamburgerButton", ["hidden"])
})

document.querySelector("#menuCollapseButton").addEventListener("click", () => {
    stylesExtract("#screen", ["blur-lg", "disabledScreen"])
    stylesInject("#menuList", ["hidden"])
    stylesInject("#titleBox", ["w-1/2"])
    stylesExtract("#titleBox", ["w-full"])
    stylesExtract("#menuList", ["block"])
    stylesExtract("#hamburgerButton", ["hidden"])

})

// document.querySelector("#backgroundVideo").play()



function getElementCount(target) {
    let total = 0;
    document.querySelectorAll(target).forEach((t) => {
        total += 1
    });
    return total;
}

let navBarStyles = ["sticky", "w-full", "h-[60px]", "flex", "fadeUp"];
let titleBoxStyles = ["w-1/2", "content-center", "cursor-pointer"];
let titleStyles = ["text-center", "text-3xl", "font-extrabold", "text-transparent", "bg-linear-to-r", "from-violet-600", "to-red-700", "bg-clip-text"];
let pageLinkBoxStyles = ["grid", "grid-rows-4", "gap-4"];
let menuBoxStyle = ["w-1/4", "h-full", "content-center"];
let hamburgerButtonStyles = ["cursor-pointer", "stroke-gray-100"]
let linkBoxStyles = ["w-full", "justify-center", "items-center", "content-center"];
let linkStyles = ["text-center", "text-lg", "px-2", "py-2", "mt-8", "rounded-lg", "text-white"];
let linkHoverStyles = ["bg-white/10"];
let menuListStyle = ["absolute", "hidden", "top-0", "left-0", "lg:w-1/4", "h-full", "z-10", "pt-8"]
let backgroundVideoStyles = ["absolute", "top-0", "left-0", "min-w-full", "max-h-screen", "-z-10"]
let postBoxStyles = ["bg-indigo-200/25", "inset-shadow-sm", "inset-shadow-indigo-500", "rounded-xl", "mt-8", "w-[80vw]", "pb-4", "transition", "delay-150", "duration-750", "fadeUp"]
let postBoxHoverStyles = ["inset-shadow-purple-600", "inset-shadow-lg", "scale-110"]
let postTitleStyles = ["text-purple-600", "text-center", "text-4xl", "font-[Serif]"]
let nameStyle = ["text-7xl", "bg-linear-to-b", "from-gray-100", "to-gray-800", "bg-clip-text", "text-transparent", "fadeUp"]

stylesInject("#screen", ["scrollRegion"])
stylesInject("#navigationBar", navBarStyles)
stylesInject("#titleBox", titleBoxStyles)
stylesInject("#menuButtonBox", menuBoxStyle)
stylesInject("#hamburgerButton", hamburgerButtonStyles)
stylesInject("#pageLinksBox", pageLinkBoxStyles)
stylesInject("#linkBox", linkBoxStyles)
stylesInject("#title", titleStyles)
stylesInject("#Page", linkStyles)
stylesInject("#Page", linkHoverStyles, "hover:")
stylesInject("#menuList", menuListStyle)
stylesInject("#menuList", ["w-full"], "sm:")
stylesInject("#backgroundVideo", backgroundVideoStyles)
stylesInject("#backgroundImage", backgroundVideoStyles)
stylesInject(".postBox", postBoxStyles)
stylesInject(".postBox", postBoxHoverStyles, "hover:")
stylesInject("#postTitle", postTitleStyles)
stylesInject("#infoRegion", ["justify-center", "items-center", "grid"])
stylesInject("#infoBox", postBoxStyles)
stylesInject("#name", nameStyle)
stylesInject("#infoTitle", ["underline", "decoration-sky-500", "text-white", "text-3xl", "font-bold", "pl-8"])
stylesInject("#infoText", ["text-white", "text-lg", "font-semibold", "px-8", "mb-8"])
stylesInject("#infoButton", ["bg-indigo-700/50", "rounded-xl", "ml-8", "justify-center", "lg:w-2/5", "cursor-pointer", "mt-8", "transition", "delay-150", "duration-750", "px-8"])
stylesInject("#infoButton", ["bg-purple-700/50", "scale-110"], "hover:")
stylesInject("#infoButton", ["w-1/2"], "sm:")