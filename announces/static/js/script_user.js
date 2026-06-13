const body = document.querySelector("body");

const user_image = document.getElementById("user_account_image");
var user_menu = document.getElementById("user_account_menu")

const menu_image = document.getElementById("vertical_menu_image")
const menu_container = document.getElementById("vertical_menu_container")

user_image.addEventListener("click", (e) => {
    if (user_menu.classList.contains("hidden")) {
        user_menu.classList.remove("hidden")
        user_menu.classList.add("flex")
    } else {
        user_menu.classList.add("hidden")
        user_menu.classList.remove("flex")
    }
})

menu_image.addEventListener("click", (e) => {
    if (menu_container.classList.contains("hidden")) {
        menu_container.classList.remove("hidden")
        menu_container.classList.add("flex")
    } else {
        menu_container.classList.add("hidden")
        menu_container.classList.remove("flex")
    }
})

body.addEventListener("click", (e) => {
    if (e.target != user_image) {
        user_menu.classList.add("hidden")
        user_menu.classList.remove("flex")
    }
    if (e.target != menu_image) {
        menu_container.classList.add("hidden")
        menu_container.classList.remove("flex")
    }
})