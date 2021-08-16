const searchBtn = document.getElementById("banner__btn-search");
closeBtn = document.getElementById("banner__btn-close");
searchBox = document.getElementById("banner__search-box");
bannerInp = document.getElementById("banner__inp");

searchBtn.addEventListener("click", () => {
    searchBox.classList.add("search-box");
    bannerInp.classList.add("banner-inp");
    closeBtn.classList.add("banner-close");
});

closeBtn.addEventListener("click", () => {
    searchBox.classList.remove("search-box");
    bannerInp.classList.remove("banner-inp");
    closeBtn.classList.remove("banner-close");
});
