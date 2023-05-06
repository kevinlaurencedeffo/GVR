var li_items = document.querySelectorAll(".side_bar_bottom ul li");
var side_bar_menu = document.querySelector(".side_bar_menu");
var wrapper = document.querySelector(".wrapper");
const body = document.querySelector("body"),
      modeswitch = document.querySelector(".toggle-switch"),
      modetext = document.querySelector(".mode-text"),
      moon = document.querySelector(".moon");

li_items.forEach(function(li_main){
	li_main.addEventListener("click", function(){
		li_items.forEach(function(li){
			li.classList.remove("active");
		})
		li_main.classList.add("active");
	})
})

side_bar_menu.addEventListener("click", function(){
	wrapper.classList.toggle("active");
});

modeswitch.addEventListener("click", () => {
	body.classList.toggle("dark");

	if (body.classList.contains("dark")){
		moon.innerHTML = "🌞 Light Mode"

	}else{
		moon.innerHTML = "🌙 Dark Mode"
	}
  });