const body = document.querySelector("body"),
      sidebar = document.querySelector(".sidebar"),
      toggle = document.querySelector(".toggle"),
      modeswitch = document.querySelector(".toggle-switch"),
      modetext = document.querySelector(".mode-text"),
      moon = document.querySelector(".moon"),
      link = document.querySelector(".nav-link");
      


      toggle.addEventListener("click", () => {
        sidebar.classList.toggle("close")
      });

      modeswitch.addEventListener("click", () => {
        body.classList.toggle("dark");

        if (body.classList.contains("dark")){
            modetext.innerHTML = "Light Mode"
            moon.innerHTML = "🌞"

        }else{
            modetext.innerHTML = "Dark Mode"
            moon.innerHTML = "🌙"
        }
      });

      link.addEventListener("click", () => {
        link.classList.toggle("color")
        link.style.background = "#695CFE"
      });
      
