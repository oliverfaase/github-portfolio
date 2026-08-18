const menuButton = document.querySelector(".menu-button");
const navigationLinks = document.querySelector(".nav-links");

if (menuButton && navigationLinks) {
  menuButton.addEventListener("click", () => {
    const isOpen = navigationLinks.classList.toggle("open");

    menuButton.setAttribute(
      "aria-expanded",
      String(isOpen)
    );
  });

  navigationLinks.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      navigationLinks.classList.remove("open");
      menuButton.setAttribute("aria-expanded", "false");
    });
  });
}
